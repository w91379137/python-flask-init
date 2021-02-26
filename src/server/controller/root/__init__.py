
from flask import Blueprint

api = Blueprint('root', __name__)

# curl http://localhost:5000/sayhello
# curl -X GET http://localhost:5000/sayhello
# curl -X POST --data "enter somethong"  http://localhost:5000/sayhello
from .sayhello import sayhello as _sayhello
@api.route('/sayhello', methods=['GET', 'POST'])
def sayhello():
    return _sayhello(**locals())