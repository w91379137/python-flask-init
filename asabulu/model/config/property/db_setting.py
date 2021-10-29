
from typing import Dict
from marshmallow import Schema, fields, INCLUDE, post_load

class DB_setting_schema(Schema):

    class Meta:
        unknown = INCLUDE

    path = fields.String()

    @post_load
    def post_load(self, data, **kwargs):
        return DB_setting(data)

class DB_setting():

    path = "sqlite:///temp.db"

    def __init__(self, obj: Dict = {}):
        self.path = obj.get('path', self.path)