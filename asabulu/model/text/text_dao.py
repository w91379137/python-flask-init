from datetime import datetime

from asabulu.domain.text.text import Text
from ..base import Base_Dao, db, ma

class Text_dao(db.Model, Base_Dao):
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

    def dao_to_bo(self) -> Text:
        return Text(
            id=self.id,
            value=self.value,
            count=self.count,
            create_time=self.create_time,
            update_time=self.update_time,
        )

class _TextSchema(ma.Schema):
    class Meta:
        fields = [
            "id",
            "value", "count",
            "create_time", "update_time",
        ]

TextSchema = _TextSchema()

