from flask import Flask
from app.blueprints.root import root_blueprint
from app.blueprints.store import store_blueprint
from app.blueprints.get_recipes import get_recipes_blueprint
from app.blueprints.rank import rank_blueprint


def create_app(name) -> Flask:
    '''
    Creating the pastastore Flask application
    '''
    app = Flask(name)

    register_blueprints(app)

    return app


def register_blueprints(app: Flask):
    '''
    Registering all needed pastastore Flask blueprints
    '''
    app.register_blueprint(root_blueprint)
    app.register_blueprint(store_blueprint)
    app.register_blueprint(get_recipes_blueprint)
    app.register_blueprint(rank_blueprint)
