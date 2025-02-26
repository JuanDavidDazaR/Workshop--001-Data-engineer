from sqlalchemy import text
from src.database.db_conection import connect_db

def create_raw_table():
    """Crea la tabla clean_candidates para almacenar datos sin procesar."""
    engine = connect_db(db_name="candidates")

    with engine.connect() as conn:
        conn.execute(text("""
            CREATE TABLE IF NOT EXISTS clean_candidates (
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
        """))
        conn.commit()
    
    print("Tabla clean_candidates creada correctamente.")


