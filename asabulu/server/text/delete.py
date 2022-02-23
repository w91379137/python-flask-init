
from asabulu.model.text.text_dao import TextSchema
from asabulu.service import main
from flask import request, jsonify

from asabulu.usecase.text.text_delete_usecase import TextDeleteUsecaseInjection
from ..tool import getValueInArgBody
import json

def delete(id):

    success = True
    try:
        input = TextDeleteUsecaseInjection()
        input.id = id

        main.textDeleteUsecase.execute(input)
    except Exception as e:
        print(f"Error({type(e).__name__}):{e}")
        # raise e
        success = False

    result = {}
    message = 'OK' if success else 'Fail'
    status = 200 if success else 400

    return jsonify(
        {
            "success": success, 
            "result": result,
            "message": message,
        }), status
