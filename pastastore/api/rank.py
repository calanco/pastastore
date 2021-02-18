from flask import Blueprint
from pastastore.vote_engine import ve
from pastastore.logger import logger

rank_api = Blueprint('rank_api', __name__)


@rank_api.route('/rank', methods=['GET'])
def rank():
    '''
    Handling the /rank endpoint
    '''
    logger.info("/rank")

    if not ve.get_votes():
        msg, status_code = "No recipe has been added so far", 200
        logger.info("{} {}".format(msg, status_code))
        return msg, status_code

    sorted_pasta_recipe_counts = tuple(ve.sort_pasta_recipes(ve.get_votes()))

    result = dict()
    rank = 1
    for recipe in sorted_pasta_recipe_counts:
        result[rank] = dict({"recipe": recipe[0], "votes": recipe[1]})
        rank += 1

    msg, status_code = result, 200
    logger.info("{} {}".format(msg, status_code))
    return msg, status_code
