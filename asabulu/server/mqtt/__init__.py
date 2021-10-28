

from flask import Blueprint

blueprint = Blueprint('mqtt', __name__)

'''
$ curl -X GET \
    'http://localhost:5000/mqtt/subscribe?topic=topic1'
'''

from .subscribe import subscribe as _subscribe
@blueprint.route('/subscribe', methods=['GET', 'POST'])
def subscribe():
    return _subscribe(**locals())


'''
$ curl -X GET \
    'http://localhost:5000/mqtt/publish?topic=topic1&msg=hello'
'''

from .publish import publish as _publish
@blueprint.route('/publish', methods=['GET', 'POST'])
def publish():
    return _publish(**locals())