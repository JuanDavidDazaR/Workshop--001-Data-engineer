from sqlalchemy import create_engine, text
from src.database.db_conection import connect_db

def create_database():
    """Crea la base de datos 'candidates' si no existe."""
    try:
        engine = connect_db("postgres")
        with engine.connect() as connection:
            connection.execution_options(isolation_level="AUTOCOMMIT")

            # Verificar si la base de datos ya existe
            result = connection.execute(text("SELECT 1 FROM pg_database WHERE datname='candidates';")).fetchone()

            if not result:
                connection.execute(text("CREATE DATABASE candidates;"))
                print("Base de datos 'candidates' creada exitosamente.")
            else:
                print("La base de datos 'candidates' ya existe.")

    except Exception as e:
        print(f"Error al crear la base de datos: {e}")

# Llamar a la función para probar
if __name__ == "__main__":
    create_database()


