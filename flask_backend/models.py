from flask_backend import db, bcrypt
from datetime import datetime

#Authorisation DB
class Login(db.Model):
    __bind_key__ = 'auth'
    user_id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(80), unique = True, nullable = False)
    password = db.Column(db.String(80), nullable = False)
    moderator = db.Column(db.Boolean, default = False)

    def __init__(self,username, plaintext_password, moderator = False):
        self.username = username
        self.password = bcrypt.generate_password_hash(plaintext_password)
        self.moderator = moderator
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
    __bind_key__ = 'auth'
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
    private = db.Column(db.Boolean, default=False)
    posts = db.relationship('Blog', backref='user', lazy=False)

    def __int__(self, user_id, username):
        self.user_id = user_id
        self.username = username
        self.private = False
    
    #get user by id
    @classmethod
    def find_by_id(cls, user_id):
        return cls.query.filter_by(user_id = user_id).first()

    def to_object(self):
        return {
            "user_id": self.user_id,
            "username": self.username,
            "private": self.private,
        }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    
class Blog(db.Model):
    post_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    title = db.Column(db.String(80), nullable=False)
    content = db.Column(db.String(500), nullable=False)
    popularity = db.Column(db.Integer, default=0)
    tag = db.Column(db.String, nullable=False)
    created = db.Column(db.DateTime, default=datetime.today())
    flagged = db.Column(db.Integer, default=False)

    def __init__(self, user_id, title, content, tag, created=datetime.today(), popularity=0):
        self.user_id = user_id
        self.title = title
        self.content = content
        self.tag = tag
        self.created = created
        self.popularity = popularity
        self.flagged = False

    def to_object(self):
        return {
            "post_id": self.post_id,
            "user_id": self.user_id,
            "title": self.title,
            "content": self.content,
            "popularity": self.popularity,
            "tag": self.tag,
            "created": self.created,
            "flagged": self.flagged,
        }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    #update by id
    @classmethod
    def edit_by_id(cls, id, title, content, tag):
        edit_blog =cls.find_by_id(id)
        edit_blog.title = title
        edit_blog.content = content
        edit_blog.tag= tag
        edit_blog.save_to_db()
    #get post by id
    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(post_id = id).first()
    
    #delete post by id
    @classmethod
    def delete_by_id(cls,id):
        cls.query.filter_by(post_id=id).delete() 
        db.session.commit()

    #get all posts by filter
    @classmethod
    def find_posts(cls, filter="pop"):
        if(filter == "pop"):
            return cls.query.order_by(cls.popularity.desc()).limit(10).all()
        elif(filter == "unpop"):
            return cls.query.order_by(cls.popularity.asc()).limit(10).all()
        elif(filter == "new"):
            return cls.query.order_by(cls.created.desc()).limit(10).all()
        elif(filter == "old"):
            return cls.query.order_by(cls.created.asc()).limit(10).all()
    
    @classmethod
    def find_user_posts(cls,user_id, filter="new"):
        if(filter == "pop"):
            return cls.query.filter(cls.user_id == user_id).order_by(cls.popularity.desc()).all()
        elif(filter == "unpop"):
            return cls.query.filter(cls.user_id == user_id).order_by(cls.popularity.asc()).all()
        elif(filter == "new"):
            return cls.query.filter(cls.user_id == user_id).order_by(cls.created.desc()).all()
        elif(filter == "old"):
            return cls.query.filter(cls.user_id == user_id).order_by(cls.created.asc()).all()

    #get all posts for a tag
    @classmethod
    def find_tag_posts(cls, tag, filter="pop"):
        if(filter == "pop"):
            return cls.query.filter(cls.tag == tag).order_by(cls.popularity.desc()).limit(10).all()
        elif(filter == "unpop"):
            return cls.query.filter(cls.tag == tag).order_by(cls.popularity.asc()).limit(10).all()
        elif(filter == "new"):
            return cls.query.filter(cls.tag == tag).order_by(cls.created.desc()).limit(10).all()
        elif(filter == "old"):
            return cls.query.filter(cls.tag == tag).order_by(cls.created.asc()).limit(10).all()


