import flask from Flask 
from .config import app_config 

def create_app(env_name):
    
    ## app initializaion
    app = Flask(__name__)
    app.config.from_object(app_config[env_name])

    @app.route("/", methods=["GET"])
    def index():
        return "Welcome to Flask App"

    return app
