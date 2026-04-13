import sqlite3
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
db_path = PROJECT_ROOT / "inventory.db"


def create_connection():
    conn = sqlite3.connect(db_path)
    conn.execute("PRAGMA foreign_key = ON")
    return conn
