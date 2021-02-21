from flask import Flask, jsonify

## __name__ gives each file a unique name 
app = Flask(__name__)

## needs to be converted to json for the client 
## json cannot be a list 
stores = [
    {
        'name': 'store 1',
        'items': [
            { 'name': 'item 1' },
            { 'name': 'item 2' },
        ]
    },
    {
        'name': 'store 2',
        'items': [
            { 'name': 'item 1' },
            { 'name': 'item 2' },
        ]
    }
]

## default method is 'GET'
@app.route('/', methods=['POST'])
def create_store():
    return { "response": "Store created" } 

@app.route('/store/<string:name>')
def get_store():
    return { "response": "Get Store" + name } 

@app.route('/store')
def get_stores():
    ## change the list to dictionary before making json
    ## this is because the json cannot be a list 
    return jsonify({ 'stores': stores })

@app.route('/store/<string:name>/item', methods=['POST'])
def create_item():
    pass 

@app.route('/store/<string:name>/item')
def get_item():
    pass

app.run(port=5000)