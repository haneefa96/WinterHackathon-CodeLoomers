from app.config import db

doc_ref = db.collection("test").document("ping")
doc_ref.set({"status": "connected"})

print("Firestore connection successful")
