import threading
from decouple import config
from models.settings import Settings
from models.entity import Entity

global_lock = threading.Lock()

entity_1 = Entity('ent_1')
# entity_2 = Entity('ent_2')
entity_list = [entity_1]

settings: Settings = Settings()
coins_counter = {
    'XRPUSDT': {'number': 0, 'time': 0},
    'ADAUSDT': {'number': 0, 'time': 0},
    'DOGEUSDT': {'number': 0, 'time': 0},
    'AAVEUSDT': {'number': 0, 'time': 0},
    'EGLDUSDT': {'number': 0, 'time': 0},
    'FILUSDT': {'number': 0, 'time': 0},
    'ALGOUSDT': {'number': 0, 'time': 0},
    'ATOMUSDT': {'number': 0, 'time': 0},
    'GRTUSDT': {'number': 0, 'time': 0},
    'MANAUSDT': {'number': 0, 'time': 0},
    'GALAUSDT': {'number': 0, 'time': 0},
    'FTMUSDT': {'number': 0, 'time': 0},
    'EOSUSDT': {'number': 0, 'time': 0},
    'SANDUSDT': {'number': 0, 'time': 0},
    'DASHUSDT': {'number': 0, 'time': 0},
    'SNXUSDT': {'number': 0, 'time': 0},
    'THETAUSDT': {'number': 0, 'time': 0},
    'LTCUSDT': {'number': 0, 'time': 0},
    'KLAYUSDT': {'number': 0, 'time': 0},
    'SOLUSDT': {'number': 0, 'time': 0},
    'DYDXUSDT': {'number': 0, 'time': 0},
    'CRVUSDT': {'number': 0, 'time': 0},
    'APEUSDT': {'number': 0, 'time': 0},
    'MINAUSDT': {'number': 0, 'time': 0},
    'HBARUSDT': {'number': 0, 'time': 0},
    'UNIUSDT': {'number': 0, 'time': 0},
    'FLOWUSDT': {'number': 0, 'time': 0},
    'INJUSDT': {'number': 0, 'time': 0},
    'FXSUSDT': {'number': 0, 'time': 0},
    'ARBUSDT': {'number': 0, 'time': 0},
    'STXUSDT': {'number': 0, 'time': 0}
}

best_set = [
    'XRPUSDT',
    'ADAUSDT',
    'DOGEUSDT',
    'AAVEUSDT',
    'EGLDUSDT',
    'FILUSDT',
    'ALGOUSDT',
    'ATOMUSDT',
    'GRTUSDT',
    'MANAUSDT',
    'GALAUSDT',
    'FTMUSDT',
    'EOSUSDT',
    'SANDUSDT',
    'DASHUSDT',
    'SNXUSDT',
    'THETAUSDT',
    'LTCUSDT',
    'KLAYUSDT',
    'SOLUSDT',
    'DYDXUSDT',
    'CRVUSDT',
    'APEUSDT',
    'MINAUSDT',
    'HBARUSDT',
    'UNIUSDT',
    'FLOWUSDT',
    'INJUSDT',
    'FXSUSDT',
    'ARBUSDT',
    'STXUSDT'
]


collection_1 = ['XRPUSDT', 'EGLDUSDT', 'GRTUSDT', 'EOSUSDT', 'THETAUSDT', 'DYDXUSDT', 'HBARUSDT', 'FXSUSDT']
collection_2 = ['ADAUSDT', 'FILUSDT', 'MANAUSDT', 'SANDUSDT', 'LTCUSDT', 'CRVUSDT', 'UNIUSDT', 'ARBUSDT']

collection_3 = ['DOGEUSDT', 'ALGOUSDT', 'GALAUSDT', 'DASHUSDT', 'KLAYUSDT', 'APEUSDT', 'FLOWUSDT', 'STXUSDT']
collection_4 = ['AAVEUSDT', 'ATOMUSDT', 'FTMUSDT', 'SNXUSDT', 'SOLUSDT', 'MINAUSDT','INJUSDT']
collections = [collection_1, collection_2, collection_3, collection_4]



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

