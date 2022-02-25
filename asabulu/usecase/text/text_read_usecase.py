

from enum import IntEnum, unique
from typing import Optional
from asabulu.domain.text.text import Text
from asabulu.domain.text.text_repository import TextRepository

class TextReadUsecaseInjection():
    textRepository: TextRepository

class TextReadUsecaseInput():
    id: int

class TextReadUsecaseOutput():
    text: Optional[Text] = None

class TextReadUsecase():

    def __init__(self, injection: TextReadUsecaseInjection) -> None:
        self.textRepository = injection.textRepository
    
    def execute(self, input: TextReadUsecaseInput) -> TextReadUsecaseOutput:

        text = self.textRepository.find_by_id(input.id)
        
        output = TextReadUsecaseOutput()
        output.text = text
        return output