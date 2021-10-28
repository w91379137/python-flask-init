
from asabulu.service import main
from flask import request, jsonify
from ..tool import getValueInArgBody
import json

def delete(id):

    try:

        # 格式
        Text = main.db.Text
        TextSchema = main.db.TextSchema

        # 輸入

        # 操作
        # result = Text.query.filter_by(value = value).all()

        try:
            dao = Text.query.filter_by(id = id).one()
        except:
            dao = None
        
        if dao is not None:
            dao.delete()

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

