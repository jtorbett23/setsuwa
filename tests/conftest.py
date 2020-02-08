import pytest
from flask_backend import create_app




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

