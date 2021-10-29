
from asabulu.view import app_instance
from asabulu.service import main

if __name__ == "__main__":
    config = main.config.server
    app_instance.run(host = config.host, port = config.port, debug = True)