
from flask import Flask

def config_app(app: Flask, test_config = None):

    # ====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====
    #  flask 原生
    app.config.from_mapping(
        SECRET_KEY='dev',
    )

    # ====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====
    # 資料庫
    app.config.from_mapping(
        SQLALCHEMY_TRACK_MODIFICATIONS = False,
        SQLALCHEMY_DATABASE_URI = 'sqlite:///temp.db',
    )
    
    # ====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====
    # 快取
    app.config.from_mapping(
        SEND_FILE_MAX_AGE_DEFAULT = 3600 # 檔案快取機制
    )

    # ====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====.====
    # 文件
    app.config.from_mapping(SWAGGER = {
        "title": "API_文件",
        "description": "---",
        "version": "1.0.1",
        "termsOfService": "",
        "hide_top_bar": True,
        "openapi": '3.0.2',
    })