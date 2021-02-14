from flask import Flask
from pastastore.blueprints.root import root_blueprint

def create_app(name):
    app = Flask(name)
    app.register_blueprint(root_blueprint)
    return app
