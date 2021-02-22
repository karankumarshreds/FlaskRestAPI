from flask import Flask, request 
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required 
from security import authenticate, identity

app = Flask(__name__)
api = Api(app)

app.secret_key = 'We3$//kjh'

"""
JWT creates a new route /auth to which we send 
a username and a password and JWT sends it to 
the authenticate function. 
It returns the user and sends it to the identity
funciton, which returns the real user from the 
database

"""
jwt = JWT(app, authenticate, identity)

## dummy data
items = []

class Item(Resource):

    # data = request.get_json()
    ## body validation
    parser = reqparse.RequestParser()
    parser.add_argument(
        'price', 
        type=float, 
        required=True, 
        help="This field cannot be left blank" 
    )

    # returns access_token if validated
    @jwt_required()
    def get(self, name):
        ## filter does not return an array
        ## Next gets the first match or None 
        item = next(filter(lambda x: x['name'] == name, items), None)
        if item is None: 
            return {"message": "Not found error"}, 404 
        return item
    
    ## create a specific item
    def post(self, name):
        data = Item.parser.parse_args()
        item = next(filter(lambda x: x['name'] == name, items), None)
        ## if item already exists
        if item:
            return {"message": "Item already exists"}, 400
        item = { 'name': name, 'price': data['price'] }
        items.append(item)
        return item, 201
    
    @jwt_required()
    def delete(self, name):
        global items
        _items = list(filter(lambda x: x['name'] != name, items))
        items = _items 
        return items

    def put(self, name):
        data = Item.parser.parse_args()
        item = next(filter(lambda x: x['name'] == name, items), None)
        if item is None:
            item = { 'name': name, 'price': data['price'] }
            items.append(item)
        else:
            item.update(data)
        return item, 201
    
class ItemList(Resource):
    ## get item list
    def get(self):
        return items

api.add_resource(Item, '/items/<string:name>')
api.add_resource(ItemList, '/items')

app.run(port=5000, debug=True)
