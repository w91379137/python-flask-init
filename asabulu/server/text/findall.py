
from asabulu.domain.text.text_repository import TextFindInput
from asabulu.service import main
from flask import request, jsonify
from ..tool import errorPrintHandle, getValueInArgBody
from asabulu.model.text.text_dao import TextSchema

def findall():
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
        
        input = TextFindInput()
        input.page = page
        input.size = size

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
        }), status
