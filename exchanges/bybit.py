import time
import requests

url = "https://api.bybit.com"

def get_kline(coin: str, number_candles: int, interv: int):
        end = int(time.time() * 1000)  # current timestamp in milliseconds
        start = end - (number_candles * interv * 60 * 1000)  # calculate start timestamp
        endpoint= f'/v5/market/kline?category=inverse&symbol={coin}&interval={interv}&limit={number_candles}'
        uri = url + endpoint
        response = requests.get(uri).json()

        new_list = [[int(x[0]), float(x[1]), float(x[2]), float(x[3]), float(x[4]), float(x[5])] for x in response['result']['list']]
        reversed_list = new_list[::-1]
        return reversed_list