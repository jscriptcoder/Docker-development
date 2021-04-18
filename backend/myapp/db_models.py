from datetime import datetime
from .db import db


class ProcessModel(db.Model):
    __tablename__ = 'process'

    id = db.Column(db.String(32), primary_key=True)
    started_on = db.Column(db.DateTime, default=datetime.utcnow)
    ended_on = db.Column(db.DateTime)
    result = db.Column(db.String(32))

    def update(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)

    def to_dict(self):
        return {'id': self.id, 'result': self.result}

    def __repr__(self):
        return f'<Process {self.id}>'
