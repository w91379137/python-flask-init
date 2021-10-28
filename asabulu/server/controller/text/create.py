
from service import main
from flask import request, jsonify
from ..tool import getValueInArgBody
import json

def create():

    try:

        # 格式
        Text = main.db.Text
        TextSchema = main.db.TextSchema

        # 輸入
        value = getValueInArgBody(request, 'value')

        if type(value) is not str:
            value = '何もありません' # 日文字存檔測試

        # 操作
        # result = Text.query.filter_by(value = value).all()

        try:
            dao = Text.query.filter_by(value = value).one()
        except:
            dao = None
        
        if dao is not None:
            dao.count = dao.count + 1
            dao.update()
        else:
            dao = Text(value = value)
            dao.save_to_db()

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

# http://localhost:5000/text/create
# http://localhost:5000/text/create?value=kkk