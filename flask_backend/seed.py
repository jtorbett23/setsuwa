#imports
from flask_backend import db
from datetime import datetime 

#post data for seeding
post_data = [
        {'user_id' : 1,'title' : 'My favourite car', 
        'content' : 'My favourite car is a Audi Q7 because it\' big and powerful. I love zooming down the motorways.', 'tag' : 'Cars', 'created' : datetime(2010, 5, 17), 'popularity' : 15},
        {'user_id' : 1, 'title' : 'My hair care routine', 
        'content' : 'It takes a lot of work to get luscious locks like mine. The secret that you\'re probably missing though is snake oil.', 'tag' : 'Hair Care','created' : datetime(2009,5,17), 'popularity' : 20},
        {'user_id' : 2, 'title' : 'Science is great', 
        'content' : 'I think it would be great to see more women in science and other STEM subjects', 'tag' : 'Science', 'created' : datetime(2021, 5, 17), 'popularity' : 100},
        {'user_id' : 2, 'title' : 'Plutonium is scary', 'content' : 'Watch out for radioactive elements like Plutonium they can make you sick', 'tag' : 'Science', 'created' : datetime(2012, 5, 17), 'popularity' : 13},
        {'user_id' : 1, 'title' : 'How do you open a can of beans', 'content' : 'I just can seem to get it open no matter how hard I try', 'tag' : 'Science', 'created' : datetime(2013, 5, 17), 'popularity' : 10},
        {'user_id' : 3, 'title' : 'Dunk School', 'content' : 'When you\'re dunking make sure to get a big run up and crouch low before you jump to get maximum air time to slam it down.', 'tag' : 'Sports', 'created' : datetime(2014, 5, 17), 'popularity' : 9},
        {'user_id' : 3, 'title' : 'Golden State Warriors for the win', 'content' : 'We are dominating right now. I hope another team can try and challenge us this season.', 'tag' : 'Sports', 'created' : datetime(2015, 5, 17), 'popularity' : 8},
        {'user_id' : 4, 'title' : 'Welcome to setsuwa', 
        'content' : 'Hi, welcome to Setsuwa. Please share your whatever you\'d like but keep it clean :)', 'tag' : 'Setsuwa', 'created' : datetime(2020, 5, 17), 'popularity' : 1},
        ]

#user data for seeding
user_data = [
    {'username' : 'johnny bravo', 'password': 'slick hair', 'moderator' : False},
    {'username' : 'madamn curie', 'password': 'radiation', 'moderator' : False},
    {'username' : 'kevin durant', 'password': 'basketball', 'moderator' : False},
    {'username' : 'admin', 'password': '123456', 'moderator' : True}
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