

from .singleton import singleton

@singleton
class _MainService():

    db: None
    applog: None
    mqtt: None
    scheduler: None

    def __init__(self): 
        pass

# 這邊的 main 做為 singleton 其實不用 寫 @singleton 也沒差
main = _MainService()