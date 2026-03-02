import sqlite3
import logging
from datetime import datetime

logger = logging.getLogger(__name__)

DB_PATH = "messages.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            username TEXT,
            full_name TEXT,
            message_text TEXT NOT NULL,
            timestamp TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()
    logger.info("Database initialized")

def save_message(user_id: int, username: str, full_name: str, message_text: str):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    timestamp = datetime.utcnow().isoformat()
    cursor.execute("""
        INSERT INTO messages (user_id, username, full_name, message_text, timestamp)
        VALUES (?, ?, ?, ?, ?)
    """, (user_id, username, full_name, message_text, timestamp))
    conn.commit()
    conn.close()
    logger.debug(f"Message from {user_id} saved to database")
