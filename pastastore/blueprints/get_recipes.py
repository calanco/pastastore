from flask import Blueprint
from pastastore.recipes import RECIPE_COUNTS

get_recipes_blueprint = Blueprint('get_recipes_blueprint', __name__)


@get_recipes_blueprint.route('/get_recipes', methods=['GET'])
def get_recipes():
    '''
    Handling the /get_recipes endpoint
    '''
    if not RECIPE_COUNTS:
        return "No recipe has been added so far", 200

    return RECIPE_COUNTS, 200
