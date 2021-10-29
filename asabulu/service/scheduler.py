
# 計時器 設定
from flask_apscheduler.scheduler import APScheduler # type: ignore
from apscheduler.triggers.cron import CronTrigger # type: ignore

# https://stackoverflow.com/questions/14874782/apscheduler-in-flask-executes-twice
# 防止 flask 重整就多出一次 需要使用 flask run

class Scheduler:

    scheduler: None

    def __init__(self, server):
        self.scheduler = APScheduler()
        self.scheduler.init_app(server)

    def start(self):
        self.scheduler.start()

    # ====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====

    def getCronTrigger(self, *args, **kwargs):
        # 參數 second = "*/10"
        # https://stackoverflow.com/questions/3136915/passing-all-arguments-of-a-function-to-another-function
        trigger = CronTrigger(**kwargs)   
        return trigger

    def addJob(self, *args, **kwargs):
        self.scheduler.add_job(**kwargs)
        # scheduler.addJob(
        #     func = func, 
        #     trigger = trigger,
        #     id = 'my_trigger',
        #     replace_existing = True)
        