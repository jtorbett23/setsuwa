import pytest
from flask_backend import create_app, db
# from flask_backend.models import Login, User, Post


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

# @pytest.fixture(scope='module')
# def init_database():
#     # Create the database and the database table
#     db.create_all()
#     db.create_all(bind=["auth"])

#     #Create and Insert user data
    
#     # Commit the changes for the users
#     # db.session.commit()

#     yield db  # this is where the testing happens!

#     db.drop_all()

