from flask import Flask
from pastastore.blueprints.root import root_blueprint
from pastastore.blueprints.store import store_blueprint
from pastastore.blueprints.get_recipes import get_recipes_blueprint


def create_app(name):
    app = Flask(name)
    app.register_blueprint(root_blueprint)
    app.register_blueprint(store_blueprint)
    app.register_blueprint(get_recipes_blueprint)
    return app
