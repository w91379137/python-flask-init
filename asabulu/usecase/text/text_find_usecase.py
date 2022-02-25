

from typing import List
from asabulu.domain.text.text import Text
from asabulu.domain.text.text_repository import TextFindInput, TextFindOutput, TextRepository

class TextFindUsecaseInjection():
    textRepository: TextRepository

TextFindUsecaseInput = TextFindInput

TextFindUsecaseOutput = TextFindOutput

# @unique
# class TextFindUsecaseExceptionCode(IntEnum):

# class TextFindUsecaseException(Exception):

#     def __init__(self, message: str, code: TextFindUsecaseExceptionCode) -> None:
#         super().__init__(message)
#         self.code = code

class TextFindUsecase():

    def __init__(self, injection: TextFindUsecaseInjection) -> None:
        self.textRepository = injection.textRepository
    
    def execute(self, input: TextFindUsecaseInput) -> TextFindUsecaseOutput:
        
        output = self.textRepository.find(input)

        return output