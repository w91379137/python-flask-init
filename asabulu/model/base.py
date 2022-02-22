from flask_sqlalchemy import SQLAlchemy # type: ignore
from flask_marshmallow import Marshmallow # type: ignore
from sqlalchemy.orm import Query

db = SQLAlchemy()
ma = Marshmallow()

def execute_raw_sql(cmd):
    # https://www.maxlist.xyz/2019/11/09/sqlalchemy-sql/
    result = db.engine.execute(cmd)
    return result
class Base_Dao():

    # https://stackoverflow.com/questions/39099117/pycharm-sqlalchemy-autocomplete-not-working/39103583
    query: Query # Type hint here

    def save_to_db(self):
        db.session.add(self)
        self.try_commit()

    def update(self):
        self.try_commit()

    def delete(self):
        db.session.delete(self)
        self.try_commit()

    def try_commit(self):
        try:
            db.session.commit()
        except Exception as e:
            print(f"db_error >> {e}")
            db.session.rollback()