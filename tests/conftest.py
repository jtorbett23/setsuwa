import pytest
from flask_backend import create_app, db
from flask_backend.models import Login, User, Blog
from datetime import datetime 

@pytest.fixture(scope='module')
def test_client():
    flask_app = create_app('flask_test.cfg')

    #create a test version of the app using /instance/flask_test.cfg using Werkzeug test Client
    testing_client = flask_app.test_client()

    #establish app context before tests
    ctx = flask_app.app_context()
    ctx.push()

    yield testing_client  # this is where the testing happens!

    ctx.pop()

@pytest.fixture(scope='module')
def init_database():
    # Create the databases and the database tables
    db.create_all()
    db.create_all(bind=["auth"]) 

    # Insert user data
    new_user = Login("test","pass")
    new_user.save_to_db()
    new_blog = Blog(1,"Faker 123", "Donald trump nukes brazil", "party", datetime(2020, 5, 17))
    new_blog.save_to_db()

    yield db  # this is where the testing happens!
    
    #clear databases
    db.drop_all()
    db.drop_all(bind=["auth"])

