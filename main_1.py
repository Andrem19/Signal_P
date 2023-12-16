import asyncio
import tracemalloc
from decouple import config
import helpers.tlg as tel
import helpers.firebase as fb
import datetime
import json
import copy
import shared_variables as sv
import helpers.services as serv
import coin_signal as cs
import time
from models.settings import Settings
from models.entity import Entity
import shared_variables as sv
import sys
import random

# Enable tracemalloc
tracemalloc.start()

# def run_main(args):
#     asyncio.run(main(args))

def get_fake_signal(coin):
    signal = random.randint(1, 3)
    hist = 'fake signal'
    timeframe = random.choice([1,5,15,30])
    incline_res = 0.05
    return signal, hist, timeframe, incline_res # coin, signal, set 1 or 2

async def handle_coin(coin: str, settings: Settings, minute: int, go: dict):
    try:
        settings.coin = coin
        signal, dataframe_hist, timeframe, incline_res = cs.get_signal(settings, minute, go)
        # signal, dataframe_hist, timeframe, incline_res = get_fake_signal(settings.coin)
        signals_dict = {}
        signals_dict[coin] = signal
        sl = incline_res
        target_len = 3
        signals_dict[f'dataframe_{coin}'] = dataframe_hist
        if signal == 1 or signal == 2:
            # handle_numbers_list(settings.coin)
            # if sv.coins_counter[settings.coin]['number'] < 2:
            if signal == 1:
                target_len = settings.target_len_1 if timeframe == 1 else settings.target_len_5 if timeframe == 5 else sv.settings.target_len_15 if timeframe == 15 else sv.settings.target_len_30
                kof = settings.st_sl_kof_long_1 if timeframe == 1 else settings.st_sl_kof_long_5 if timeframe == 5 else sv.settings.st_sl_kof_long_15 if timeframe == 15 else sv.settings.st_sl_kof_long_30
            elif signal == 2:
                target_len = settings.target_len_1_short if timeframe == 1 else settings.target_len_5_short if timeframe == 5 else sv.settings.target_len_15_short if timeframe == 15 else sv.settings.target_len_30_short
                kof = settings.st_sl_kof_short_1 if timeframe == 1 else settings.st_sl_kof_short_5 if timeframe == 5 else sv.settings.st_sl_kof_short_15 if timeframe == 15 else sv.settings.st_sl_kof_short_30
            sl = incline_res * kof
            targ_len = (target_len-1)*timeframe
            fb.write_new_signal(signal, settings.coin, sl, targ_len, timeframe)
            # sv.coins_counter[coin]['time'] = datetime.datetime.now().timestamp()
            # sv.coins_counter[coin]['number']+=1

        with sv.global_lock:
            sv.global_info_dict.update(signals_dict)
    except Exception as e:
        print(f'Error: {e}')
        with sv.global_lock:
            await tel.send_inform_message(f'Error: {e}', None, False)

def handle_numbers_list(coin: str):
    timestamp = sv.coins_counter[coin]['time']
    timestamp_expired = timestamp+1200 < datetime.datetime.now().timestamp()
    if timestamp_expired:
        sv.coins_counter[coin]['number'] = 0

async def main(args=None):
    if args is None:
        args = [0]
    my_id = args[0]
    coins = sv.collections[int(args[0])]
    serv.write_timestamp(f'watchdog/{my_id}.txt')
    msg = f'Procces number {int(args[0])+1} successfuly started'
    await tel.send_inform_message(msg, '', False)
    while True:
        try:
            time.sleep(3)
            current_time = datetime.datetime.now()

            if current_time.second in [56, 55, 56, 57]:
                if current_time.minute in [58, 28]:
                    sv.go['go_30'] = True
                if current_time.minute in [59, 4, 9, 14, 19, 24, 29, 34, 39, 44, 49, 54]:
                    sv.go['go_5'] = True
                    if current_time.minute in [59, 14, 29, 44]:
                        sv.go['go_15'] = True
                    else:
                        sv.go['go_15'] = False
                else:
                    sv.go_5 = False
                sv.current_minute = current_time.minute

                settings = Settings()
                serv.load_settings(settings)

                tasks = []
                for coin in coins:
                    task = asyncio.create_task(handle_coin(coin, copy.deepcopy(settings), copy.copy(sv.current_minute), copy.deepcopy(sv.go)))
                    tasks.append(task)

                await asyncio.gather(*tasks)

                if sv.go['go_5']:
                    message = serv.prettie_message(sv.global_info_dict, coins)
                    await tel.send_inform_message(message, '', False)
                    serv.write_timestamp(f'watchdog/{my_id}.txt')
                sv.go['go_5'] = False
                sv.go['go_15'] = False
                sv.go['go_30'] = False
                sv.aditional_message = ''
                sv.global_info_dict.clear()
                time.sleep(3)

        except Exception as e:
            print(f'Error: {e}')
            await tel.send_inform_message(f'Error: {e}', None, False)
            pass



if __name__ == "__main__":
    asyncio.run(main(sys.argv[1:]))