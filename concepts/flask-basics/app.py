from flask import Flask, jsonify, request

## __name__ gives each file a unique name 
app = Flask(__name__)

## needs to be converted to json for the client 
## json cannot be a list 
stores = [
    {
        'name': 'store1',
        'items': [
            { 'name': 'item 1' },
            { 'name': 'item 2' },
        ]
    },
    {
        'name': 'store2',
        'items': [
            { 'name': 'item 1' },
            { 'name': 'item 2' },
        ]
    }
]

## default method is 'GET'
@app.route('/', methods=['POST'])
def create_store():
    ## method to parse json from body
    data = request.get_json()
    new_store = {
        'name': data['name'],
        'items': data['items']
    }
    stores.append(new_store)
    return jsonify(new_store)

@app.route('/store/<string:name>')
def get_store(name):
    ## find the store by the name 
    store = [store for store in stores if store['name'] == name]
    if len(store) < 1:
        return { "error": "No store found" }
    ## otherwise return an error message 
    return jsonify(store[0])

@app.route('/store')
def get_stores():
    ## change the list to dictionary before making json
    ## this is because the json cannot be a list 
    return jsonify({ 'stores': stores })

@app.route('/store/<string:name>/item', methods=['POST'])
def create_item(name):
    ## find the store 
    store = [ store for store in stores if store['name'] == name]
    ## return an error if no store found 
    if len(store) < 1:
        return { "error": "No store found" }
    ## fetch data from the request 
    data = request.get_json()
    ## append an item with that data 
    store[0]['items'].append(data)
    ## return the updated store 
    return jsonify(store)

@app.route('/store/<string:name>/item')
def get_item(name):
    ## find the store by the name 
    store = [store for store in stores if store['name'] == name]
    if len(store) < 1:
        return { "error": "No store found" }
    ## return all the items in the store 
    return jsonify({ 'items': store[0]['items'] })

app.run(port=5000)