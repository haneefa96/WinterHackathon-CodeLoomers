from app.config import db

doc_ref = db.collection("test").add({
    "message": "Firestore is working"
})

print("✅ Firestore connected successfully")
