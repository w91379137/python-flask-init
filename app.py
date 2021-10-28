
from asabulu.view import app
from asabulu.service import main

app.run(host ='0.0.0.0', port = 5000, threaded=True)

if __name__ == "__main__":
    config = main.config.server
    app.run(host = config.host, port = config.port, debug = True)