import firebase_admin
from firebase_admin import credentials, firestore
import os
import base64
import json

# Get the FIREBASE_CREDENTIALS environment variable
firebase_creds_base64 = os.getenv("FIREBASE_CREDENTIALS")

if not firebase_creds_base64:
    raise ValueError("FIREBASE_CREDENTIALS environment variable is not set or empty.")

try:
    firebase_creds = json.loads(base64.b64decode(firebase_creds_base64).decode())
except json.JSONDecodeError:
    raise ValueError("Invalid FIREBASE_CREDENTIALS: Unable to decode JSON.")

# Initialize Firebase only if not already initialized
if not firebase_admin._apps:
    cred = credentials.Certificate(firebase_creds)
    firebase_admin.initialize_app(cred)

# Get Firestore client
db = firestore.client()
