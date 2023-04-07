from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import db

class Member(UserMixin, db.Model):
    __tablename__= "member"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(128), nullable=False)
    last_name = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)
    dob = db.Column(db.Date, nullable=False)
    hometown = db.Column(db.String(128), nullable=True)
    gender = db.Column(db.String(1), nullable=True)
    password = db.Column(db.String(128), nullable=False)
    
    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return f'<User {self.first_name} {self.last_name}>'