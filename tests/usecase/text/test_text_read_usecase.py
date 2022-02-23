
# pytest -s tests/usecase/text/test_text_read_usecase.py

from asabulu.domain.text.text import Text
from asabulu.usecase.text.text_read_usecase import TextReadUsecase, TextReadUsecaseInjection, TextReadUsecaseInput
from tests.model.text.text_repository_memory_impl import TextRepositoryMemoryImpl

def test_TextReadUsecase():

    # Arrange
    injection = TextReadUsecaseInjection()
    aTextRepository = TextRepositoryMemoryImpl()
    injection.textRepository = aTextRepository

    aText = Text()
    aValue = 'hello world'
    aText.value = aValue
    aTextRepository.create(aText)

    input = TextReadUsecaseInput()
    input.id = 1
    
    usecase = TextReadUsecase(injection)

    # Act
    output = usecase.execute(input)

    # Assert
    assert output.text.id == 1
    assert output.text.value == aValue
