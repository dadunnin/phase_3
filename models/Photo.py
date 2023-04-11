from app import db

class Photo(db.Model):
    photo_id = db.Column(db.Integer, primary_key=True)
    album_id = db.Column(db.Integer, db.ForeignKey('album.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    caption = db.Column(db.Text, nullable=True)
    img = db.Column(db.String(128), nullable=True)

    def __repr__(self):
        return f'<Photo {self.photo_id}>'
