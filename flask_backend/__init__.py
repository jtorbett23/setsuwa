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
        db.create_all()
        db.create_all(bind=["auth"]) 



