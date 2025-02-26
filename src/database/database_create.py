import psycopg2
from src.database.db_conection import connect_db

def create_database():
    """Crea la base de datos 'candidates' si no existe."""
    try:
        # Conectar a la base de datos predeterminada (postgres)
        conn = connect_db(db_name="postgres")
        conn.autocommit = True  # Necesario para crear una base de datos
        cursor = conn.cursor()

        # Verificar si la base de datos ya existe
        cursor.execute("SELECT 1 FROM pg_database WHERE datname = 'candidates';")
        exists = cursor.fetchone()

        if not exists:
            cursor.execute("CREATE DATABASE candidates;")
            print("Base de datos 'candidates' creada exitosamente.")
        else:
            print("La base de datos 'candidates' ya existe.")

        # Cerrar conexión
        cursor.close()
        conn.close()

    except Exception as e:
        print(f"Error al crear la base de datos: {e}")

