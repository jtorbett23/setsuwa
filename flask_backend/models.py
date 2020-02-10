from flask_backend import db, bcrypt
from datetime import datetime

#Authorisation DB
class Login(db.Model):
    __bind_key__ = 'auth'
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)

    def __init__(self,username, plaintext_password):
        self.username = username
        self.password = bcrypt.generate_password_hash(plaintext_password)
    #add user to db    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
        # new_user = User(
        #     self.user_id, 
        #     self.username)
        # db.session.add(new_user)
        # db.session.commit()
    #get user by username
    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username = username).first()

    #password handling
    def set_password(self, plaintext_password): #for testing password hashing
        self.password = bcrypt.generate_password_hash(plaintext_password)

    def is_correct_password(self, plaintext_password):
        return bcrypt.check_password_hash(self.password, plaintext_password)

#Content DB
class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    moderator = db.Column(db.Boolean, default=False)
    private = db.Column(db.Boolean, default=False)
    posts = db.relationship('Post', backref='user', lazy=False)

    def __int__(self, user_id, username):
        self.user_id = user_id
        self.username = username
        self.moderator = False
        self.private = False


class Post(db.Model):
    post_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    title = db.Column(db.String(80), nullable=False)
    content = db.Column(db.String(500), nullable=False)
    popularity = db.Column(db.Integer, default=0)
    flagged = db.Column(db.Integer, default=False)

