from flask import Blueprint
from pastastore.recipes import RECIPE_COUNTS

rank_blueprint = Blueprint('rank_blueprint', __name__)


@rank_blueprint.route('/rank', methods=['GET'])
def rank():
    '''
    Handling the /rank endpoint
    '''
    if not RECIPE_COUNTS:
        return "No recipe has been added so far", 200

    sorted_recipe_counts = sorted(RECIPE_COUNTS.items(),
                                  key=lambda item: item[1], reverse=True)

    result = dict()
    rank = 1
    for recipe in sorted_recipe_counts:
        result[rank] = recipe
        rank += 1

    return result, 200
