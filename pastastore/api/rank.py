from flask import Blueprint
from pastastore.vote_engine import ve

rank_api = Blueprint('rank_api', __name__)


@rank_api.route('/rank', methods=['GET'])
def rank():
    '''
    Handling the /rank endpoint
    '''
    if not ve.counts:
        return "No recipe has been added so far", 200

    sorted_pasta_recipe_counts = ve.sort_pasta_recipes(ve.counts)

    result = dict()
    rank = 1
    for recipe in sorted_pasta_recipe_counts:
        result[rank] = dict({"recipe": recipe[0], "votes": recipe[1]})
        rank += 1

    return result, 200
