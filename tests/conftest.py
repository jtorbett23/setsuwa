import pytest
from flask import g
from flask_backend import create_app, db
from flask_backend.models import Login,User, Blog, Revoked_Token
from datetime import datetime 

@pytest.fixture(scope="module")
def test_client():
    flask_app = create_app('flask_test.cfg')

    #create a test version of the app using /instance/flask_test.cfg using Werkzeug test Client
    testing_client = flask_app.test_client()

    #establish app context before tests
    ctx = flask_app.app_context()
    ctx.push()

    yield testing_client  # this is where the testing happens!

    ctx.pop()

@pytest.fixture(scope="module")
def init_database():
    #clear databases
    db.drop_all()
    db.drop_all(bind=["auth"])

    # Create the databases and the database tables
    db.create_all()
    db.create_all(bind=["auth"]) 

    # Insert user data
    new_user = Login("test","pass")
    new_user.save_to_db()
    new_mod = Login("mod","pass", True)
    new_mod.save_to_db()
    posts = [
        {"user_id":1, "title": "Faker 123", "content": "Donald trump nukes brazil", "tag":"party", "created": datetime(2020, 5, 17),"popularity":0, "flagged": True},
        {"user_id":1, "title": "2", "content": "b", "tag":"sport", "created": datetime(2010, 5, 17),"popularity":15, "flagged": True},
        {"user_id":1, "title": "3", "content": "c", "tag":"sport", "created": datetime(2021, 5, 17),"popularity":14, "flagged": False},
        {"user_id":1, "title": "4", "content": "d", "tag":"movies", "created": datetime(2012, 5, 17),"popularity":13, "flagged": False},
        {"user_id":1, "title": "5", "content": "e", "tag":"movies", "created": datetime(2013, 5, 6),"popularity":10, "flagged": False},
        {"user_id":1, "title": "6", "content": "f", "tag":"food", "created": datetime(2014, 5, 17),"popularity":9, "flagged": False},
        {"user_id":2, "title": "7", "content": "g", "tag":"food", "created": datetime(2015, 5, 17),"popularity":8, "flagged": False},
        {"user_id":2, "title": "8", "content": "h", "tag":"food", "created": datetime(2016, 5, 17),"popularity":7, "flagged": False},
        {"user_id":2, "title": "9", "content": "i", "tag":"food", "created": datetime(2017, 5, 17),"popularity":6, "flagged": False},
        {"user_id":2, "title": "10", "content": "j", "tag":"travel", "created": datetime(2018, 5, 17),"popularity":3, "flagged": True},
        {"user_id":2, "title": "11", "content": "k", "tag":"games", "created": datetime(2019, 5, 17),"popularity":2, "flagged": True},
        {"user_id":2, "title": "12", "content": "l", "tag":"technology", "created": datetime(2020, 5, 17),"popularity":1, "flagged": False}
        ]
    for post in posts:
        new_post = Blog(post['user_id'],post['title'],post['content'], post['tag'], post['created'], post['popularity'], post['flagged'])
        new_post.save_to_db()
    
    yield db  # this is where the testing happens!

    #clear databases
    db.drop_all()
    db.drop_all(bind=["auth"])

