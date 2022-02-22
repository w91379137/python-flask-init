
from typing import List, Optional
from datetime import datetime

from asabulu.domain.text.text import Text
from asabulu.domain.text.text_repository import TextRepository

class TextRepositoryMemoryImpl(TextRepository):

    id_count = 1
    text_list: List[Text] = []

    def create(self, text: Text) -> Optional[Text]:
        dao = Text(
            id = self.id_count,
            value = text.value,
            count = 0,
            create_time = datetime.now(),
            update_time = datetime.now(),
        )
        self.id_count += 1
        self.text_list.append(dao)
        return dao

    def find_by_value(self, value: str) -> Optional[Text]:

        def condition(check_text: Text) -> bool:
            return check_text.value == value

        dao = next(filter(condition, self.text_list), None)
        if dao is None:
            return None
        return dao

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

    def delete_by_id(self, id: str):
        raise NotImplementedError