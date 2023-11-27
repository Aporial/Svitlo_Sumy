import sqlite3

DB_NAME = "sqlite_db.db"

with sqlite3.connect(DB_NAME) as sqlite_conn:
    print(sqlite_conn)
    print(sqlite3.version)