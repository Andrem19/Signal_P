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

# Enable tracemalloc
tracemalloc.start()

# def run_main(args):
#     asyncio.run(main(args))

def get_fake_signal(coin):
    return 1 # coin, signal, set 1 or 2

async def handle_coin(coin: str, settings: Settings, minute: int):
    try:
        settings.coin = coin
        signal, dataframe_hist, timeframe, incline_res = cs.get_signal(settings, minute)
        # signal = get_fake_signal(settings.coin)
        signals_dict = {}
        signals_dict[coin] = signal
        signals_dict['coin'] = coin
        sl = incline_res
        if signal != 3:
            kof = settings.st_sl_kof_long_1 if timeframe == 1 else settings.st_sl_kof_long_5 if timeframe == 5 else sv.settings.filter_border_15
            sl = incline_res * kof
        signals_dict['sl'] = sl
        signals_dict['t'] = timeframe
        signals_dict[f'dataframe_{coin}'] = dataframe_hist
        signals_dict['timestamp'] = datetime.datetime.now().timestamp()

        if signals_dict[coin] == 1 or signals_dict[coin] == 2:
            ent = None
            with sv.global_lock:
                ent = serv.get_free_ent(sv.entity_list, coin, signal)
            if ent is not None:
                for e in ent:
                    signals_dict['name'] = e.name
                    message_1 = json.dumps(signals_dict)

                    fb.write_data('signal', e.name, 'signal', message_1)
                    await tel.send_inform_message(f'I found trader {e.name} for signal {signal} {coin}', '', False)
            else:
                with sv.global_lock:
                    await tel.send_inform_message(f'I cant find trader for {signal} signal {coin}', '', False)
        signals_dict.pop('coin')
        with sv.global_lock:
            sv.global_info_dict.update(signals_dict)
    except Exception as e:
        print(f'Error: {e}')
        with sv.global_lock:
            await tel.send_inform_message(f'Error: {e}', None, False)

async def main(args=None):
    if args is None:
        args = [0]

    coins = sv.collections[int(args[0])]

    msg = f'Procces number {int(args[0])+1} successfuly started'
    await tel.send_inform_message(msg, '', False)
    while True:
        try:
            time.sleep(3)
            current_time = datetime.datetime.now()

            if current_time.second in [55, 56, 57, 58]:
                if current_time.minute in [59, 4, 9, 14, 19, 24, 29, 34, 39, 44, 49, 54]:
                    sv.go_5 = True
                    if current_time.minute in [59, 14, 29, 44]:
                        sv.go_15 = True
                    else:
                        sv.go_15 = False
                else:
                    sv.go_5 = False
                sv.current_minute = current_time.minute

                settings = Settings()
                serv.load_settings(settings)
                serv.read_entity_status(sv.entity_list)

                tasks = []
                for coin in coins:
                    task = asyncio.create_task(handle_coin(coin, copy.deepcopy(settings), copy.copy(sv.current_minute)))
                    tasks.append(task)

                await asyncio.gather(*tasks)

                if sv.go_5:
                    message = serv.prettie_message(sv.global_info_dict, coins)
                    await tel.send_inform_message(message, '', False)
                sv.go_5 = False
                sv.go_15 = False
                sv.aditional_message = ''
                sv.global_info_dict.clear()
                time.sleep(3)

        except Exception as e:
            print(f'Error: {e}')
            await tel.send_inform_message(f'Error: {e}', None, False)
            pass



if __name__ == "__main__":
    asyncio.run(main(sys.argv[1:]))