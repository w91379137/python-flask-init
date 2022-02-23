
from flask import Flask, request
from flask_compress import Compress # type: ignore
from flask_cors import CORS # type: ignore
from asabulu.model.config.main_config import MainConfig

from asabulu.service import main, db_init_step
from asabulu.config import Setting

def create_app(test_config = None):
    app = Flask(__name__, template_folder='../../templates', static_folder='../../static')

    Setting.config_flask_app(app, test_config)
    main.config = Setting.get_config(test_config)

    flask_configuration(app, main.config)
    init_main_service(app, main.config)
    register_blueprint(app, main.config)

    Compress(app)
    CORS(app)

    return app

def flask_configuration(app: Flask, config: MainConfig):
    """
    初始化 flask 相關套件
    """
    
    pass

def init_main_service(app: Flask, config: MainConfig):
    """
    初始化 專案本身 singleton service
    """
    # log 設定
    from asabulu.service.getlogger import getlogger
    main.applog = getlogger('app')

    main.applog.info('manager start')

    # db 設定
    import asabulu.model # 提前 import 所有 model
    main.db = db_init_step.on_app(app, config.db)

    # mqtt 設定
    # from asabulu.config.mqtt_config import mqtt_config
    # from asabulu.service.mqtt_manager import MQTTManager
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

    # usecase 設定
    from asabulu.model.text.text_repository_sql_impl import TextRepositorySQLImpl
    injection: object

    if True:
        from asabulu.usecase.text.text_create_usecase import TextCreateUsecase, TextCreateUsecaseInjection

        injection = TextCreateUsecaseInjection()
        injection.textRepository = TextRepositorySQLImpl()

        main.textCreateUsecase = TextCreateUsecase(injection)

    if True:
        from asabulu.usecase.text.text_update_usecase import TextUpdateUsecase, TextUpdateUsecaseInjection

        injection = TextUpdateUsecaseInjection()
        injection.textRepository = TextRepositorySQLImpl()

        main.textUpdateUsecase = TextUpdateUsecase(injection)


    if True:
        from asabulu.usecase.text.text_read_usecase import TextReadUsecase, TextReadUsecaseInjection

        injection = TextReadUsecaseInjection()
        injection.textRepository = TextRepositorySQLImpl()

        main.textReadUsecase = TextReadUsecase(injection)


def register_blueprint(app: Flask, config: MainConfig):

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
    config = main.config.server
    app.run(host = config.host, port = config.port, debug = True)
