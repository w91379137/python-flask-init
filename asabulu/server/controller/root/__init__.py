
from flask import Blueprint

api = Blueprint('root', __name__)

'''
$ curl 'http://localhost:5000/sayhello'

$ curl -X GET \
    'http://localhost:5000/sayhello'

$ curl -X POST \
    -d '{"foo":"bar"}' \
    'http://localhost:5000/sayhello'

$ curl -X POST \
    -H 'Content-Type: application/json' \
    -d '{"foo":"bar"}' \
    'http://localhost:5000/sayhello?test=haha'
'''

from .sayhello import sayhello as _sayhello
@api.route('/sayhello', methods=['GET', 'POST'])
def sayhello():
    return _sayhello(**locals())