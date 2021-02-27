
def getValueInArgBody(request, key):

    if request.json is not None:
        # print(json.dumps(request.json))

        if key in request.json:
            return request.json[key]

    if request.args is not None:
        # print(json.dumps(request.args))
        return request.args.get(key)

