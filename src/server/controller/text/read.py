
from service import main
from flask import request, jsonify
import json

def read(id):
    # https://marshmallow.readthedocs.io/en/3.0/examples.html

    try:
        # 格式
        Text = main.db.Text
        TextSchema = main.db.TextSchema

        # 輸入

        # 操作
        # dao = Text.query.get(id)
        dao = Text.query.filter_by(id = id).one()
    except:
        dao = {}

    json = TextSchema.dump(dao)

    success = 'id' in json
    result = TextSchema.dump(dao)
    message = 'OK' if success else 'Not found'
    status = 200 if success else 400
    
    return jsonify(
        {
            "success": success, 
            "result": result,
            "message": message,
        }), status
    
# http://localhost:5000/text/read/1