import threading
from decouple import config
from models.settings import Settings
from models.entity import Entity

global_lock = threading.Lock()

entity_1 = Entity('ent_1')
# entity_2 = Entity('ent_2')
entity_list = [entity_1]

settings: Settings = Settings()

best_set = [
     'ADAUSDT',
     'XRPUSDT',
     'UNIUSDT',
     'ATOMUSDT', 
     'FILUSDT',
     'ALGOUSDT', 
     'FTMUSDT', 
     'MANAUSDT',
     'GALAUSDT', 
     'DYDXUSDT',
     'DOGEUSDT',
     'SOLUSDT',
     'LTCUSDT',
     'HBARUSDT',
     'ARBUSDT',
     'AAVEUSDT',
     'GRTUSDT',
     'SNXUSDT',
     'STXUSDT',
     'EOSUSDT',
     'EGLDUSDT',
     'SANDUSDT',
     'THETAUSDT',
     'INJUSDT',
     'FLOWUSDT',
     'APEUSDT',
     'KLAYUSDT',
     'FXSUSDT',
     'MINAUSDT',
     'CRVUSDT',
     'DASHUSDT',
    ]


collection_1 = ['ADAUSDT','XRPUSDT','UNIUSDT','ATOMUSDT','FILUSDT','ALGOUSDT','FTMUSDT','MANAUSDT',]
collection_2 = ['GALAUSDT','DYDXUSDT','DOGEUSDT','SOLUSDT','LTCUSDT','HBARUSDT','ARBUSDT','AAVEUSDT',]

collection_3 = ['GRTUSDT','SNXUSDT','STXUSDT','EOSUSDT','EGLDUSDT','SANDUSDT','THETAUSDT','INJUSDT',]
collection_4 = ['FLOWUSDT','APEUSDT','KLAYUSDT','FXSUSDT','MINAUSDT','CRVUSDT','DASHUSDT',]
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

