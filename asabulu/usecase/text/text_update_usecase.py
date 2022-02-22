
from enum import IntEnum, unique
from typing import Optional

from asabulu.domain.text.text import Text
from asabulu.domain.text.text_repository import TextRepository

class TextUpdateUsecaseInjection():

    textRepository: TextRepository

class TextUpdateUsecaseInput():
    id: int
    value: Optional[str]
    count: Optional[int]

class TextUpdateUsecaseOuput():
    text: Optional[Text] = None

@unique
class TextUpdateUsecaseExceptionCode(IntEnum):
    id_found = 1

class TextUpdateUsecaseException(Exception):
    code: int

    def __init__(self, message: str, code: TextUpdateUsecaseExceptionCode) -> None:
        super().__init__(message)
        self.code = code

class TextUpdateUsecase():

    def __init__(self, injection: TextUpdateUsecaseInjection) -> None:
        self.textRepository = injection.textRepository

    def execute(self, input: TextUpdateUsecaseInput) -> TextUpdateUsecaseOuput:

        inputText = self.textRepository.find_by_id(input.id)
        if inputText is None:
            raise TextUpdateUsecaseException(f'text id:{id} not found, can not update', TextUpdateUsecaseExceptionCode.id_found)

        if input.value is not None:
            inputText.value = input.value

        if input.count is not None:
            inputText.count = input.count

        outputText = self.textRepository.update(inputText)

        output = TextUpdateUsecaseOuput()
        output.text = outputText
        
        return output