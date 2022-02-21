
from abc import ABC, abstractmethod
from typing import Optional

from .text import Text

class TextRepository(ABC):

    @abstractmethod
    def create(self, text: Text) -> Optional[Text]:
        raise NotImplementedError

    @abstractmethod
    def find_by_value(self, value: str) -> Optional[Text]:
        raise NotImplementedError

    @abstractmethod
    def update(self, text: Text) -> Optional[Text]:
        raise NotImplementedError

    @abstractmethod
    def delete_by_id(self, id: str):
        raise NotImplementedError