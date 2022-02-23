
from flask import jsonify

from asabulu.model.text.text_dao import TextSchema
from asabulu.server.tool import errorPrintHandle
from asabulu.service import main
from asabulu.usecase.text.text_update_usecase import TextUpdateUsecaseInput, TextUpdateUsecaseOuput

def read(id):
    # https://marshmallow.readthedocs.io/en/3.0/examples.html

    try:
        input = TextUpdateUsecaseInput()
        input.id = id

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
    