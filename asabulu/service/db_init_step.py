
from flask import Flask

from asabulu.model.base import db
from asabulu.model.config.property.db_setting import DB_setting

def on_app(app: Flask, db_config: DB_setting):

    app.config['SQLALCHEMY_DATABASE_URI'] = db_config.path

    db.init_app(app)

    with app.app_context():
        db.create_all()
        # 這邊可以做其他初始化動作
        
    return db