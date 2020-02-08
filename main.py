from flask_backend import create_app

# call app factory func to create app instance 
# using the standard config defined in instance/flask-config 

app = create_app('flask.cfg')

