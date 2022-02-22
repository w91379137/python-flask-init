
# pytest -s tests/usecase/text/test_text_create_usecase.py

from tests.model.text.text_repository_memory_impl import TextRepositoryMemoryImpl
from asabulu.usecase.text.text_create_usecase import TextCreateUsecase, TextCreateUsecaseInjection, TextCreateUsecaseInput

def test_TextCreateUsecase():

    # 3A
    # https://blog.givemin5.com/tdd-1-unit-test-3a-yuan-ze/

    # Arrange
    injection = TextCreateUsecaseInjection()
    injection.textRepository = TextRepositoryMemoryImpl()

    aContent = 'hello world'

    input = TextCreateUsecaseInput()
    input.value = aContent
    usecase = TextCreateUsecase(injection)

    # Act
    output = usecase.execute(input)
    output = usecase.execute(input)
    
    # Assert
    assert output.text.value == aContent
    assert output.text.count == 1
