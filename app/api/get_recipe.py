from flask import Blueprint
from app.recipes import PASTA_RECIPE_COUNTS

get_recipe_api = Blueprint('get_recipe_api', __name__)


@get_recipe_api.route('/get_recipe/<recipe>', methods=['GET'])
def get_recipe(recipe):
    '''
    Handling the /get_recipe endpoint
    '''
    recipe = recipe.replace("_", " ")
    if recipe not in PASTA_RECIPE_COUNTS:
        return "{} has not been added so far".format(recipe), 400

    return str(PASTA_RECIPE_COUNTS[recipe]), 200
