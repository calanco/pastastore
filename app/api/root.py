from flask import Blueprint

root_api = Blueprint('root_api', __name__)


@root_api.route('/', methods=['GET'])
def root():
    '''
    Handling the / endpoint
    '''
    return "Welcome to PastaStore!"
