import sqlite3

def create_connection():
    conn = sqlite3.connect("users.db", check_same_thread=False)
    return conn

conn = create_connection()
cursor = conn.cursor()

def create_table():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT
    )
    """)
    conn.commit()