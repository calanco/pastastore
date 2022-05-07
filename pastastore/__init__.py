from flask import Flask
from .api.clean import clean_api
from .api.recipe import recipe_api
from .api.recipes import recipes_api
from .api.rank import rank_api
from .api.root import root_api
from .api.vote import vote_api


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
    app.register_blueprint(clean_api)
    app.register_blueprint(recipe_api)
    app.register_blueprint(recipes_api)
    app.register_blueprint(rank_api)
    app.register_blueprint(root_api)
    app.register_blueprint(vote_api)
