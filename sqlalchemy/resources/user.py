import sqlite3
import os 
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

__all__ = [
    'UserRegister'
]

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