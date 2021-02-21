from flask import Flask
from flask_restful import Resource, Api 

app = Flask(__name__)
api = Api(app)
## api works with resources 

## dummy data
items = []

class Item(Resource):
    ## get a specific item
    def get(self, name):
        item = [ item for item in items if item['name'] == name ]
        if len(item) < 1:
            return 
        return item[0]
    
    ## create a specific item
    def post(self, name):
        item = { 'name': name, 'price': 12 }
        items.append(item)
        return item
    
api.add_resource(Item, '/items/<string:name>')

app.run(port=5000)
