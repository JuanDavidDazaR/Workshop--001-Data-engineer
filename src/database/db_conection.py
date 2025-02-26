import psycopg2
import json
import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CREDENTIALS_PATH = os.path.join(BASE_DIR, "credentials.json")

with open(CREDENTIALS_PATH, "r") as file:
    credentials = json.load(file)

def connect_db(db_name="postgres"):

    """Conectar a PostgreSQL."""
    return psycopg2.connect(
        dbname=db_name,
        user=credentials["user"],
        password=credentials["password"],
        host=credentials["host"],
        port=credentials["port"]
    )



