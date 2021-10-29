from datetime import datetime
from ...model.base import db, ma

class Text(db.Model):
    __tablename__ = 'text'
    
    id = db.Column(db.Integer, primary_key = True)
    """ 流水號 """
    
    value = db.Column(db.String(3000))
    """ 文字訊息 """

    count = db.Column(db.Integer, default = 0)
    """ 儲存次數 """
    
    create_time = db.Column(db.DateTime, default = datetime.now)
    """ 建立時間 """

    update_time = db.Column(db.DateTime, onupdate = datetime.now, default = datetime.now)
    """ 更新時間 """

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
        except:
            db.session.rollback()

class _TextSchema(ma.Schema):
    class Meta:
        fields = [
            "id",
            "value", "count",
            "create_time", "update_time",
        ]

TextSchema = _TextSchema()
