
from flask_sqlalchemy import SQLAlchemy

import warnings

# https://github.com/marshmallow-code/flask-marshmallow/issues/53
with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    from flask_marshmallow import Marshmallow

from model.text import getTableClass as getTableText, getSchemaClass as getTextSchema

# @singleton
# 這邊不做 singleton 改由 service 那邊統一實作 因為測試的時候 就不會重複生成
class DBManager:

    db: None
    ma: None

    Text: None
    TextSchema: None

    def __init__(self, server, db_config):

        server.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = db_config['SQLALCHEMY_TRACK_MODIFICATIONS']
        server.config['SQLALCHEMY_DATABASE_URI'] = db_config['SQLALCHEMY_DATABASE_URI']

        self.db = SQLAlchemy(server)
        self.ma = Marshmallow(server)
        
        self.Text = getTableText(self.db)
        self.TextSchema = getTextSchema(self.ma)() # 直接創建物件

        self.db.create_all()
        
    def execute(self, cmd):
        # https://www.maxlist.xyz/2019/11/09/sqlalchemy-sql/
        result = self.db.engine.execute(cmd).fetchall()
        return result