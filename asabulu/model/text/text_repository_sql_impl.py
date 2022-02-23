
from typing import Optional
from asabulu.domain.text.text import Text
from asabulu.domain.text.text_repository import TextRepository

from .text_dao import Text_dao

class TextRepositorySQLImpl(TextRepository):

    def create(self, text: Text) -> Optional[Text]:
        dao = Text_dao(value = text.value)
        dao.save_to_db()
        return dao.dao_to_bo()

    def find_by_id(self, id: int) -> Optional[Text]:
        dao = Text_dao.query.get(id)
        if dao is None:
            return None
        return dao.dao_to_bo()

    def find_by_value(self, value: str) -> Optional[Text]:
        dao: Optional[Text_dao] = Text_dao.query.filter_by(value = value).first()
        if dao is None:
            return None
        return dao.dao_to_bo()

    def update(self, text: Text) -> Optional[Text]:
        dao: Optional[Text_dao] = Text_dao.query.get(text.id)
        if dao is None:
            return None

        dao.value = text.value
        dao.count = text.count
        dao.update()
        return dao.dao_to_bo()

    def delete_by_id(self, id: int):

        dao: Optional[Text_dao] = Text_dao.query.get(id)
        if dao is not None:
            dao.delete()
        