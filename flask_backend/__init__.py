#imports
from flask import Flask, render_template
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_jwt_extended import JWTManager

#defined in global access and configured when app is created
db = SQLAlchemy()
auth_api = Api()
bcrypt = Bcrypt()
db_api = Api()

# app factory function
def create_app(config_filename=None):
    #create app and link to react build folder
    app = Flask(
        __name__, 
        instance_relative_config=True, 
        static_folder='../react_frontend/build/static', 
        template_folder='../react_frontend/build')
    
    #configure app with /instance/*.cfg files
    app.config.from_pyfile(config_filename)
    
    #initialise addition extensions
    initialise_extensions(app)

    #all routes direct to react application index.html  
    @app.route('/', defaults={'path': ''})
    @app.route('/<path:path>')
    def react(path):
        return render_template('index.html')
    
    return app

# helper function
def initialise_extensions(app):
# initialise extensions with created app
    
    #import and configure api routes
    from flask_backend import auth
    from flask_backend import database
    auth_api.init_app(app)
    db_api.init_app(app)

    #configure CORS for development
    CORS(app, resources={
        r'/auth/*': {'origins': '*'},
        r'/db/*':{'origins:': '*'}})

    #configure JWTs
    jwt = JWTManager(app)

    #handle blacklisting of JWTs
    @jwt.token_in_blacklist_loader
    def check_if_token_in_blacklist(decrypted_token):
        jti = decrypted_token['jti']
        return models.Revoked_Token.is_jti_blacklisted(jti)
    
    #configure password hashing
    bcrypt.init_app(app)
    #import models and configure databse
    import flask_backend.models
    db.init_app(app) 
    
    #migrate or seed db
    from flask_backend.seed import seed_db
    with app.app_context():
        #seed - should only be run for development
        # seed_db()
        #migrate
        db.create_all()
        db.create_all(bind=['auth']) 