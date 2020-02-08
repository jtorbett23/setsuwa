import pytest
from flask_backend import create_app

#scope of this module tests
@pytest.fixture(scope='module')
def test_client():
    #create a test version of the app using /instance/flask_test.cfg
    flask_app = create_app('flask_test.cfg')

    test_client = flask_app.test_client()

    #establish app context before tests

    app_in_context = flask_app.app_context()
    app_in_context.push()

    yield test_client # testing begins here

    app_in_context.pop()