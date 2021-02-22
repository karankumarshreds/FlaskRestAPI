from flask import Flask, request 
from flask_restful import Resource, Api
app = Flask(__name__)
api = Api(app)

## api works with resources 

## dummy data
items = []

class Item(Resource):
    ## get a specific item
    def get(self, name):
        ## filter does not return an array
        ## Next gets the first match or None 
        item = next(filter(lambda x: x['name'] == name, items), None)
        if item is None: 
            return {"message": "Not found error"}, 404 
        return item
    
    ## create a specific item
    def post(self, name):
        item = next(filter(lambda x: x['name'] == name, items), None)
        ## if item already exists
        if item:
            return {"message": "Item already exists"}, 400
        price = request.get_json()['price']
        item = { 'name': name, 'price': price }
        items.append(item)
        return item, 201

    
class ItemList(Resource):
    ## get item list
    def get(self):
        return items

api.add_resource(Item, '/items/<string:name>')
api.add_resource(ItemList, '/items')

app.run(port=5000, debug=True)
