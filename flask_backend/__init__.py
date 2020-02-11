from flask import Flask, render_template
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_jwt_extended import JWTManager


# defined in global scope, but without any arguments passed in. 
# later will need to be attached to the application
db = SQLAlchemy()
auth_api = Api()
bcrypt = Bcrypt()
db_api = Api()


# app factory func
def create_app(config_filename=None):
    app = Flask(__name__, instance_relative_config=True, static_folder='../react_frontend/build/static', template_folder='../react_frontend/build')
    app.config.from_pyfile(config_filename)
    
    initialise_extensions(app)
    # test app can run 
    @app.route('/running')
    def test():
        return "app is running"
        
    @app.route('/')
    def react():
        return render_template('index.html')
    return app

# helper func
def initialise_extensions(app):
# app instance created set up extensions
    bcrypt.init_app(app)
    db.init_app(app) #set up db
    import flask_backend.models #db model
    CORS(app, resources={
        r"/auth/*": {"origins": "*"},
        r"/db/*":{"origins:": "*"}})
    from flask_backend import auth
    from flask_backend import database
    auth_api.init_app(app)
    db_api.init_app(app)
    jwt = JWTManager(app)
    @jwt.token_in_blacklist_loader
    def check_if_token_in_blacklist(decrypted_token):
        jti = decrypted_token['jti']
        return models.Revoked_Token.is_jti_blacklisted(jti)
        
    with app.app_context():
        # seed_db()
        db.create_all()
        db.create_all(bind=["auth"]) 

def seed_db():
    db.drop_all()
    db.drop_all(bind=["auth"])
    db.create_all()
    db.create_all(bind=["auth"]) 
    import flask_backend.models 
    user = models.Login("user","pass")
    user.save_to_db()
    from datetime import datetime 
    posts = [
        {"title": "1", "content": "a", "tag":"sport", "created": datetime(2009,5,17)},
        {"title": "2", "content": "b", "tag":"sport", "created": datetime(2010, 5, 17)},
        {"title": "3", "content": "c", "tag":"sport", "created": datetime(2021, 5, 17)},
        {"title": "4", "content": "d", "tag":"movies", "created": datetime(2012, 5, 17)},
        {"title": "5", "content": "e", "tag":"movies", "created": datetime(2013, 5, 17)},
        {"title": "6", "content": "f", "tag":"food", "created": datetime(2014, 5, 17)},
        {"title": "7", "content": "g", "tag":"food", "created": datetime(2015, 5, 17)},
        {"title": "8", "content": "h", "tag":"food", "created": datetime(2016, 5, 17)},
        {"title": "9", "content": "i", "tag":"food", "created": datetime(2017, 5, 17)},
        {"title": "10", "content": "j", "tag":"travel", "created": datetime(2018, 5, 17)},
        {"title": "11", "content": "k", "tag":"games", "created": datetime(2019, 5, 17)},
        {"title": "12", "content": "l", "tag":"technology", "created": datetime(2020, 5, 17)},
        ]
    for post in posts:
        new_post = models.Blog(user.user_id,post['title'],post['content'], post['tag'], post['created'])
        new_post.save_to_db()


