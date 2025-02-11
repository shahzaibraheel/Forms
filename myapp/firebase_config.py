import firebase_admin
from firebase_admin import credentials, firestore
import os
import base64
import json

# Decode the base64 Firebase credentials from the environment variable
firebase_creds = json.loads(
    base64.b64decode(os.getenv("FIREBASE_CREDENTIALS")).decode()
)

# Initialize Firebase only if not already initialized
if not firebase_admin._apps:
    cred = credentials.Certificate(firebase_creds)
    firebase_admin.initialize_app(cred)

# Get Firestore client
db = firestore.client()
