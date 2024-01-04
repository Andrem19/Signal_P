import threading
from decouple import config
from models.settings import Settings
from models.entity import Entity

global_lock = threading.Lock()

entity_1 = Entity('ent_1')
# entity_2 = Entity('ent_2')
entity_list = [entity_1]

settings: Settings = Settings()
# coins_counter = {
#     'XRPUSDT': {'number': 0, 'time': 0},
#     'ADAUSDT': {'number': 0, 'time': 0},
#     'DOGEUSDT': {'number': 0, 'time': 0},
#     'AAVEUSDT': {'number': 0, 'time': 0},
#     'EGLDUSDT': {'number': 0, 'time': 0},
#     'FILUSDT': {'number': 0, 'time': 0},
#     'ALGOUSDT': {'number': 0, 'time': 0},
#     'ATOMUSDT': {'number': 0, 'time': 0},
#     'GRTUSDT': {'number': 0, 'time': 0},
#     'MANAUSDT': {'number': 0, 'time': 0},
#     'GALAUSDT': {'number': 0, 'time': 0},
#     'FTMUSDT': {'number': 0, 'time': 0},
#     'EOSUSDT': {'number': 0, 'time': 0},
#     'SANDUSDT': {'number': 0, 'time': 0},
#     'DASHUSDT': {'number': 0, 'time': 0},
#     'SNXUSDT': {'number': 0, 'time': 0},
#     'THETAUSDT': {'number': 0, 'time': 0},
#     'LTCUSDT': {'number': 0, 'time': 0},
#     'KLAYUSDT': {'number': 0, 'time': 0},
#     'SOLUSDT': {'number': 0, 'time': 0},
#     'DYDXUSDT': {'number': 0, 'time': 0},
#     'CRVUSDT': {'number': 0, 'time': 0},
#     'APEUSDT': {'number': 0, 'time': 0},
#     'MINAUSDT': {'number': 0, 'time': 0},
#     'HBARUSDT': {'number': 0, 'time': 0},
#     'UNIUSDT': {'number': 0, 'time': 0},
#     'FLOWUSDT': {'number': 0, 'time': 0},
#     'INJUSDT': {'number': 0, 'time': 0},
#     'FXSUSDT': {'number': 0, 'time': 0},
#     'ARBUSDT': {'number': 0, 'time': 0},
#     'STXUSDT': {'number': 0, 'time': 0}
# }

best_set = [
    'XRPUSDT', #55
    'DOGEUSDT', #50
    'KAVAUSDT', #50
    'IOTAUSDT', #50
    'ALGOUSDT', #45
    'SANDUSDT', #40
    'EOSUSDT', #40
    'ATOMUSDT', #40
    'LINKUSDT', #39
    'ADAUSDT', #38
    'GRTUSDT', #35
    'AAVEUSDT', #35
    'FILUSDT', #35
    'MANAUSDT', #32
    'EGLDUSDT', #30
    'AVAXUSDT', #30
    'XMRUSDT', #30
    'AXSUSDT', #30
    'NEOUSDT', #30
    'THETAUSDT', #30
    'GALAUSDT', #30
    'FTMUSDT', #25
    'SOLUSDT', #25
    'DYDXUSDT', #20
    'UNIUSDT', # 19
    'MINAUSDT', #17
    'HBARUSDT', #12
    'STXUSDT', #10
    'APTUSDT', #10
    'OPUSDT', #8
    'ARBUSDT', #7
    'APEUSDT', #6
    'INJUSDT', #4
    'QNTUSDT', #2
]


collection_1 = ['XRPUSDT', 'SANDUSDT', 'ADAUSDT', 'ALGOUSDT', 'AXSUSDT', 'MANAUSDT', 'UNIUSDT', 'APTUSDT', 'INJUSDT']
collection_2 = ['DOGEUSDT', 'EOSUSDT', 'GRTUSDT', 'EGLDUSDT', 'NEOUSDT', 'FTMUSDT', 'MINAUSDT', 'ARBUSDT', 'QNTUSDT']
collection_3 = ['KAVAUSDT', 'ATOMUSDT', 'AAVEUSDT', 'AVAXUSDT', 'THETAUSDT', 'SOLUSDT', 'HBARUSDT', 'APEUSDT']
collection_4 = ['IOTAUSDT', 'LINKUSDT', 'FILUSDT', 'XMRUSDT', 'GALAUSDT', 'DYDXUSDT', 'STXUSDT', 'OPUSDT']
collections = [collection_1, collection_2, collection_3, collection_4]

