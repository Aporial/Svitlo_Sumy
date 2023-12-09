# import sqlite3

# DB_NAME = 'DATA_BASE.db'

# with sqlite3.connect(DB_NAME) as sqlite_conn:
#     sql_request = """CREATE TABLE "6_cherg" (
# 	"1"	TEXT,
# 	"2"	TEXT,
# 	"3"	TEXT,
# 	"4"	TEXT,
# 	"5"	TEXT,
# 	"6"	TEXT
#     );"""
#     sqlite_conn.execute(sql_request)

# with sqlite3.connect(DB_NAME) as sqlite_conn:
#     sql_request = "INSERT INTO courses VALUES(?, ?, ?, ?)"
#     sqlite_conn.execute(sql_request, (123, 'pepega', 100, 24))
#     sqlite_conn.commit()

# with sqlite3.connect(DB_NAME) as sqlite_conn:
#     sql_request = "SELECT one FROM '1_cherg'"
#     sql_cursor = sqlite_conn.execute(sql_request)
#     result_one = sql_cursor.fetchone()[0]
#     print(result_one)
#     result_two = sql_cursor.fetchone()[0]
#     print(result_two)
