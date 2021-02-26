
from server import server

@server.route("/sayhello")
def hello():
    return "hello"

# curl http://localhost:5000/sayhello

if __name__ == "__main__":
    server.run(host = "0.0.0.0", port = 5000, debug = True)
