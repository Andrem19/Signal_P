import requests
import numpy as np

def get_kline(coin: str, number_candles: int, interv: int):

    endpoint = f'/fapi/v1/klines?symbol={coin}&interval={interv}m&limit={number_candles}'
    url = 'https://fapi.binance.com' + endpoint
    response = requests.get(url).json()

    new_list = [[x[0], float(x[1]), float(x[2]), float(x[3]), float(x[4]), float(x[5])] for x in response]
    return np.array(new_list)