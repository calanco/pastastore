from flask import Blueprint
from pastastore.vote_engine import ve
from pastastore.logger import logger

recipes_api = Blueprint('recipes_api', __name__)


@recipes_api.route('/recipes', methods=['GET'])
def recipes():
    '''
    Handling the /recipes endpoint
    '''
    logger.info("/recipes")

    try:
        msg, status_code = ve.get_votes(), 200
    except KeyError:
        msg, status_code = "No recipe has been added so far", 404

    logger.info(f"{msg} {status_code}")
    return msg, status_code
