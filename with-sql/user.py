import sqlite3
import os 

SQL_URI = os.getenv("SQL_URI")

class User:
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

    def find_by_username(self, username):
        connection = sqlite3.connect(SQL_URI)
        cursor = connection.cursor()
        query = "SELECT * from users WHERE username=?"
        result = cursor.execute(query, (username,))

