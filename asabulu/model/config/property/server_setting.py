
from typing import Dict
from marshmallow import Schema, fields, INCLUDE, post_load

class Server_setting_schema(Schema):

    class Meta:
        unknown = INCLUDE

    range_api_host = fields.String(default = "0.0.0.0")
    invoice_api_host = fields.Integer(default = 5000)

    @post_load
    def post_load(self, data, **kwargs):
        return Server_setting(data)

class Server_setting():

    host = "0.0.0.0"
    port = 5000

    def __init__(self, obj: Dict = {}):
        self.host = obj.get('host', self.host)
        self.port = obj.get('port', self.port)