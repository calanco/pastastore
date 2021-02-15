from flask import Blueprint

root_blueprint = Blueprint('root_blueprint', __name__)


@root_blueprint.route('/', methods=['GET'])
def root():
    '''
    Handling the / endpoint
    '''
    return "Welcome to PastaStore!"
