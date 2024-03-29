
from flask import request, jsonify

from asabulu.usecase.text.text_create_usecase import TextCreateUsecaseInput, TextCreateUsecaseOutput
from ..tool import errorPrintHandle, getValueInArgBody

from asabulu.service import main
from asabulu.model.text.text_dao import TextSchema

def create():

    try:
        input = TextCreateUsecaseInput()
        input.value = getValueInArgBody(request, 'value')

        output = main.textCreateUsecase.execute(input)

    except Exception as e:
        errorPrintHandle(e)
        output = TextCreateUsecaseOutput()

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

