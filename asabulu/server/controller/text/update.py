
from asabulu.service import main
from flask import request, jsonify
from ..tool import getValueInArgBody
import json

def update(id):

    try:

        # 格式
        Text = main.db.Text
        TextSchema = main.db.TextSchema

        # 輸入
        count = getValueInArgBody(request, 'count')
        try:
            count = int(count)
        except:
            count = 1

        try:
            dao = Text.query.filter_by(id = id).one()
        except:
            dao = None
        
        if dao is not None:
            dao.count = count
            dao.update()

    except:
        dao = {}

    json = TextSchema.dump(dao)
    # print(json)

    success = 'id' in json
    result = TextSchema.dump(dao)
    message = 'OK' if success else 'Fail'
    status = 200 if success else 400

    return jsonify(
        {
            "success": success, 
            "result": result,
            "message": message,
        }), status

# http://localhost:5000/text/update/1?count=40