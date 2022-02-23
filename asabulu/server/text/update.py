
from asabulu.service import main
from flask import request, jsonify

from asabulu.usecase.text.text_update_usecase import TextUpdateUsecaseInput, TextUpdateUsecaseOuput
from ..tool import errorPrintHandle, getValueInArgBody
import json
from asabulu.model.text.text_dao import TextSchema

def update(id):

    try:
        # 輸入
        count = getValueInArgBody(request, 'count')
        try:
            count = int(count)
        except:
            count = 1

        input = TextUpdateUsecaseInput()
        input.id = id
        input.count = count

        output = main.textUpdateUsecase.execute(input)

    except Exception as e:
        errorPrintHandle(e)
        output = TextUpdateUsecaseOuput()

    json = TextSchema.dump(output.text)
    # print(json)

    success = 'id' in json
    result = json
    message = 'OK' if success else 'Fail'
    status = 200 if success else 400

    return jsonify(
        {
            "success": success, 
            "result": result,
            "message": message,
        }), status
