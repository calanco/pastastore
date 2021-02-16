from flask import Blueprint
from pastastore.vote_engine import ve

get_recipe_api = Blueprint('get_recipe_api', __name__)


@get_recipe_api.route('/get_recipe/<recipe>', methods=['GET'])
def get_recipe(recipe):
    '''
    Handling the /get_recipe endpoint
    '''
    recipe = recipe.replace("_", " ")
    if recipe not in ve.counts:
        return "{} has not been added so far".format(recipe), 400

    return str(ve.counts[recipe]), 200
