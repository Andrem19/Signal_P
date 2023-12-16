from models.settings import Settings
import exchanges.bybit as bb
import exchanges.binance as bn
import shared_variables as sv
from datetime import datetime
import helpers.services as serv
import helpers.talib as ta
import numpy as np
import copy

def align_data(data: np.ndarray, minute: int, timeframe: int):
    last_data_min = datetime.fromtimestamp(float(data[-1][0] / 1000)).minute
    if timeframe == 1:
        if minute != last_data_min:
            return data[:-1]
        elif minute == last_data_min:
            return data[1:]
    elif timeframe == 5 or timeframe == 15:
        if last_data_min == minute+1:
            return data[:-1]
        elif last_data_min == minute-(timeframe-1):
            return data[1:]
    elif timeframe == 30:
        if last_data_min == minute-(timeframe-2) or last_data_min == minute-(timeframe-1):
            return data[1:]
    return -1


def get_signal(settings: Settings, minute: int, go:dict):
    add_m = ''
    step = ''
    chunk_1 = None
    chunk_5 = None
    chunk_15 = None
    chunk_30 = None
    incline_res_1 = None
    closes_1 = None
    highs_1 = None
    lows_1 = None
    incline_res_5 = None
    closes_5 = None
    highs_5 = None
    lows_5 = None
    incline_res_15 = None
    closes_15 = None
    highs_15 = None
    lows_15 = None
    incline_res_30 = None
    closes_30 = None
    highs_30 = None
    lows_30 = None
    # ===================== 5 Preparation =====================
    if go['go_5']:
        chunk_5 = bn.get_kline(settings.coin, settings.chunk_len*2+1, 5)
        if len(chunk_5) < settings.chunk_len*2+1:
            chunk_5 = bb.get_kline(settings.coin, settings.chunk_len*2+1, 5)
        if len(chunk_5) == settings.chunk_len*2+1:
            chunk_5 = align_data(chunk_5, minute, 5)
            if isinstance(chunk_5, np.ndarray):
                closes_5 = chunk_5[:-settings.chunk_len, 4]
                incline_res_5 = serv.calculate_percent_difference(closes_5[0], closes_5[-1])
                if abs(incline_res_5) < settings.filter_border_5:
                    go['go_5'] = False
            else:
                add_m + '5 minuteerr; '
                go['go_5'] = False
        else:
            add_m + '5 lenerr; '
            go['go_5'] = False
    
    # ===================== 1 Preparation =====================
    if go['go_1']:
        chunk_1 = bn.get_kline(settings.coin, settings.chunk_len*2+1, 1)
        if len(chunk_1) < settings.chunk_len*2+1:
            chunk_1 = bb.get_kline(settings.coin, settings.chunk_len*2+1, 1)
        if len(chunk_1) == settings.chunk_len*2+1:
            chunk_1 = align_data(chunk_1, minute, 1)
            if isinstance(chunk_1, np.ndarray):
                closes_1 = chunk_1[:-settings.chunk_len, 4]
                incline_res_1 = serv.calculate_percent_difference(closes_1[0], closes_1[-1])
                if abs(incline_res_1) < settings.filter_border_1:
                    go['go_1'] = False
            else:
                add_m + '1 minuteerr; '
                go['go_1'] = False
        else:
            add_m + '1 lenerr; '
            go['go_1'] = False
    
    # ===================== 15 Preparation =====================
    if go['go_15']:
        chunk_15 = bn.get_kline(settings.coin, settings.chunk_len*2+1, 15)
        if len(chunk_15) < settings.chunk_len*2+1:
            chunk_15 = bb.get_kline(settings.coin, settings.chunk_len*2+1, 15)
        if len(chunk_15) == settings.chunk_len*2+1:
            chunk_15 = align_data(chunk_15, minute, 15)
            if isinstance(chunk_15, np.ndarray):
                closes_15 = chunk_15[:-settings.chunk_len, 4]
                incline_res_15 = serv.calculate_percent_difference(closes_15[0], closes_15[-1])
                if abs(incline_res_15) < settings.filter_border_15:
                    go['go_15'] = False
            else:
                add_m + '15 minuteerr; '
                go['go_15'] = False
        else:
            add_m + '15 lenerr; '
            go['go_15'] = False

    # ===================== 30 Preparation =====================
    if go['go_30']:
        chunk_30 = bn.get_kline(settings.coin, settings.chunk_len*2+1, 30)
        if len(chunk_30) < settings.chunk_len*2+1:
            chunk_30 = bb.get_kline(settings.coin, settings.chunk_len*2+1, 30)
        if len(chunk_30) == settings.chunk_len*2+1:
            chunk_30 = align_data(chunk_30, minute, 30)
            print(f'type_30: {type(chunk_30)}')
            print(f'type_30_len: {len(chunk_30)}')
            if isinstance(chunk_30, np.ndarray):
                closes_30 = chunk_30[:-settings.chunk_len, 4]
                incline_res_30 = serv.calculate_percent_difference(closes_30[0], closes_30[-1])
                if abs(incline_res_30) < settings.filter_border_30:
                    go['go_30'] = False
            else:
                add_m + '30 minuteerr; '
                go['go_30'] = False
        else:
            add_m + '30 lenerr; '
            go['go_30'] = False
    # ===================================================
    # =====================   LONG  =====================
    # ===================================================

    # ===================== 5 Long ======================
    if go['go_5']:
        data = chunk_5[:, 4]
        signal_5, rsi = ta.rsi(data, settings.rsi_max_border, settings.rsi_min_border_5, settings.timeperiod_5)
        step +=f'(5:{round(rsi,0)}) '
        if signal_5 == 1:
            if add_m != '':
                sv.aditional_message+= f'\n{settings.coin} '
                sv.aditional_message += add_m
            return signal_5, step, 5, abs(incline_res_5)
            
    # ===================== 1 Long ======================
    if go['go_1']:
        data = chunk_1[:, 4]
        signal_1, rsi = ta.rsi(data, settings.rsi_max_border, settings.rsi_min_border_1, settings.timeperiod_1)
        step +=f'(1:{round(rsi,0)}) '
        if signal_1 == 1:
            if add_m != '':
                sv.aditional_message+= f'\n{settings.coin} '
                sv.aditional_message += add_m
            return signal_1, step, 1, abs(incline_res_1)
        
    # ===================== 30 Long ======================
    if go['go_30']:
        data = chunk_30[:, 4]
        signal_30, rsi = ta.rsi(data, settings.rsi_max_border, settings.rsi_min_border_30, settings.timeperiod_30)
        step +=f'(30:{round(rsi,0)}) '
        if signal_30 == 1:
            if add_m != '':
                sv.aditional_message+= f'\n{settings.coin} '
                sv.aditional_message += add_m
            return signal_30, step, 30, abs(incline_res_30)

    # ===================== 15 Long ======================
    if go['go_15']:
        data = chunk_15[:, 4]
        signal_15, rsi = ta.rsi(data, settings.rsi_max_border, settings.rsi_min_border_15, settings.timeperiod_15)
        step +=f'(15:{round(rsi,1)}) '
        if signal_15 == 1:
            if add_m != '':
                sv.aditional_message+= f'\n{settings.coin} '
                sv.aditional_message += add_m
            return signal_15, step, 15,abs(incline_res_15)

    # ====================================================
    # =====================  SHORT  ======================
    # ====================================================

    # ===================== 15 Short =====================
    if go['go_15']:
        closes_15 = chunk_15[:, 4]
        highs_15 =  chunk_15[:, 2]
        lows_15 =  chunk_15[:, 3]
        signal_15,adxdi = ta.detect_trend(highs_15, lows_15, closes_15, settings.adx_threshold_s_15, settings.rsi_threshold_s_15, settings.plus_di_treshold_s_15)
        step += f'(adx-di 15:{adxdi}) '
        if signal_15 == 2:
            if add_m != '':
                sv.aditional_message+= f'\n{settings.coin} '
                sv.aditional_message += add_m
            return signal_15, step, 15, abs(incline_res_15)

    # ===================== 1 Short ======================

    # ===================== 30 Short =====================

    # ===================== 5 Short ======================
    if go['go_5']:
        closes_5 = chunk_5[:, 4]
        highs_5 =  chunk_5[:, 2]
        lows_5 =  chunk_5[:, 3]
        signal_5, adxdi = ta.detect_trend(highs_5, lows_5, closes_5, settings.adx_threshold_s_5, settings.rsi_threshold_s_5, settings.plus_di_treshold_s_5)
        step += f'(adx-di 5:{adxdi}) '
        if signal_5 == 2:
            if add_m != '':
                sv.aditional_message+= f'\n{settings.coin} '
                sv.aditional_message += add_m
            return signal_5, step, 5, abs(incline_res_5)


    if add_m != '':
        sv.aditional_message+= f'\n{settings.coin} '
        sv.aditional_message += add_m
    return 3, step, 0, 0