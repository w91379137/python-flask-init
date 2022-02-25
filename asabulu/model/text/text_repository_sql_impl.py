
from typing import Optional
from flask_sqlalchemy import Pagination  # type: ignore

from asabulu.domain.text.text import Text
from asabulu.domain.text.text_repository import TextFindInput, TextFindOutput, TextRepository

from .text_dao import Text_dao
class TextRepositorySQLImpl(TextRepository):

    def create(self, text: Text) -> Optional[Text]:
        dao = Text_dao(value = text.value, count = text.count)
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

    def find(self, input: TextFindInput) -> TextFindOutput:

        result = Text_dao.query
        
        if input.value_eql is not None:
            value_eql: str = input.value_eql
            result = result.filter(Text_dao.value == value_eql)

        if input.value_like is not None:
            value_like: str = input.value_like
            result = result.filter(Text_dao.value.like(f'%{value_like}%'))

        if input.count_eql is not None:
            count_eql: int = input.count_eql
            # result = result.filter_by(count = count_eql)
            result = result.filter(Text_dao.count == count_eql)

        if input.count_greater is not None:
            count_greater: int = input.count_greater
            result = result.filter(Text_dao.count > count_greater)

        if input.count_lower is not None:
            count_lower: int = input.count_lower
            result = result.filter(Text_dao.count < count_lower)

        result = result.order_by(
            Text_dao.id.desc()
        )

        page = input.page
        size = input.size
        aPagination: Pagination = result.paginate(page, per_page = size)

        output = TextFindOutput()
        output.items = aPagination.items
        output.total = aPagination.total
        return output

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
        