
from flask import Blueprint

blueprint = Blueprint('status', __name__)

'''
$ curl http://localhost:5000/status/githash
'''

from .githash import githash as _githash
@blueprint.route('/githash', methods=['GET', 'POST'])
def githash():
    return _githash(**locals())