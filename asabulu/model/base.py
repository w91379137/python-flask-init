from flask_sqlalchemy import SQLAlchemy # type: ignore
from flask_marshmallow import Marshmallow # type: ignore

db = SQLAlchemy()
ma = Marshmallow()

def execute_raw_sql(cmd):
    # https://www.maxlist.xyz/2019/11/09/sqlalchemy-sql/
    result = db.engine.execute(cmd).fetchall()
    return result