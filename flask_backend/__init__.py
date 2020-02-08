from flask import Flask

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
    print("loading extensions")
    # app instance created set up extensions 



