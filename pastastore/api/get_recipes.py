from flask import Blueprint
from pastastore.vote_engine import ve

get_recipes_api = Blueprint('get_recipes_api', __name__)


@get_recipes_api.route('/get_recipes', methods=['GET'])
def get_recipes():
    '''
    Handling the /get_recipes endpoint
    '''
    if not ve.counts:
        return "No recipe has been added so far", 400

    return ve.counts, 200
