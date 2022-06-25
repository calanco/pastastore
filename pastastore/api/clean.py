from flask import Blueprint
from pastastore.vote_engine import ve
from pastastore.logger import logger

clean_api = Blueprint('clean_api', __name__)


@clean_api.route('/clean', methods=['GET'])
def root():
    '''
    Handling the /clean endpoint
    '''
    logger.info("/clean")

    ve.clean_votes()

    msg, status_code = "Cleaned", 200
    logger.info(f"{msg} {status_code}")
    return msg, status_code
