from flask import Flask

# to make use of dotenv
from dotenv import load_dotenv
load_dotenv()

from .config import app_config 
from .models import db, bcrypt 

def create_app(env_name):
    
    ## app initializaion
    app = Flask(__name__)
    
    ## this way we pass in the name class based on the env type we pass
    app.config.from_object(app_config[env_name])
    
    ## hook bcrypt and models to this app 
    bcrypt.init_app(app)
    db.init_app(app)
    
    @app.route("/", methods=["GET"])
    def index():
        return "Welcome to Flask App"

    return app
