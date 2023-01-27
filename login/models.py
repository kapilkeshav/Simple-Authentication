from app import db
from flask_login import UserMixin

class User(UserMixin,db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username  = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    pwd = db.Column(db.String(80),unique=True)

    def __repr__(self) -> str:
        return '<User %r>'%self.username