individual_settings = {
    'XRPUSDT': {
        'rsi': {1: 18, 5: 22, 15: 0, 30: 0},
        'bord': {1: 0, 5: 0, 15: 0, 30: 0},
        'targ_len': {1: 0, 5: 0, 15: 0, 30: 0}
    },
    'DOGEUSDT': {
        'rsi': {1: 22, 5: 26, 15: 0, 30: 0},
        'bord': {1: 0, 5: 0, 15: 0, 30: 0},
        'targ_len': {1: 0, 5: 12, 15: 0, 30: 0}
    },
    'KAVAUSDT': {
        'rsi': {1: 18, 5: 24, 15: 0, 30: 0},
        'bord': {1: 0, 5: 0, 15: 0, 30: 0},
        'targ_len': {1: 0, 5: 12, 15: 0, 30: 0}
    },
    'IOTAUSDT': {
        'rsi': {1: 16, 5: 22, 15: 0, 30: 0},
        'bord': {1: 0, 5: 0, 15: 0, 30: 0},
        'targ_len': {1: 0, 5: 0, 15: 0, 30: 0}
    },
    'SANDUSDT': {
        'rsi': {1: 18, 5: 22, 15: 0, 30: 0},
        'bord': {1: 0, 5: 0, 15: 0, 30: 0},
        'targ_len': {1: 0, 5: 0, 15: 0, 30: 0}
    },
    'EOSUSDT': {
        'rsi': {1: 22, 5: 22, 15: 0, 30: 0},
        'bord': {1: 0, 5: 0, 15: 0, 30: 0},
        'targ_len': {1: 0, 5: 0, 15: 0, 30: 0}
    },
    'ATOMUSDT': {
        'rsi': {1: 16, 5: 24, 15: 0, 30: 0},
        'bord': {1: 0, 5: 0, 15: 0, 30: 0},
        'targ_len': {1: 0, 5: 0, 15: 0, 30: 0}
    },
    'LINKUSDT': {
        'rsi': {1: 18, 5: 22, 15: 0, 30: 0},
        'bord': {1: 0, 5: 0, 15: 0, 30: 0},
        'targ_len': {1: 0, 5: 0, 15: 0, 30: 0}
    },
    'ADAUSDT': {
        'rsi': {1: 18, 5: 22, 15: 0, 30: 0},
        'bord': {1: 0, 5: 0, 15: 0, 30: 0},
        'targ_len': {1: 0, 5: 0, 15: 0, 30: 0}
    },
    'GRTUSDT': {
        'rsi': {1: 18, 5: 22, 15: 0, 30: 0},
        'bord': {1: 0, 5: 0, 15: 0, 30: 0},
        'targ_len': {1: 0, 5: 0, 15: 0, 30: 0}
    },
    'AAVEUSDT': {
        'rsi': {1: 12, 5: 24, 15: 0, 30: 0},
        'bord': {1: 0, 5: 0, 15: 0, 30: 0},
        'targ_len': {1: 0, 5: 0, 15: 0, 30: 0}
    },
    'FILUSDT': {
        'rsi': {1: 16, 5: 26, 15: 0, 30: 0},
        'bord': {1: 0, 5: 0, 15: 0, 30: 0},
        'targ_len': {1: 0, 5: 0, 15: 0, 30: 0}
    },
    'ALGOUSDT': {
        'rsi': {1: 18, 5: 24, 15: 0, 30: 0},
        'bord': {1: 0, 5: 0, 15: 0, 30: 0},
        'targ_len': {1: 0, 5: 0, 15: 0, 30: 0}
    },
    'EGLDUSDT': {
        'rsi': {1: 14, 5: 24, 15: 0, 30: 0},
        'bord': {1: 0, 5: 0, 15: 0, 30: 0},
        'targ_len': {1: 0, 5: 0, 15: 0, 30: 0}
    },
    'AVAXUSDT': {
        'rsi': {1: 12, 5: 24, 15: 0, 30: 0},
        'bord': {1: 0, 5: 0, 15: 0, 30: 0},
        'targ_len': {1: 0, 5: 0, 15: 0, 30: 0}
    },
    'XMRUSDT': {
        'rsi': {1: 0, 5: 18, 15: 0, 30: 0},
        'bord': {1: 0, 5: 0, 15: 0, 30: 0},
        'targ_len': {1: 0, 5: 0, 15: 0, 30: 0}
    },
    'AXSUSDT': {
        'rsi': {1: 18, 5: 22, 15: 0, 30: 0},
        'bord': {1: 0, 5: 0, 15: 0, 30: 0},
        'targ_len': {1: 0, 5: 0, 15: 0, 30: 0}
    },
    'NEOUSDT': {
        'rsi': {1: 16, 5: 22, 15: 0, 30: 0},
        'bord': {1: 0, 5: 0, 15: 0, 30: 0},
        'targ_len': {1: 0, 5: 0, 15: 0, 30: 0}
    },
    'THETAUSDT': {
        'rsi': {1: 20, 5: 22, 15: 0, 30: 0},
        'bord': {1: 0, 5: 0, 15: 0, 30: 0},
        'targ_len': {1: 0, 5: 0, 15: 0, 30: 0}
    },
    'GALAUSDT': {
        'rsi': {1: 18, 5: 22, 15: 0, 30: 0},
        'bord': {1: 0, 5: 0, 15: 0, 30: 0},
        'targ_len': {1: 0, 5: 0, 15: 0, 30: 0}
    },
    'MANAUSDT': {
        'rsi': {1: 14, 5: 26, 15: 0, 30: 0},
        'bord': {1: 0, 5: 0, 15: 0, 30: 0},
        'targ_len': {1: 0, 5: 0, 15: 0, 30: 0}
    },
    'FTMUSDT': {
        'rsi': {1: 20, 5: 22, 15: 0, 30: 0},
        'bord': {1: 0, 5: 0, 15: 0, 30: 0},
        'targ_len': {1: 0, 5: 0, 15: 0, 30: 0}
    },
    'SOLUSDT': {
        'rsi': {1: 20, 5: 24, 15: 0, 30: 0},
        'bord': {1: 0, 5: 0, 15: 0, 30: 0},
        'targ_len': {1: 0, 5: 0, 15: 0, 30: 0}
    },
    'DYDXUSDT': {
        'rsi': {1: 20, 5: 28, 15: 0, 30: 0},
        'bord': {1: 0, 5: 0, 15: 0, 30: 0},
        'targ_len': {1: 0, 5: 0, 15: 0, 30: 0}
    },
    'UNIUSDT': {
        'rsi': {1: 18, 5: 22, 15: 0, 30: 0},
        'bord': {1: 0, 5: 0, 15: 0, 30: 0},
        'targ_len': {1: 0, 5: 0, 15: 0, 30: 0}
    },
    'MINAUSDT': {
        'rsi': {1: 16, 5: 26, 15: 0, 30: 0},
        'bord': {1: 0, 5: 0, 15: 0, 30: 0},
        'targ_len': {1: 0, 5: 0, 15: 0, 30: 0}
    },
    'HBARUSDT': {
        'rsi': {1: 14, 5: 22, 15: 0, 30: 0},
        'bord': {1: 0, 5: 0, 15: 0, 30: 0},
        'targ_len': {1: 0, 5: 0, 15: 0, 30: 0}
    },
    'STXUSDT': {
        'rsi': {1: 18, 5: 24, 15: 0, 30: 0},
        'bord': {1: 0, 5: 0, 15: 0, 30: 0},
        'targ_len': {1: 0, 5: 0, 15: 0, 30: 0}
    },
    'APTUSDT': {
        'rsi': {1: 16, 5: 26, 15: 0, 30: 0},
        'bord': {1: 0, 5: 0, 15: 0, 30: 0},
        'targ_len': {1: 0, 5: 0, 15: 0, 30: 0}
    },
    'ARBUSDT': {
        'rsi': {1: 20, 5: 28, 15: 0, 30: 0},
        'bord': {1: 0, 5: 0, 15: 0, 30: 0},
        'targ_len': {1: 0, 5: 0, 15: 0, 30: 0}
    },
    'APEUSDT': {
        'rsi': {1: 16, 5: 28, 15: 0, 30: 0},
        'bord': {1: 0, 5: 0, 15: 0, 30: 0},
        'targ_len': {1: 0, 5: 0, 15: 0, 30: 0}
    },
    'OPUSDT': {
        'rsi': {1: 16, 5: 0, 15: 0, 30: 0},
        'bord': {1: 0, 5: 0, 15: 0, 30: 0},
        'targ_len': {1: 0, 5: 0, 15: 0, 30: 0}
    },
    'INJUSDT': {
        'rsi': {1: 18, 5: 30, 15: 0, 30: 0},
        'bord': {1: 0, 5: 0, 15: 0, 30: 0},
        'targ_len': {1: 0, 5: 0, 15: 0, 30: 0}
    },
    'QNTUSDT': {
        'rsi': {1: 0, 5: 30, 15: 0, 30: 0},
        'bord': {1: 0, 5: 0, 15: 0, 30: 0},
        'targ_len': {1: 0, 5: 0, 15: 0, 30: 0}
    },
}


global_info_dict = {}

current_minute = 0

go_1 = True
go_5 = False
go_15 = False
go_30 = False

go = {
    'go_1':True,
    'go_5':False,
    'go_15':False,
    'go_30':False,
}

aditional_message = ''

global_settings: Settings = Settings()

is_signal = False