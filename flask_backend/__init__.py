from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt



# defined in global scope, but without any arguments passed in. 
# later will need to be attached to the application
db = SQLAlchemy()
auth_api = Api()
bcrypt = Bcrypt()
# db_api = Api()


# app factory func
def create_app(config_filename=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile(config_filename)
    
    initialise_extensions(app)
    # test app can run 
    @app.route('/')
    def test():
        return "app is running"
    return app

# helper func
def initialise_extensions(app):
    # app instance created set up extensions
    bcrypt.init_app(app)
    db.init_app(app) #set up db
    from flask_backend import auth
    # from flask_backend import database
    auth_api.init_app(app)
    # db_api.init_app(app)
    import flask_backend.models #db model
    with app.app_context():
        db.create_all()
        db.create_all(bind=["auth"]) 



