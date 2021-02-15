from flask import Blueprint
from app.recipes import RECIPE_COUNTS

get_recipes_api = Blueprint('get_recipes_api', __name__)


@get_recipes_api.route('/get_recipes', methods=['GET'])
def get_recipes():
    '''
    Handling the /get_recipes endpoint
    '''
    if not RECIPE_COUNTS:
        return "No recipe has been added so far", 200

    return RECIPE_COUNTS, 200
