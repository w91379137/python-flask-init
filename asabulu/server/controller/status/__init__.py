
from flask import Blueprint

api = Blueprint('status', __name__)

'''
$ curl http://localhost:5000/status/githash
'''

from .githash import githash as _githash
@api.route('/githash', methods=['GET', 'POST'])
def githash():
    return _githash(**locals())