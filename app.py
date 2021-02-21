from flask import Flask 

## __name__ gives each file a unique name 
app = Flask(__name__)

@app.route('/', method=['POST'])
def create_store():
    return { "response": "Store created" } 

@app.route('/store/<string:name>', method=['GET'])
def get_store():
    return { "response": "Get Store" + name } 

@app.route('/store')
def get_stores():
    return { "response": "All stores" }

@app.route('/store/<string:name>/item', methods=['POST'])
def create_item():
    pass 

@app.route('/store/<string:name>/item')
def get_item():
    pass

app.run(port=5000)