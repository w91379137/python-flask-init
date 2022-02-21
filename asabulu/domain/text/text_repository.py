
from abc import ABC, abstractmethod
from typing import Optional

from .text import Text

class BookRepository(ABC):
    """BookRepository defines a repository interface for Book entity."""

    @abstractmethod
    def create(self, text: Text) -> Optional[Text]:
        raise NotImplementedError

    @abstractmethod
    def find_by_id(self, id: str) -> Optional[Text]:
        raise NotImplementedError

    @abstractmethod
    def update(self, text: Text) -> Optional[Text]:
        raise NotImplementedError

    @abstractmethod
    def delete_by_id(self, id: str):
        raise NotImplementedError