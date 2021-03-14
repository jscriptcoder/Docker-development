from .db import db


class ProcessModel(db.Model):
    __tablename__ = 'process'

    id = db.Column(db.String(32), primary_key=True)

    def to_dict(self):
        return { 'id': self.id }

    def __repr__(self):
        return f'<Process {self.id}>'
