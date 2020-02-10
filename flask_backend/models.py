from flask_backend import db
from datetime import datetime

#Authorisation DB
class Login(db.Model):
    __bind_key__ = 'auth'
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=True, nullable=False)

#Content DB
class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    moderator = db.Column(db.Boolean, default=False)
    private = db.Column(db.Boolean, default=False)
    posts = db.relationship('Post', backref='user', lazy=False)

class Post(db.Model):
    post_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    title = db.Column(db.String(80), nullable=False)
    content = db.Column(db.String(500), nullable=False)
    popularity = db.Column(db.Integer, default=0)
    flagged = db.Column(db.Integer, default=False)

