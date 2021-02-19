from flask import Blueprint
from pastastore.vote_engine import ve
from pastastore.logger import logger

get_recipe_api = Blueprint('get_recipe_api', __name__)


@get_recipe_api.route('/get_recipe/<recipe>', methods=['GET'])
def get_recipe(recipe):
    '''
    Handling the /get_recipe endpoint
    '''
    recipe = recipe.replace("_", " ")
    logger.info("{} {}".format("/get_recipe", recipe))

    try:
        msg, status_code = str(ve.get_vote(recipe)), 200
    except KeyError:
        msg, status_code = "{} has not been added so far".format(recipe), 400

    logger.info("{} {}".format(msg, status_code))
    return msg, status_code
