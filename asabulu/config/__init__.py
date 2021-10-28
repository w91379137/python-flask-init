
import os.path
import yaml # type: ignore
from flask import Flask

from asabulu.model.config.main_config import MainConfig, MainConfig_Schema
'''
https://able.bio/rhett/how-to-set-and-get-environment-variables-in-python--274rgt5
'''

import os
FlaskHost = os.getenv('FLASKHOST', "0.0.0.0")
FlaskPort = os.getenv('FLASKPORT', "5000")

class Setting():

    @staticmethod
    def config_flask_app(app: Flask, test_config = None):
        # 設定進去 Flask app
        
        from asabulu.config.default_env import init_setting
        init_setting.config_app(app, test_config)
    
    @staticmethod
    def get_config(test_config = None):
        # 自己使用的跟 flask 無關的
        # 會放到 main.config
        
        config = MainConfig()

        # 確定是否有 menu.yml
        menu_path = 'asabulu/config/custom/main_config.yml'

        try:
            if os.path.isfile(menu_path):
                with open(menu_path, encoding="utf-8") as file:
                    data = yaml.load(file, Loader = yaml.FullLoader)
                    # prettyprint(data)

                    schema = MainConfig_Schema()
                    config = schema.load(data)
                    # print(config)
            else:
                raise BaseException(f"請放設定檔(旁邊有範例): {menu_path}")

        except Exception as e:
            print(f"Error:{e}")
            raise e

        return config