
from server import server

# ====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====
# 對內初始化

from service import main

# log 設定
from service.getlogger import getlogger
main.applog = getlogger('app')

main.applog.info('manager start')

# db 設定
from config.db_config import db_config
from service.db_manager import DBManager

main.db = DBManager(server, db_config)

result = main.db.execute('select * from text')
print(result)

# mqtt 設定
from config.mqtt_config import mqtt_config
from service.mqtt_manager import MQTTManager
# main.mqtt = MQTTManager(server, mqtt_config)


# 計時器 設定
from flask_apscheduler.scheduler import APScheduler
from apscheduler.triggers.interval import IntervalTrigger

scheduler = APScheduler()
scheduler.init_app(server)

def looptask(): 
    print("looptask !!!")

interval = IntervalTrigger(
        seconds = 10,
        start_date='2019-4-24 08:00:00',
        end_date='2099-4-24 08:00:00',
        timezone='Asia/Shanghai')

scheduler.add_job(func=looptask,trigger=interval,id='bak_one')

scheduler.start()

# ====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====
# 對外初始化

from config import FlaskHost, FlaskPort

# middleware
# https://stackoverflow.com/questions/51691730/flask-middleware-for-specific-route
from flask import request
import json
@server.before_request
def hook():
    # request - flask.request
    print(
        f"""
        [{request.method}] [{request.url}] [{request.path}]
        args: {json.dumps(request.args)}
        json: {json.dumps(request.json)}
        data: {str(request.data)}
        [{request.endpoint}] 
        """
    )

if __name__ == "__main__":
    server.run(host = FlaskHost, port = FlaskPort, debug = True)
