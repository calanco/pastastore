from flask import Blueprint
from pastastore.vote_engine import ve

clean_api = Blueprint('clean_api', __name__)


@clean_api.route('/clean', methods=['GET'])
def root():
    '''
    Handling the /clean endpoint
    '''
    ve.clean_votes()
    return "Cleaned", 200
