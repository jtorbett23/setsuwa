# setsuwa

Setsuwa is a website designed to bring the community together. Here you can share blogs, make friends and send posts to them from your user account. Or if you just want to browse, you are free to do so. But do be aware, this is a moderated forum - so do be cautious of what you post.

## User stories:

User stories marked with a * represent stretch goals for this project.

- As a non-logged in user, to register, I want to easily be able to navigate to the register page from the any page
- As a non-logged in user, to register, I want a fields to enter a (email,) username, password and a submit button
- As a non-logged in user, to register, I want relevant error messages if my registration is unsuccessful

- As a non-logged in user, to login, I want to easily be able to navigate to the login page from the any page
- As a non-logged in user, to login, I want a fields to enter a username & password and a submit button
- As a non-logged in user, to login, I want relevant error messages if my login is unsuccessful
- As a non-logged in user, to login, I want an option to reset my password*

- As a logged in user, to view my account, I want to easily be able to navigate to my account page from the any page
- As a logged in user, to edit my details, I want an account page where I can change my details*
- As a logged in user, to edit my details,  I want relevant error messages if my detail change is unsuccessful*
- As a logged in user, to delete my posts, I want a button to delete the edit post page
- As a logged in user, to logout of my account, I want a logout button my account page
- As a user, to delete my posts, I want a warning to confirm deleting my post*
- As a logged in user, to view my messages, I want them to be displayed on my account page

- As a logged in user, to create a post,  I want to easily be able to navigate to the create post page from the any page
- As a logged in user, to create a post, I want fields for titles, tags, content and a submit button

- As a logged in user, to share a post, I want a share post form with fields user, message*
- As a logged in user, to share a post,  I want relevant error messages if my share is unsuccessful*

- As a logged in user, to edit my posts, I want a button to edit on my own posts
- As a logged in user, to edit my posts, I want fields for titles, tags, content and a submit button

- As a user, to view posts, I want to see popular posts on my homepage*
- As a user, to view posts, when clicking on a post I am brought to a page for that post
- As a user, to view posts, I want to be to search for posts by tag

- As a user, to view all of a user's posts, I want them to be listed on their account page
- As a user, to view all of a user’s friends, I want them to be listed on their account page

- As a logged in user, to react to a post, I want buttons to upvote and downvote a post
- As a logged in user, to react to a post, I want to be able to leave a comment on a post

- As a user, to report a post,  I want an option to be able to report posts and it be hidden

- As an admin, to moderate posts, I want to be able to delete posts*
- As an admin, to moderate posts, I want to be a page to able review flagged posts
- As an admin, to moderate posts, I want a warning to confirm deleting a post*

## Technologies used:

* Python
  * Flask
  * SQLAlchemy
* SQ lite
* Javascript
  * React
  * Enzyme
* CSS
* Git & Github
* Node.js
Honourable mentions:
* Postman 
* DB Browser

## Using the project

This project is soon to be hosted remotely. If you would like to run this project on your machine then follow the instructions bellow.

### Prerequisites
- Download [Python](https://www.python.org/downloads/ "Python"), follow the link for installation instructions
- Recommended IDE [VS Code](https://code.visualstudio.com/ "VS Code")

### Installing
Open the terminal in the project directory and run this command:
```
git clone https://github.com/AaronM97/setsuwa.git
```
then 
```
cd setsuwa
```
Once you are in the project folder that you have pulled, run:
```
./setsuwa/Scripts/activate
```
This activates the virtual environment for this project. But we are not fully set up yet. Run:
```
pip install -r requirements.txt
```
This installs the required packages we need to run the application. We are now ready to run the app 

### Running the project
In the terminal run, if you are on Windows run:
```
$env:FLASK_APP="main.py"
```
and if you are on Mac run:
```
export FLASK_APP="main.py"
```
Then run: 
```
flask run
```
The app is now up and running. To access it go to: http://localhost:5000/

## Contributors:
Aaron ([@AaronM97](https://github.com/AaronM97 "Aaron's Github")) | 
Aaron ([@jtorbett23](https://github.com/jtorbett23 "Josh's Github"))
