import firebase_admin
from firebase_admin import credentials
from models.settings import Settings
from firebase_admin import firestore
from datetime import datetime
# Initialize Firebase SDK
cred = credentials.Certificate('rychara-31314.json')
firebase_admin.initialize_app(cred)

# Create a Firestore client
db = firestore.client()

# Write data to Firestore
def write_data(collection, document, prop, signal):
    doc_ref = db.collection(collection).document(document)
    doc_ref.update({prop: signal})

# Read data from Firestore
def read_data(collection, document):
    doc_ref = db.collection(collection).document(document)
    doc = doc_ref.get()
    if doc.exists:
        return doc.to_dict()
    else:
        return None
def write_new_signal(signal: int, coin: str, sl: float, targ_len: int, timeframe: int):
    doc_ref = db.collection('coin_rating').document('coins')
    doc_ref.update({
        f'{coin}.sl': sl,
        f'{coin}.targ_len': targ_len,
        f'{coin}.signal': signal,
        f'{coin}.timeframe': timeframe,
        f'{coin}.timestamp': firestore.SERVER_TIMESTAMP,
    })

def write_settings(settings: Settings):
    doc_ref = db.collection('settings').document('signal')
    doc_ref.update(vars(settings))

def write_tmst(my_id: int):
    doc_ref = db.collection('settings').document('watchdog')
    doc_ref.update({
        f'ent_{my_id}': datetime.now().timestamp()
    })