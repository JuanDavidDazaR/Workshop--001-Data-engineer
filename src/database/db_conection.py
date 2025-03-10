from sqlalchemy import create_engine
import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CREDENTIALS_PATH = os.path.join(BASE_DIR, "credentials.json")

with open(CREDENTIALS_PATH, "r", encoding="utf-8") as file:
    credentials = json.load(file)

def connect_db(db_name=None):
    database = db_name if db_name else credentials["db_name"]  
    return create_engine(
        f"postgresql://{credentials['user']}:{credentials['password']}@{credentials['host']}:{credentials['port']}/{database}"
    )






