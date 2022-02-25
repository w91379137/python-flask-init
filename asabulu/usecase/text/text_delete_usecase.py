

from asabulu.domain.text.text_repository import TextRepository

class TextDeleteUsecaseInjection:
    textRepository: TextRepository

class TextDeleteUsecaseInput:
    id: int

class TextDeleteUsecase:

    def __init__(self, injection: TextDeleteUsecaseInjection) -> None:
        self.textRepository = injection.textRepository

    def execute(self, input: TextDeleteUsecaseInput) -> None:

        self.textRepository.delete_by_id(input.id)
        