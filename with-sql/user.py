import sqlite3
import os 
from flask_restful import Resource, reqparse

SQL_URI = os.getenv("SQL_URI")

class User:
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

    @classmethod #cls === User 
    def find_by_username(cls, username):
        connection = sqlite3.connect(SQL_URI)
        cursor = connection.cursor()
        query = "SELECT * from users WHERE username=?"
        result = cursor.execute(query, (username,))
        ## get the first row 
        row = result.fetchone()
        if row: 
            ## get all columns 
            # user = cls(row[0], row[1], row[2])
            # or 
            user = cls(*row)
        else: 
            user = None
        connection.close()
        return user

    @classmethod
    def find_by_id(cls, _id):
        connection = sqlite3.connect(SQL_URI)
        cursor = connection.cursor()
        query = "SELECT * from users WHERE id=?"
        result = cursor.execute(query, (_id,))
        row = result.fetchone()
        if row: 
            user = cls(*row)
        else: 
            user = None
        connection.close()
        return user 


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'username',
        type=str,
        required=True,
        help="Must enter a valid username"
    )
    parser.add_argument(
        'password',
        type=str,
        required=True,
        help="Must enter a valid password"
    )
    def post(self):
        connection = sqlite3.connect(SQL_URI)
        cursor = connection.cursor()
        ## NULL because id is auto incrementing 
        query = 'INSERT INTO users VALUES(NULL, ?, ?)'
        data = UserRegister.parser.parse_args()
        cursor.execute(query, (data['username'], data['password']))
        connection.commit()
        connection.close()
        return { "message": "User created successfully" }