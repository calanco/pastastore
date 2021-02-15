from flask import Blueprint
from app.recipes import RECIPE_COUNTS
from app.api.utils import sort_recipes

rank_api = Blueprint('rank_api', __name__)


@rank_api.route('/rank', methods=['GET'])
def rank():
    '''
    Handling the /rank endpoint
    '''
    if not RECIPE_COUNTS:
        return "No recipe has been added so far", 200

    sorted_recipe_counts = sort_recipes(RECIPE_COUNTS)

    result = dict()
    rank = 1
    for recipe in sorted_recipe_counts:
        result[rank] = recipe
        rank += 1

    return result, 200
