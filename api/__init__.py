from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
import os

load_dotenv()

default_origins = "http://localhost:5173,http://localhost:3000"
ALLOWED_ORIGINS_STRING = os.environ.get("ALLOWED_ORIGINS", default_origins)
ALLOWED_ORIGINS_LIST = ALLOWED_ORIGINS_STRING.split(",")

def createApp():
    app = Flask(__name__)
    CORS(app, resources={r"/api/*": {"origins": ALLOWED_ORIGINS_LIST}})
    
    with app.app_context():
        from . import routes
        app.register_blueprint(routes.api_bp)
    
    return app