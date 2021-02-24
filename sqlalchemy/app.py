from flask import Flask, request 
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required 
## custom methods 
from security import authenticate, identity
## Resources
from resources.user import UserRegister
from resources.item import Item, ItemList

from dotenv import load_dotenv
import os 

load_dotenv()
secret_key = os.getenv("SECRET_KEY")
# print(f"My name is {name}")


app = Flask(__name__)
api = Api(app)

app.secret_key = secret_key

"""
JWT creates a new route /auth to which we send 
a username and a password and JWT sends it to 
the authenticate function. 
It returns the user and sends it to the identity
funciton, which returns the real user from the 
database

"""
jwt = JWT(app, authenticate, identity)

api.add_resource(Item, '/items/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')

app.run(port=5000, debug=True)
