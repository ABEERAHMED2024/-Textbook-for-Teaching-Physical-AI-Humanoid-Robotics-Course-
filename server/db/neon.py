import psycopg2
import os
import logging

def get_neon_connection():
    db_url = os.getenv("NEON_DATABASE_URL")
    if not db_url:
        logging.warning("NEON_DATABASE_URL not set. History will not be saved.")
        return None
    return psycopg2.connect(db_url)

def initialize_db():
    conn = get_neon_connection()
    if not conn:
        return
    try:
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS chat_history (
                    id SERIAL PRIMARY KEY,
                    message TEXT NOT NULL,
                    response TEXT NOT NULL,
                    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
        conn.commit()
    except Exception as e:
        logging.error(f"Failed to initialize DB: {e}")
    finally:
        conn.close()

def save_chat(message: str, response: str):
    conn = get_neon_connection()
    if not conn:
        return
    try:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO chat_history (message, response) VALUES (%s, %s)",
                (message, response)
            )
        conn.commit()
    except Exception as e:
        logging.error(f"Failed to save chat: {e}")
    finally:
        conn.close()
