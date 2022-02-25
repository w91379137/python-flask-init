
from typing import List, Optional
from datetime import datetime

from asabulu.domain.text.text import Text
from asabulu.domain.text.text_repository import TextFindInput, TextFindOutput, TextRepository

class TextRepositoryMemoryImpl(TextRepository):

    def __init__(self) -> None:
        super().__init__()
        self.id_count: int = 1
        self.text_list: List[Text] = []

    def create(self, text: Text) -> Optional[Text]:
        dao = Text(
            id = self.id_count,
            value = text.value,
            count = text.count,
            create_time = datetime.now(),
            update_time = datetime.now(),
        )
        self.id_count += 1
        self.text_list.append(dao)
        return dao
    
    def find_by_id(self, id: int) -> Optional[Text]:

        def condition(check_text: Text) -> bool:
            return check_text.id == id

        aIter = filter(condition, self.text_list)
        return next(aIter, None)

    def find_by_value(self, value: str) -> Optional[Text]:

        def condition(check_text: Text) -> bool:
            return check_text.value == value

        aIter = filter(condition, self.text_list)
        return next(aIter, None)

    def find(self, input: TextFindInput) -> TextFindOutput:
        
        aIter = iter(self.text_list)

        if input.value_eql is not None:
            value_eql: str = input.value_eql

            def condition(check_text: Text) -> bool:
                return check_text.value == value_eql

            aIter = filter(condition, aIter)

        if input.value_like is not None:
            value_like: str = input.value_like

            def condition(check_text: Text) -> bool:
                return value_like in check_text.value

            aIter = filter(condition, aIter)
   
        if input.count_eql is not None:
            count_eql: int = input.count_eql

            def condition(check_text: Text) -> bool:
                return check_text.count == count_eql

            aIter = filter(condition, aIter)

        if input.count_greater is not None:
            count_greater: int = input.count_greater

            def condition(check_text: Text) -> bool:
                return check_text.count > count_greater

            aIter = filter(condition, aIter)

        if input.count_lower is not None:
            count_lower: int = input.count_lower

            def condition(check_text: Text) -> bool:
                return check_text.count < count_lower

            aIter = filter(condition, aIter)

        textList = list(aIter)

        page = input.page
        size = input.size
        startIndex = (page - 1) * size
        endIndex = page * size
        
        items = textList[startIndex:endIndex]

        output = TextFindOutput()
        output.items = items
        output.total = len(textList)
        return output


    def update(self, text: Text) -> Optional[Text]:

        def condition(check_text: Text) -> bool:
            return check_text.id == text.id

        dao = next(filter(condition, self.text_list), None)
        if dao is None:
            return None

        dao.value = text.value
        dao.count = text.count
        dao.update_time = datetime.now()
        return dao

    def delete_by_id(self, id: int):

        def condition(check_text: Text) -> bool:
            return check_text.id != id
        
        self.text_list = list(filter(condition, self.text_list))