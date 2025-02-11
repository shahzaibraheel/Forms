import firebase_admin
from firebase_admin import credentials, firestore

import os

# Get the base directory of the Django project
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Construct the full path to Dso.json inside the "myapp" directory
FIREBASE_CREDENTIALS = os.path.join(BASE_DIR, "myapp", "Dso.json")

if not firebase_admin._apps:
    cred = credentials.Certificate(FIREBASE_CREDENTIALS)
    firebase_admin.initialize_app(cred)

db = firestore.client()
