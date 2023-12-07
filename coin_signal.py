from models.settings import Settings
import exchanges.bybit as bb
import exchanges.binance as bn
import shared_variables as sv
from datetime import datetime
import helpers.services as serv
import helpers.talib as ta
import numpy as np
import copy

def align_data(data: np.ndarray, minute: int):
    if minute != datetime.fromtimestamp(float(data[-1][0] / 1000)).minute:
        data = data[:-1]
    elif minute == datetime.fromtimestamp(float(data[-1][0] / 1000)).minute:
        data = data[1:]
    return data

def get_signal(settings: Settings, minute: int):
    add_m = ''
    step = ''
    if sv.go_5:
        chunk_5 = bn.get_kline(settings.coin, settings.chunk_len*2+1, 5)

        if len(chunk_5) < settings.chunk_len*2+1:
            chunk_5 = bb.get_kline(settings.coin, settings.chunk_len*2+1, 5)
        
        
        if len(chunk_5) == settings.chunk_len*2+1:
            step +='50 '
            chunk_5 = align_data(chunk_5, minute)
            closes_5 = chunk_5[:-settings.chunk_len, 4]
            incline_res_5 = serv.calculate_percent_difference(closes_5[0], closes_5[-1])
            if abs(incline_res_5) > settings.filter_border_5:
                step +='51 '
                data = chunk_5[:, 4]
                signal_5 = ta.rsi(data, settings.rsi_max_border, settings.rsi_min_border_5, settings.timeperiod_5)
                if signal_5 == 1:
                    if add_m != '':
                        sv.aditional_message+= f'\n{settings.coin} '
                        sv.aditional_message += add_m
                    return signal_5, step, 5, abs(incline_res_5)
        else:
            add_m + '5 lenerr; '
    if sv.go_1:
        chunk_1 = bn.get_kline(settings.coin, settings.chunk_len*2+1, 1)

        if len(chunk_1) < settings.chunk_len*2+1:
            chunk_1 = bb.get_kline(settings.coin, settings.chunk_len*2+1, 1)
        
        
        if len(chunk_1) == settings.chunk_len*2+1:
            step += '10 '
            chunk_1 = align_data(chunk_1, minute)
            closes_1 = chunk_1[:-settings.chunk_len, 4]
            incline_res_1 = serv.calculate_percent_difference(closes_1[0], closes_1[-1])
            if abs(incline_res_1) > settings.filter_border_1:
                step += '11 '
                data = chunk_1[:, 4]
                signal_1 = ta.rsi(data, settings.rsi_max_border, settings.rsi_min_border_1, settings.timeperiod_1)
                if signal_1 == 1:
                    if add_m != '':
                        sv.aditional_message+= f'\n{settings.coin} '
                        sv.aditional_message += add_m
                    return signal_1, step, 1, abs(incline_res_1)
        else:
            add_m + '1 lenerr; '
    if sv.go_15:
        chunk_15 = bn.get_kline(settings.coin, settings.chunk_len*2+1, 15)

        if len(chunk_15) < settings.chunk_len*2+1:
            chunk_15 = bb.get_kline(settings.coin, settings.chunk_len*2+1, 15)
        
        
        if len(chunk_15) == settings.chunk_len*2+1:
            step += '150 '
            chunk_15 = align_data(chunk_15, minute)
            closes_15 = chunk_15[:-settings.chunk_len, 4]
            incline_res_15 = serv.calculate_percent_difference(closes_15[0], closes_15[-1])
            if abs(incline_res_15) > settings.filter_border_15:
                step += '151 '
                data = chunk_15[:, 4]
                signal_15 = ta.rsi(data, settings.rsi_max_border, settings.rsi_min_border_15, settings.timeperiod_15)
                if signal_15 == 1:
                    if add_m != '':
                        sv.aditional_message+= f'\n{settings.coin} '
                        sv.aditional_message += add_m
                    return signal_15, step, 15,abs(incline_res_15)
        else:
            add_m + '15 lenerr; '
    if add_m != '':
        sv.aditional_message+= f'\n{settings.coin} '
        sv.aditional_message += add_m
    return 3, step, 0, 0