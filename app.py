from flask import Flask 

## __name__ gives each file a unique name 
app = Flask(__name__)

@app.route('/')
def home():
    return { "Response": "Home page" }

app.run(port=5000)