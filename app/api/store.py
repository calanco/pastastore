from flask import Blueprint, request
from app.recipes import PASTA_RECIPES, PASTA_RECIPE_COUNTS

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
    if recipe not in PASTA_RECIPES:
        return "Insert a valid pasta recipe", 400

    add_recipe_count(recipe)

    return "{} has been added".format(recipe), 200


def add_recipe_count(recipe: str):
    '''
    Adding the inserted recipe to PASTA_RECIPE_COUNTS dict
    '''
    if recipe not in PASTA_RECIPE_COUNTS:
        PASTA_RECIPE_COUNTS[recipe] = 0
    PASTA_RECIPE_COUNTS[recipe] += 1
