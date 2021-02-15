from flask import Flask
from app.api.root import root_api
from app.api.store import store_api
from app.api.get_recipes import get_recipes_api
from app.api.rank import rank_api


def create_app(name) -> Flask:
    '''
    Creating the pastastore Flask application
    '''
    app = Flask(name)

    register_blueprints(app)

    return app


def register_blueprints(app: Flask):
    '''
    Registering all needed pastastore Flask apis
    '''
    app.register_blueprint(root_api)
    app.register_blueprint(store_api)
    app.register_blueprint(get_recipes_api)
    app.register_blueprint(rank_api)
