import talib

def rsi(closes, rsi_max_border, rsi_min_border, timeperiod): 
    rsi = talib.RSI(closes, timeperiod=timeperiod)
    if rsi[-1] < rsi_min_border:
        return 1
    elif rsi[-1] > rsi_max_border:
        return 2
    else:
        return 3
    
def detect_trend(highs, lows, closes, adx_trh, rsi_trh, di_trh):
    adx = talib.ADX(highs, lows, closes, timeperiod=24)
    plus_di = talib.PLUS_DI(highs, lows, closes, timeperiod=24)
    minus_di = talib.MINUS_DI(highs, lows, closes, timeperiod=24)
    rsi = talib.RSI(closes, timeperiod=20)

    if plus_di[-1]>adx_trh and rsi[-1]>rsi_trh and adx[-1]>di_trh:
        return 2
    # elif adx[-1] > adx_trh_l and rsi[-1]>rsi_trh_l and minus_di[-1]>di_trh_l:
    #     return 1
    return 3