import sqlite3

DB_NAME = "tasks.db"

def get_connection(db_path=DB_NAME):
    """Create and return a new database connection."""
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn

def initialize_db(conn):
    """Initialize the database with the tasks table."""
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT,
        due_date TEXT,
        done INTEGER DEFAULT 0
    )
    """)
    conn.commit()
