import psycopg2
from src.database.db_conection import connect_db

def create_raw_table():
    """Crea la tabla raw_candidates para almacenar datos sin procesar."""
    conn = connect_db(db_name="candidates")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS raw_candidates (
        id SERIAL PRIMARY KEY,
        first_name TEXT,
        last_name TEXT,
        email VARCHAR(255),
        application_date DATE,
        country TEXT,
        yoe INTEGER,
        seniority TEXT,
        technology TEXT,
        code_challenge_score INTEGER,
        technical_interview_score INTEGER
    );
""")
    
    conn.commit()
    cursor.close()
    conn.close()
    print("Tabla raw_candidates creada correctamente.")

