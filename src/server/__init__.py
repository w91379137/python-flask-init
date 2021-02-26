
from flask import Flask

server = Flask(__name__)

from .controller import root
server.register_blueprint(root, url_prefix = '/')