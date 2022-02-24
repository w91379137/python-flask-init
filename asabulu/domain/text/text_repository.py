
from abc import ABC, abstractmethod
from typing import List, Optional

from .text import Text

class TextFindInput():
    page: int = 1
    size: int = 10
    value_eql: Optional[str] = None
    value_like: Optional[str] = None
    count_eql: Optional[int] = None
    count_greater: Optional[int] = None
    count_lower: Optional[int] = None

class TextFindOutput():
    items: List[Text] = []
    total: int = 0
class TextRepository(ABC):

    @abstractmethod
    def create(self, text: Text) -> Optional[Text]:
        raise NotImplementedError

    @abstractmethod
    def find_by_id(self, id: int) -> Optional[Text]:
        raise NotImplementedError

    @abstractmethod
    def find_by_value(self, value: str) -> Optional[Text]:
        raise NotImplementedError

    @abstractmethod
    def find(self, input: TextFindInput) -> TextFindOutput:
        raise NotImplementedError

    @abstractmethod
    def update(self, text: Text) -> Optional[Text]:
        raise NotImplementedError

    @abstractmethod
    def delete_by_id(self, id: int):
        raise NotImplementedError