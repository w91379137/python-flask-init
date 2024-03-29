from flask_sqlalchemy import SQLAlchemy, BaseQuery # type: ignore
from flask_marshmallow import Marshmallow # type: ignore
from sqlalchemy.orm import Query

class FLBaseQuery(BaseQuery, Query):
    # 因為只寫一個都會有部分沒有定義 雖然本質上是 BaseQuery
    # 為了 filter paginate 的定義
    pass

db = SQLAlchemy()
ma = Marshmallow()

def execute_raw_sql(cmd):
    # https://www.maxlist.xyz/2019/11/09/sqlalchemy-sql/
    result = db.engine.execute(cmd)
    return result
class Base_Dao():

    # https://stackoverflow.com/questions/39099117/pycharm-sqlalchemy-autocomplete-not-working/39103583
    query: FLBaseQuery # Type hint here

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