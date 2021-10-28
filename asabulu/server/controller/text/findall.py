
from asabulu.service import main
from flask import request, jsonify
from ..tool import getValueInArgBody
import json

def findall():
    try:

        # 格式
        Text = main.db.Text
        TextSchema = main.db.TextSchema

        # 輸入
        page = getValueInArgBody(request, 'page')
        try:
            page = int(page)
        except:
            page = 1

        size = getValueInArgBody(request, 'size')
        try:
            size = int(size)
        except:
            size = 10
        
        result = Text.query.order_by(
            Text.id.desc()
        ).paginate(page, per_page = size)

        success = True
        items = result.items
        total = result.total
    except:
        success = False
        items = []
        total = 0

    result = TextSchema.dump(items, many = True)
    message = 'OK' if success else 'Fail'
    status = 200 if success else 400

    return jsonify(
        {
            "success": success, 
            "result": result,
            "message": message,

            "page": page,
            "size": size,
            "total": total,
        }), status

# http://localhost:5000/text/findall
# http://localhost:5000/text/findall?page=2&size=1