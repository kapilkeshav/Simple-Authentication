from app import db
from flask_login import UserMixin

class User(UserMixin,db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username  = db.Column(db.String(80),nullable=False, unique=True)
    email = db.Column(db.String(120),nullabale=False, unique=True )
    pwd = db.Column(db.String(80),nullable=False)

    def __repr__(self) -> str:
        return '<User %r>'%self.username
