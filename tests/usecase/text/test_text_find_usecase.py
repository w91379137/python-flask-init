
# pytest -s tests/usecase/text/test_text_find_usecase.py

from asabulu.domain.text.text import Text
from asabulu.usecase.text.text_find_usecase import TextFindUsecase, TextFindUsecaseInjection, TextFindUsecaseInput
from tests.model.text.text_repository_memory_impl import TextRepositoryMemoryImpl


def test_TextFindUsecase():

    # Arrange
    injection = TextFindUsecaseInjection()
    aTextRepository = TextRepositoryMemoryImpl()
    injection.textRepository = aTextRepository

    if True:
        aText = Text(value="abc", count=1)
        aTextRepository.create(aText)

    if True:
        aText = Text(value="def", count=3)
        aTextRepository.create(aText)

    usecase = TextFindUsecase(injection)

    if True:
        input = TextFindUsecaseInput()
        input.value_eql = "abc"

        # Act
        output = usecase.execute(input)

        # Assert
        find_text = output.items[0]
        assert find_text.value == "abc"
    
    if True:
        input = TextFindUsecaseInput()
        input.value_like = "a"

        # Act
        output = usecase.execute(input)

        # Assert
        find_text = output.items[0]
        assert find_text.value == "abc"

    if True:
        input = TextFindUsecaseInput()
        input.count_eql = 1

        # Act
        output = usecase.execute(input)

        # Assert
        find_text = output.items[0]
        assert find_text.value == "abc"

    if True:
        input = TextFindUsecaseInput()
        input.count_greater = 2

        # Act
        output = usecase.execute(input)

        # Assert
        find_text = output.items[0]
        assert find_text.value == "def"

    if True:
        input = TextFindUsecaseInput()
        input.count_lower = 2

        # Act
        output = usecase.execute(input)

        # Assert
        find_text = output.items[0]
        assert find_text.value == "abc"