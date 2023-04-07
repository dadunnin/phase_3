from datetime import datetime
from app import db

class Album(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    owner_id = db.Column(db.Integer, db.ForeignKey('member.id', ondelete='CASCADE', onupdate='CASCADE'))
    created = db.Column(db.Date, default=datetime.utcnow)

    def __repr__(self):
        return f'<Album {self.name}>'
