
# 持久的輸入輸出管道
from typing import Optional
from asabulu.domain.text.text import Text
from asabulu.domain.text.text_repository import TextRepository

class TextCreateUsecaseInjection():

    textRepository: TextRepository
    # timeProvider
    # logger
    # eventBus

# 一次性輸入
class TextCreateUsecaseInput():
    value: str

# 一次性輸出
class TextCreateUsecaseOuput():
    text: Optional[Text] = None

# 意外輸出
class TextCreateUsecaseException():
    pass

class TextCreateUsecase():

    def __init__(self, injection: TextCreateUsecaseInjection) -> None:
        self.textRepository = injection.textRepository
        
    def execute(self, input: TextCreateUsecaseInput) -> TextCreateUsecaseOuput:

        value = input.value
        if type(value) is not str:
            value = '何もありません' # 日文字存檔測試

        text = self.textRepository.find_by_value(value)
        if text is not None:
            text.count += 1
            self.textRepository.update(text)
        else:
            text = Text(value = value)
            text = self.textRepository.create(text)

        output = TextCreateUsecaseOuput()
        output.text = text
        
        return output