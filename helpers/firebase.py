import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

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