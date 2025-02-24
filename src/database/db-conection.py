
import psycopg2
import json

with open("credentials.json", "r") as file:
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
    return conn


