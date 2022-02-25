
# pytest -s tests/usecase/text/test_text_delete_usecase.py

from asabulu.domain.text.text import Text
from asabulu.usecase.text.text_delete_usecase import TextDeleteUsecase, TextDeleteUsecaseInjection, TextDeleteUsecaseInput
from tests.model.text.text_repository_memory_impl import TextRepositoryMemoryImpl


def test_TextDeleteUsecase():

    # Arrange
    injection = TextDeleteUsecaseInjection()
    aTextRepository = TextRepositoryMemoryImpl()
    injection.textRepository = aTextRepository

    aText = Text()
    aTextRepository.create(aText)

    input = TextDeleteUsecaseInput()
    aId = 1
    input.id = aId
    usecase = TextDeleteUsecase(injection)

    # Act
    usecase.execute(input)

    # Assert
    find_text = aTextRepository.find_by_id(aId)
    assert find_text == None
    