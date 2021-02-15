from flask import Blueprint
from app.recipes import PASTA_RECIPE_COUNTS

get_recipes_api = Blueprint('get_recipes_api', __name__)


@get_recipes_api.route('/get_recipes', methods=['GET'])
def get_recipes():
    '''
    Handling the /get_recipes endpoint
    '''
    if not PASTA_RECIPE_COUNTS:
        return "No recipe has been added so far", 400

    return PASTA_RECIPE_COUNTS, 200
