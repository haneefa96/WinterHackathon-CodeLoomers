# from app.config import db

# doc_ref = db.collection("test").add({
#     "message": "Firestore is working"
# })

# print("✅ Firestore connected successfully")
# from google.cloud import firestore

# db = firestore.Client()

# db.collection("test").add({"hello": "world"})
# print("Firestore OK")
from google.cloud import firestore

db = firestore.Client()

db.collection("test").add({"hello": "world"})
print("Firestore OK")
