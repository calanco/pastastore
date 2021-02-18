from flask import Blueprint
from pastastore.vote_engine import ve
from pastastore.logger import logger

get_recipes_api = Blueprint('get_recipes_api', __name__)


@get_recipes_api.route('/get_recipes', methods=['GET'])
def get_recipes():
    '''
    Handling the /get_recipes endpoint
    '''
    logger.info("/get_recipes")

    if not ve.get_votes():
        msg, status_code = "No recipe has been added so far", 400
    else:
        msg, status_code = ve.get_votes(), 200

    logger.info("{} {}".format(msg, status_code))
    return msg, status_code
