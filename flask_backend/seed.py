#imports
from flask_backend import db
from datetime import datetime 

#post data for seeding
post_data = [
        {'user_id' : 1,'title' : '2', 'content' : 'b', 'tag' : 'sport', 'created' : datetime(2010, 5, 17), 'popularity' : 15},
        {'user_id' : 1, 'title' : '1', 'content' : 'a', 'tag' : 'sport', 'created' : datetime(2009,5,17), 'popularity' : 20},
        {'user_id' : 1, 'title' : '3', 'content' : 'c', 'tag' : 'sport', 'created' : datetime(2021, 5, 17), 'popularity' : 14},
        {'user_id' : 1, 'title' : '4', 'content' : 'd', 'tag' : 'movies', 'created' : datetime(2012, 5, 17), 'popularity' : 13},
        {'user_id' : 1, 'title' : '5', 'content' : 'e', 'tag' : 'movies', 'created' : datetime(2013, 5, 17), 'popularity' : 10},
        {'user_id' : 1, 'title' : '6', 'content' : 'f', 'tag' : 'food', 'created' : datetime(2014, 5, 17), 'popularity' : 9},
        {'user_id' : 2, 'title' : '7', 'content' : 'g', 'tag' : 'food', 'created' : datetime(2015, 5, 17), 'popularity' : 8},
        {'user_id' : 2, 'title' : '8', 'content' : 'h', 'tag' : 'food', 'created' : datetime(2016, 5, 17), 'popularity' : 7},
        {'user_id' : 2, 'title' : '9', 'content' : 'i', 'tag' : 'food', 'created' : datetime(2017, 5, 17), 'popularity' : 6},
        {'user_id' : 2, 'title' : '10', 'content' : 'j', 'tag' : 'travel', 'created' : datetime(2018, 5, 17), 'popularity' : 3},
        {'user_id' : 2, 'title' : '11', 'content' : 'k', 'tag' : 'games', 'created' : datetime(2019, 5, 17), 'popularity' : 2},
        {'user_id' : 2, 'title' : '12', 'content' : 'l', 'tag' : 'technology', 'created' : datetime(2020, 5, 17), 'popularity' : 1},
        ]

#user data for seeding
user_data = [
    {'username' : 'user', 'password': 'pass', 'moderator' : False},
    {'username' : 'mod', 'password': '123', 'moderator' : True}
]

#seed the database
def seed_db():
    #drop all tables and data
    db.drop_all()
    db.drop_all(bind=['auth'])

    #create all tables
    db.create_all()
    db.create_all(bind=['auth']) 

    #import schema
    from flask_backend import models 
    #save users to database
    for user in user_data:
        new_user = models.Login(user['username'], user['password'], user['moderator'])
        new_user.save_to_db()

    #save posts to database
    for post in post_data:
        new_post = models.Blog(post['user_id'],post['title'],post['content'], post['tag'], post['created'], post['popularity'])
        new_post.save_to_db()