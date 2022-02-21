

from typing import Optional
from datetime import datetime

class Text:
    """ 記載字串輸入次數 """

    def __init__(
        self,
        id: Optional[int] = None,
        value: str = "",
        count: int = 0,
        create_time: Optional[datetime] = None,
        update_time: Optional[datetime] = None,
    ):
        self.id: Optional[int] = id
        self.value: str = value
        self.count: int = count
        self.create_time: Optional[datetime] = create_time
        self.update_time: Optional[datetime] = update_time
