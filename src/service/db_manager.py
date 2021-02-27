
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

from model.text import getTableClass as getTableText, getSchemaClass as getTextSchema

# @singleton
# 這邊不做 singleton 改由 service 那邊統一實作 因為測試的時候 就不會重複生成
class DBManager:

    Text: None
    TextSchema: None

    def __init__(self, server, db_config):

        server.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = db_config['SQLALCHEMY_TRACK_MODIFICATIONS']
        server.config['SQLALCHEMY_DATABASE_URI'] = db_config['SQLALCHEMY_DATABASE_URI']

        db = SQLAlchemy(server)
        ma = Marshmallow(server)
        
        self.Text = getTableText(db)
        self.TextSchema = getTextSchema(ma)() # 直接創建物件

        db.create_all()
        