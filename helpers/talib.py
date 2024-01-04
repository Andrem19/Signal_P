import talib
import numpy as np
import helpers.services as serv

def rsi(closes, rsi_max_border, rsi_min_border, timeperiod, tm_frame): 
    rsi = talib.RSI(closes, timeperiod=timeperiod)
    rsi_to_return = rsi[-2] if tm_frame == 1 else rsi[-1]
    if rsi[-1] < rsi_min_border:
        return 1, rsi_to_return
    elif rsi[-1] > rsi_max_border:
        return 2, rsi_to_return
    else:
        return 3, rsi_to_return
    
def detect_trend(highs, lows, closes, adx_trh, rsi_trh, di_trh):
    adx = talib.ADX(highs, lows, closes, timeperiod=24)
    plus_di = talib.PLUS_DI(highs, lows, closes, timeperiod=24)
    minus_di = talib.MINUS_DI(highs, lows, closes, timeperiod=24)
    rsi = talib.RSI(closes, timeperiod=20)

    if plus_di[-1]>di_trh and rsi[-1]>rsi_trh and adx[-1]>adx_trh:
        return 2, (round(adx[-1],2), round(plus_di[-1],2))
    # elif adx[-1] > adx_trh_l and rsi[-1]>rsi_trh_l and minus_di[-1]>di_trh_l:
    #     return 1
    return 3, (round(adx[-1],2), round(plus_di[-1],2))

def detect_trend_2(highs, lows, closes):
    adx = talib.ADX(highs, lows, closes, timeperiod=16)
    plus_di = talib.PLUS_DI(highs, lows, closes, timeperiod=22)
    minus_di = talib.MINUS_DI(highs, lows, closes, timeperiod=24)
    rsi = talib.RSI(closes, timeperiod=19)

    if minus_di[-1]> plus_di[-1]\
        and rsi[-1]> 60\
        and adx[-1]< 40:
        return 2
    else:
        return 3
    
def comb(one, two, three):
    combinations = [
        [2,1,2],
        [1,0,2],
        [1,2,2],
        [1,2,1],
    ]
    if [one, two, three] in combinations:
        return True
    else:
        return False

def rsi_direction(closes: np.ndarray):
    incline_res = serv.calculate_percent_difference(closes[-30], closes[-1])
    if abs(incline_res) < 0.040:
        return 3, 'dir '
    rsi = talib.RSI(closes, timeperiod=27)

    row_1 = serv.chose_arr(0, closes[:-10], 10)
    row_2 = serv.chose_arr(3, closes[:-10], 10)

    trend = all(np.diff(row_1) > 0) or all(np.diff(row_2) > 0)

    zero_rsi = np.diff(rsi[-14:-10])
    one_rsi = np.diff(rsi[-10:-6])
    last_rsi = np.diff(rsi[-6:-1])

    zero = 1 if all(zero_rsi > 0) else 2 if all(zero_rsi < 0) else 0
    one = 1 if all(one_rsi > 0) else 2 if all(one_rsi < 0) else 0
    last = 1 if all(last_rsi > 0) else 2 if all(last_rsi < 0) else 0

    if zero == 0 and one == 0 and last == 2 and rsi[-1] > 28 and rsi[-1] < 50 and trend:
        return 1, f'{zero}-{one}-{last} '
    elif comb(zero, one, last) and rsi[-1] > 28 and rsi[-1] < 40:
        return 1, f'{zero}-{one}-{last} '
    else:
        return 3, f'{zero}-{one}-{last} '