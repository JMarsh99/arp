from app.launch import db
from flask_login import UserMixin


class User(db.Model, UserMixin):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(500))

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

