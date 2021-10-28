
from asabulu.service import main
from flask import request, jsonify
from ..tool import getValueInArgBody
import json

def find():
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

        value_eql = getValueInArgBody(request, 'value_eql')
        value_like = getValueInArgBody(request, 'value_like')

        count_eql = getValueInArgBody(request, 'count_eql')
        try:
            count_eql = int(count_eql)
        except:
            count_eql = None

        count_greater = getValueInArgBody(request, 'count_greater')
        try:
            count_greater = int(count_greater)
        except:
            count_greater = None

        count_lower = getValueInArgBody(request, 'count_lower')
        try:
            count_lower = int(count_lower)
        except:
            count_lower = None
        
        result = Text.query

        if value_eql is not None:
            result = result.filter(Text.value == value_eql)

        if value_like is not None:
            result = result.filter(Text.value.like(f'%{value_like}%'))

        if count_eql is not None:
            # result = result.filter_by(count = count_eql)
            result = result.filter(Text.count == count_eql)

        if count_greater is not None:
            result = result.filter(Text.count > count_greater)

        if count_lower is not None:
            result = result.filter(Text.count < count_lower)

        result = result.order_by(
            Text.id.desc()
        )
        result = result.paginate(page, per_page = size)

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

            "value_eql": value_eql,
            "value_like": value_like,

            "count_eql": count_eql,
            "count_greater": count_greater,
            "count_lower": count_lower,
        }), status

# http://localhost:5000/text/find
# http://localhost:5000/text/find?count_lower=400&value_like=k