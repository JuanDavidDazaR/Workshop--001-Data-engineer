import psycopg2
import json

# Cargar credenciales (usa la ruta correcta)
with open("credentials.json", "r") as file:
    conexion = json.load(file)

try:
    # Conectar a PostgreSQL
    connection = psycopg2.connect(**conexion)
    print(" Conexión exitosa a PostgreSQL")

except psycopg2.Error as err:
    print(f" Error al conectar a PostgreSQL: {err}")

