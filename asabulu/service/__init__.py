
from logging import Logger
from typing import Any

from asabulu.usecase.text.text_create_usecase import TextCreateUsecase
from asabulu.usecase.text.text_delete_usecase import TextDeleteUsecase
from asabulu.usecase.text.text_find_usecase import TextFindUsecase
from asabulu.usecase.text.text_read_usecase import TextReadUsecase
from asabulu.usecase.text.text_update_usecase import TextUpdateUsecase
from .singleton import singleton
from asabulu.model.config.main_config import MainConfig
@singleton
class _MainService():

    config: MainConfig
    db: Any
    applog: Logger
    mqtt: Any
    scheduler: Any

    textCreateUsecase: TextCreateUsecase
    textUpdateUsecase: TextUpdateUsecase
    textReadUsecase: TextReadUsecase
    textDeleteUsecase: TextDeleteUsecase
    textFindUsecase: TextFindUsecase

    def __init__(self): 
        pass

# 這邊的 main 做為 singleton 其實不用 寫 @singleton 也沒差
main = _MainService()