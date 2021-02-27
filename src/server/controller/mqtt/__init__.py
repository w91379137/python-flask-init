

from flask import Blueprint

api = Blueprint('mqtt', __name__)

'''
$ curl -X GET \
    'http://localhost:5000/mqtt/subscribe?topic=topic1'
'''

from .subscribe import subscribe as _subscribe
@api.route('/subscribe', methods=['GET', 'POST'])
def subscribe():
    return _subscribe(**locals())