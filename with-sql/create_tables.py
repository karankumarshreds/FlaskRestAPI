import sqlite3
import os 

SQL_URI = os.getenv("SQL_URI")
connection = sqlite3.connect(SQL_URI)

cursor = connection.cursor()

## USE : INTEGER PRIMARY KEY for auto incrementing id 
create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"
cursor.execute(create_table)

connection.commit()
connection.close()