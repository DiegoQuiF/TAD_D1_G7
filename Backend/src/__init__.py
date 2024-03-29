from flask import Flask
from .database.config import *
from .routes import index


app = Flask(__name__)

def init_app():
    app.register_blueprint( index.main, url_prefix = "/" )
    app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{user}:{password}@{host}/{dbname}'
    return app