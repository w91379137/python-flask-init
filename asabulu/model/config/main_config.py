
from typing import Dict
from marshmallow import Schema, fields, INCLUDE, post_load
from asabulu.model.config.property.db_setting import DB_setting, DB_setting_schema
from asabulu.model.config.property.server_setting import Server_setting, Server_setting_schema

class MainConfig_Schema(Schema):
    
    class Meta:
        unknown = INCLUDE

    server = fields.Nested(Server_setting_schema(), required = True)
    db = fields.Nested(DB_setting_schema(), required = True)

    @post_load
    def post_load(self, data, **kwargs):
        return MainConfig(data)

class MainConfig():

    server: Server_setting = Server_setting()
    db: DB_setting = DB_setting()
    mqtt: None
    
    def __init__(self, obj: Dict = {}):
        self.server = obj.get('server', self.server)
