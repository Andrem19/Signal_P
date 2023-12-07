import json

class Settings:
    def __init__(self):

        self.time_1 = True
        self.time_5 = True
        self.time_15 = True

        self.strategy = 'one' #one

        self.coin: str = 'BTCUSDT'
        self.chunk_len: int = 30
        self.only: int = 1

        self.filter_border_1 = 0.024
        self.filter_border_5 = 0.026
        self.filter_border_15 = 0.048
        self.timeperiod_1 = 30
        self.timeperiod_5 = 27
        self.timeperiod_15 = 22
        self.rsi_min_border_1 = 16
        self.rsi_min_border_5 = 20
        self.rsi_min_border_15 = 20
        self.rsi_max_border = 85
        self.st_sl_kof_long_1 = 0.08
        self.st_sl_kof_long_5 = 0.16
        self.st_sl_kof_long_15 = 0.18


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