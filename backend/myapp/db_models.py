from .db import db


class ProcessModel(db.Model):
    __tablename__ = 'process'

    id = db.Column(db.String(32), primary_key=True)
    done = db.Column(db.Boolean, default=False)

    def to_dict(self):
        return { 'id': self.id, 'done': self.done }

    def __repr__(self):
        return f'<Process {self.id}>'
