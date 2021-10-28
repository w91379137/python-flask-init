
from typing import Dict
from marshmallow import Schema, fields, INCLUDE, post_load
from asabulu.model.config.property.server import Server, Server_Schema

class MainConfig_Schema(Schema):
    
    class Meta:
        unknown = INCLUDE

    server = fields.Nested(Server_Schema(), required = True)

    @post_load
    def post_load(self, data, **kwargs):
        return MainConfig(data)

class MainConfig():

    server: Server = Server()
    
    def __init__(self, obj: Dict = {}):
        self.server = obj.get('server', self.server)
