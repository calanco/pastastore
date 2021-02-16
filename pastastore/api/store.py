from flask import Blueprint, request
from pastastore.vote_engine import ve

store_api = Blueprint('store_api', __name__)


@store_api.route('/store', methods=['POST'])
def store():
    '''
    Handling the /store endpoint
    '''
    json_data = request.json

    if "recipe" not in json_data:
        return "No recipe found", 400

    recipe = json_data["recipe"]
    if recipe not in ve.pasta_recipes:
        return "Insert a valid pasta recipe", 400

    ve.vote_recipe(recipe)

    return "{} has been added".format(recipe), 200
