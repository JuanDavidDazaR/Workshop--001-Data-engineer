import mysql.connector
import json

with open("src/database/credentials.json", "r") as file:
    conexion = json.load(file)

try:
    connection = mysql.connector.connect(**conexion)

    if connection.is_connected():
        print("Conexión exitosa a MySQL")

except mysql.connector.Error as err:
    print(f"Error: {err}")

