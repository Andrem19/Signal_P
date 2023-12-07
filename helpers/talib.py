import talib

def rsi(closes, rsi_max_border, rsi_min_border, timeperiod): 
    rsi = talib.RSI(closes, timeperiod=timeperiod)
    
    if rsi[-1] < rsi_min_border:
        return 1
    elif rsi[-1] > rsi_max_border:
        return 2
    else:
        return 3