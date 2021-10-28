
from flask import Flask, request
from flask_compress import Compress # type: ignore
from flask_cors import CORS # type: ignore

from asabulu.service import main
from asabulu.config import FlaskHost, FlaskPort

def create_app(test_config = None):
    app = Flask(__name__, template_folder='../../templates', static_folder='../../static')

    flask_configuration(app)
    init_main_service(app)
    register_blueprint(app)

    Compress(app)
    CORS(app)

    return app

def flask_configuration(app: Flask):
    """
    初始化 flask 相關套件
    """
    
    pass

def init_main_service(app: Flask):
    """
    初始化 專案本身 singleton service
    """
    # log 設定
    from asabulu.service.getlogger import getlogger
    main.applog = getlogger('app')

    main.applog.info('manager start')

    # db 設定
    from asabulu.config.db_config import db_config
    from asabulu.service.db_manager import DBManager

    main.db = DBManager(app, db_config)

    # mqtt 設定
    from asabulu.config.mqtt_config import mqtt_config
    from asabulu.service.mqtt_manager import MQTTManager
    # main.mqtt = MQTTManager(server, mqtt_config)

    # 計時器 設定
    from asabulu.service.scheduler import Scheduler
    scheduler = Scheduler(app)
    main.scheduler = scheduler

    # from datetime import datetime
    # def looptask():
    #     print("looptask !!!", datetime.now())
    # trigger = scheduler.getCronTrigger(second = "*/10")
    # scheduler.addJob(
    #     func = looptask, 
    #     trigger = trigger,
    #     id = 'test',
    #     replace_existing = True)

    # main.scheduler.start()

def register_blueprint(app: Flask):

    from asabulu.server import root
    app.register_blueprint(root, url_prefix = '/')

    from asabulu.server import status
    app.register_blueprint(status, url_prefix = '/status')

    from asabulu.server import text
    app.register_blueprint(text, url_prefix = '/text')

    from asabulu.server import mqtt
    app.register_blueprint(mqtt, url_prefix = '/mqtt')
    
    # middleware
    # https://stackoverflow.com/questions/51691730/flask-middleware-for-specific-route
    import json
    @app.before_request
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
    app = create_app()
    app.run(host = FlaskHost, port = FlaskPort, debug = True)
