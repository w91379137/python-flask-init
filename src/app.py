
from server import server


# middleware
# https://stackoverflow.com/questions/51691730/flask-middleware-for-specific-route
from flask import request
import json
@server.before_request
def hook():
    # request - flask.request
    print(
        f"""
        [{request.method}]
        {request.url} {request.path}
        args: {json.dumps(request.args)}
        data: {request.data}
        [{request.endpoint}] """
    )

if __name__ == "__main__":
    server.run(host = "0.0.0.0", port = 5000, debug = True)
