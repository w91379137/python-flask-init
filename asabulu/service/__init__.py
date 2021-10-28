
from logging import Logger
from typing import Any
from .singleton import singleton
from asabulu.model.config.main_config import MainConfig
@singleton
class _MainService():

    config: MainConfig
    db: Any
    applog: Logger
    mqtt: Any
    scheduler: Any

    def __init__(self): 
        pass

# 這邊的 main 做為 singleton 其實不用 寫 @singleton 也沒差
main = _MainService()