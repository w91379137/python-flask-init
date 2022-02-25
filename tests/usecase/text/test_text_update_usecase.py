
# pytest -s tests/usecase/text/test_text_update_usecase.py

from asabulu.domain.text.text import Text
from asabulu.usecase.text.text_update_usecase import TextUpdateUsecase, TextUpdateUsecaseInjection, TextUpdateUsecaseInput
from tests.model.text.text_repository_memory_impl import TextRepositoryMemoryImpl


def test_TextUpdateUsecase():

    # Arrange
    injection = TextUpdateUsecaseInjection()
    aTextRepository = TextRepositoryMemoryImpl()
    injection.textRepository = aTextRepository

    aText = Text()
    aTextRepository.create(aText)
    
    aValue = "hello"
    aCount = 100

    input = TextUpdateUsecaseInput()
    input.id = 1
    input.value = aValue
    input.count = aCount
    
    usecase = TextUpdateUsecase(injection)

    # Act
    output = usecase.execute(input)
    
    # Assert
    assert output.text.count == aCount