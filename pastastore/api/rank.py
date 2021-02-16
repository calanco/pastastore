from flask import Blueprint
from pastastore.recipes import PASTA_RECIPE_COUNTS
from pastastore.api.utils import sort_pasta_recipes

rank_api = Blueprint('rank_api', __name__)


@rank_api.route('/rank', methods=['GET'])
def rank():
    '''
    Handling the /rank endpoint
    '''
    if not PASTA_RECIPE_COUNTS:
        return "No recipe has been added so far", 200

    sorted_pasta_recipe_counts = sort_pasta_recipes(PASTA_RECIPE_COUNTS)

    result = dict()
    rank = 1
    for recipe in sorted_pasta_recipe_counts:
        result[rank] = dict({"recipe": recipe[0], "votes": recipe[1]})
        rank += 1

    return result, 200
