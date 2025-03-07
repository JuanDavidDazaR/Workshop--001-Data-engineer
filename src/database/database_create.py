from sqlalchemy import text
import json
import os
from src.database.db_conection import connect_db 


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CREDENTIALS_PATH = os.path.join(BASE_DIR, "credentials.json")

with open(CREDENTIALS_PATH, "r", encoding="utf-8") as file:
    credentials = json.load(file)

db_name = credentials["db_name"]

def create_database():
    try:
        engine = connect_db("postgres")
        with engine.connect() as connection:
            connection.execution_options(isolation_level="AUTOCOMMIT")

            result = connection.execute(text("SELECT 1 FROM pg_database WHERE datname= :db_name;"), {"db_name": db_name}).fetchone()

            if not result:
                connection.execute(text(f'CREATE DATABASE "{db_name}";'))
                print(f"Data base '{db_name}' successfully created.")
            else:
                print(f"Data base '{db_name}' already exists.")

    except Exception as e:
        print(f"Error when creating the database: {e}")












