
from datetime import datetime

# 命名規則
# https://www.itread01.com/p/1397452.html

def getTableClass(db):

    # 模型( model )定義
    class Text(db.Model):
        __tablename__ = 'text'
        id = db.Column(db.Integer, primary_key=True)
        value = db.Column(db.String(30))
        count = db.Column(db.Integer, default=0)

        insert_time = db.Column(db.DateTime, default=datetime.now)
        update_time = db.Column(db.DateTime, onupdate=datetime.now, default=datetime.now)

        def __init__(self, value):
            self.value = value

        def save_to_db(self):
            db.session.add(self)
            db.session.commit()

        def update(self):
            db.session.commit()

        def delete(self):
            db.session.delete(self)
            db.session.commit()

    return Text

def getSchemaClass(ma):

    class TextSchema(ma.Schema):
        class Meta:
            fields = ("id", "value", "count", "insert_time", "update_time")

    return TextSchema