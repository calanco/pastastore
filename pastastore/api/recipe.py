from flask import Blueprint
from pastastore.vote_engine import ve
from pastastore.logger import logger

recipe_api = Blueprint('recipe_api', __name__)


@recipe_api.route('/recipe/<recipe>', methods=['GET'])
def recipe(recipe):
    '''
    Handling the /recipe endpoint
    '''
    recipe = recipe.replace("_", " ")
    logger.info(f"/recipe {recipe}")

    try:
        msg, status_code = str(ve.get_vote(recipe)), 200
    except KeyError:
        msg, status_code = f"{recipe} has not been added so far", 404

    logger.info(f"{msg} {status_code}")
    return msg, status_code
