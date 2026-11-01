import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Connection to SQLite DB successful: {db_file}")
    except Error as e:
        print(e)
    return conn

def execute_query(conn, query):
    try:
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")




connection = create_connection("my_database.db")

user_table_query = """
CREATE TABLE IF NOT EXISTS users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT NOT NULL UNIQUE,
  email TEXT NOT NULL UNIQUE,
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
"""

create_posts_table="""
CREATE TABLE IF NOT EXISTS posts (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title TEXT NOT NULL,
  description TEXT NOT NULL,
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
  user_id INTEGER NOT NULL,
  FOREIGN KEY (user_id) REFERENCES users (id)
);
"""

execute_query(connection, user_table_query)
execute_query(connection, create_posts_table)

