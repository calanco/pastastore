from flask import Blueprint, request
from app.recipes import RECIPES, RECIPE_COUNTS

store_blueprint = Blueprint('store_blueprint', __name__)


@store_blueprint.route('/store', methods=['POST'])
def store():
    '''
    Handling the /store endpoint
    '''
    json_data = request.json

    if "recipe" not in json_data:
        return "No recipe found", 400

    recipe = json_data["recipe"]
    if recipe not in RECIPES:
        return "Insert a valid recipe", 400

    add_recipe_count(recipe)

    return "{} has been added".format(recipe), 200


def add_recipe_count(recipe: str):
    '''
    Adding the inserted recipe to RECIPE_COUNTS dict
    '''
    if recipe not in RECIPE_COUNTS:
        RECIPE_COUNTS[recipe] = 0
    RECIPE_COUNTS[recipe] += 1
