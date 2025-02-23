##*import psycopg2
#import json

# Cargar credenciales (usa la ruta correcta)
#with open("credentials.json", "r") as file:
#   conexion = json.load(file)

#try:
#    # Conectar a PostgreSQL
#    connection = psycopg2.connect(**conexion)
#    print(" Conexión exitosa a PostgreSQL")

#except psycopg2.Error as err:
#    print(f" Error al conectar a PostgreSQL: {err}")

import psycopg2
import json

# Cargar credenciales
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

def create_database():
    """Crear la base de datos si no existe."""
    conn = connect_db()
    conn.autocommit = True
    cursor = conn.cursor()
    db_name = "candidates_db"

    cursor.execute(f"SELECT 1 FROM pg_database WHERE datname = '{db_name}'")
    if not cursor.fetchone():
        cursor.execute(f"CREATE DATABASE {db_name}")
        print(f"Base de datos '{db_name}' creada.")

    cursor.close()
    conn.close()

if __name__ == "__main__":
    create_database()
