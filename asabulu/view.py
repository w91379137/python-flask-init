
from asabulu.util import create_app
from asabulu.service import main

app_instance = create_app()

if __name__ == "__main__":
    config = main.config.server
    app_instance.run(host = config.host, port = config.port, debug = True)
