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
        ## get the first row 
        row = result.fetchone()
        if row: 
            ## get all columns 
            user = User(row[0], row[1], row[2])
        else: 
            user = None
        connection.close()
        return user

