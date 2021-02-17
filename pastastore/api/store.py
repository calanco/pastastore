from flask import Blueprint, request
from pastastore.vote_engine import ve
from pastastore.logger import logger

store_api = Blueprint('store_api', __name__)


@store_api.route('/store', methods=['POST'])
def store():
    '''
    Handling the /store endpoint
    '''
    json_data = request.json
    logger.info("{} {}".format("/store", json_data))

    if "recipe" not in json_data:
        msg, status_code = "No recipe found", 400
        logger.info("{} {}".format(msg, status_code))
        return msg, status_code

    recipe = json_data["recipe"]
    if recipe not in ve.pasta_recipes:
        msg, status_code = "Insert a valid pasta recipe", 400
        logger.info("{} {}".format(msg, status_code))
        return msg, status_code

    ve.vote_recipe(recipe)

    msg, status_code = "{} has been added".format(recipe), 200
    logger.info("{} {}".format(msg, status_code))
    return msg, status_code
