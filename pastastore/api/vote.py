from flask import Blueprint, request
from pastastore.vote_engine import ve
from pastastore.logger import logger
from pastastore.recipe_error import RecipeError

vote_api = Blueprint('vote_api', __name__)


@vote_api.route('/vote', methods=['POST'])
def vote():
    '''
    Handling the /vote endpoint
    '''
    json_data = request.json
    logger.info(f"/vote {json_data}")

    if "recipe" not in json_data:
        msg, status_code = "No recipe found", 404
        logger.info(f"{msg} {status_code}")
        return msg, status_code

    recipe = json_data["recipe"]

    msg, status_code = "", ""
    try:
        ve.vote_recipe(recipe)
    except RecipeError as re:
        msg, status_code = str(re), 400
    else:
        msg, status_code = f"{recipe} has been added", 200

    logger.info(f"{msg} {status_code}")
    return msg, status_code
