from flask import Blueprint
from pastastore.logger import logger

root_api = Blueprint('root_api', __name__)


@root_api.route('/', methods=['GET'])
def root():
    '''
    Handling the / endpoint
    '''
    logger.info("/")

    msg = "Welcome to PastaStore!"
    logger.info(msg)
    return msg
