from google.cloud import firestore
from google.cloud import storage

# Firestore client
db = firestore.Client()

# Cloud Storage client
storage_client = storage.Client()

PROJECT_ID = "codeloomers-484010"
from google.cloud import firestore
db = firestore.Client()