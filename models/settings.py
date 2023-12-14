import json

class Settings:
    def __init__(self):

        self.time_1 = True
        self.time_5 = True
        self.time_15 = True
        self.time_30 = True

        self.strategy = 'one' #one

        self.coin: str = 'BTCUSDT'
        self.chunk_len: int = 30
        self.only: int = 0

        self.filter_border_1 = 0.024
        self.filter_border_5 = 0.026
        self.filter_border_15 = 0.048
        self.filter_border_30 = 0.024


        self.timeperiod_1 = 30
        self.timeperiod_5 = 27
        self.timeperiod_15 = 22
        self.timeperiod_30 = 20


        self.rsi_min_border_1 = 18 #16
        self.rsi_min_border_5 = 22 #20
        self.rsi_min_border_15 = 22 #20
        self.rsi_min_border_30 = 22 #20

        self.rsi_max_border = 85

        self.st_sl_kof_long_1 = 0.08
        self.st_sl_kof_long_5 = 0.16
        self.st_sl_kof_long_15 = 0.18
        self.st_sl_kof_long_30 = 0.20

        self.st_sl_kof_short_1 = 0.18
        self.st_sl_kof_short_5 = 0.22
        self.st_sl_kof_short_15 = 0.16
        self.st_sl_kof_short_30 = 0.16

        self.adx_threshold_s_1 = 49
        self.rsi_threshold_s_1 = 88
        self.plus_di_treshold_s_1 = 47

        self.adx_threshold_s_5 = 50
        self.rsi_threshold_s_5 = 63
        self.plus_di_treshold_s_5 = 46

        self.adx_threshold_s_15 = 45
        self.rsi_threshold_s_15 = 80
        self.plus_di_treshold_s_15 = 48

        self.adx_threshold_s_30 = 46
        self.rsi_threshold_s_30 = 65
        self.plus_di_treshold_s_30 = 48

        self.target_len_1 = 6
        self.target_len_1_short = 4
        self.target_len_5 = 16
        self.target_len_5_short = 10
        self.target_len_15 = 3
        self.target_len_15_short = 4
        self.target_len_30 = 3
        self.target_len_30_short = 5


    def to_json(self):
        with open(f"settings/settings_UNIVERSAL.json", "w") as file:
            json.dump(self.__dict__, file, default=self.json_default)

    @staticmethod
    def json_default(obj):
        if isinstance(obj):
            return obj.to_dict()
        raise TypeError(f"Object of type {obj.__class__.__name__} is not JSON serializable")

    def from_json(self, path):
        with open(path, "r") as file:
            data = json.load(file)
            for key, value in data.items():
                setattr(self, key, value)

    @staticmethod
    def json_decode(data, obj_class):
        obj = obj_class()
        for key, value in data.items():
            setattr(obj, key, value)
        return obj
    
# set = Settings()
# set.to_json()