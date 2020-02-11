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
        new_user = User(
            user_id = self.user_id, 
            username = self.username)
        new_user.save_to_db()
    #get user by username
    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username = username).first()

    #password handling
    def set_password(self, plaintext_password): #for testing password hashing
        self.password = bcrypt.generate_password_hash(plaintext_password)

    def is_correct_password(self, plaintext_password):
        return bcrypt.check_password_hash(self.password, plaintext_password)


class Revoked_Token(db.Model):
    __tablename__ = 'revoked_tokens'
    id = db.Column(db.Integer, primary_key = True)
    jti = db.Column(db.String(120))
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    
    @classmethod
    def is_jti_blacklisted(cls, jti):
        query = cls.query.filter_by(jti = jti).first()
        return bool(query)


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
    
    #get user by id
    @classmethod
    def find_by_id(cls, user_id):
        return cls.query.filter_by(user_id = user_id).first()

    def to_object(self):
        return {
            "user_id": self.user_id,
            "username": self.username,
            "moderator": self.moderator,
            "private": self.private,
        }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    
class Post(db.Model):
    post_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    title = db.Column(db.String(80), nullable=False)
    content = db.Column(db.String(500), nullable=False)
    popularity = db.Column(db.Integer, default=0)
    tag = db.Column(db.String, nullable=False)
    created = db.Column(db.DateTime, default=datetime.utcnow)
    flagged = db.Column(db.Integer, default=False)

    def __init__(self, user_id, title, content, tag):
        self.user_id = user_id
        self.title = title
        self.content = content
        self.tag = tag
        self.created = datetime.utcnow
        self.popularity = 0
        self.flagged = False
        
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    
    #get post by id
    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(post_id = id).first()

    #get 10 post by popularity
    @classmethod
    def find_popular(cls):
        return cls.query.limit(10).all().order_by(cls.popularity.amount.desc())

    #get posts by tag in order of popularity
    @classmethod
    def find_popular(cls, tag_name):
        return cls.query.filter_by(tag = tag_name).all().order_by(cls.popularity.amount.desc())
    
    # #get 10 newest posts
    # @classmethod
    # def find_new(cls):
    #     return cls.query.limit(10).all()
    
    # #get 10 oldest posts
    # @classmethod
    # def find_old(cls):
    #     return cls.query.limit(10).all()

    


