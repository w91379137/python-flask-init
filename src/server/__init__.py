
from flask import Flask

server = Flask(__name__)

from .controller import root
server.register_blueprint(root, url_prefix = '/')

from .controller import status
server.register_blueprint(status, url_prefix = '/status')