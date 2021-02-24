from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

__all__ = [
    'Item',
    'ItemList'
]


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
        item = next(filter(lambda x: x['name'] == name, items), None)
        ## if item already exists
        if item:
            return {"message": "Item already exists"}, 400
        data = Item.parser.parse_args()
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
        item = next(filter(lambda x: x['name'] == name, items), None)
        data = Item.parser.parse_args()
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