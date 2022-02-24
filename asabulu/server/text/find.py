
from asabulu.domain.text.text_repository import TextFindInput
from asabulu.service import main
from flask import request, jsonify
from ..tool import errorPrintHandle, getValueInArgBody
from asabulu.model.text.text_dao import TextSchema

def find():
    try:

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
        
        
        input = TextFindInput()
        input.page = page
        input.size = size
        input.value_eql = value_eql
        input.value_like = value_like
        input.count_eql = count_eql
        input.count_greater = count_greater
        input.count_lower = count_lower

        output = main.textFindUsecase.execute(input)

        success = True
        items = output.items
        total = output.total

    except Exception as e:
        
        errorPrintHandle(e)
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

