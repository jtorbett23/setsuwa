from flask_restful import Resource, reqparse 
from flask_backend.models import User, Blog
from flask_backend import db_api
from flask import jsonify
from flask_jwt_extended import jwt_required

parser = reqparse.RequestParser()
parser.add_argument('user_id')
parser.add_argument('post_id')
parser.add_argument('title')
parser.add_argument('content')
parser.add_argument('tag')

class User_Access(Resource):
    # @jwt_required -> commented out for development
    def get(self):
        data = parser.parse_args() 
        try:
            return_user = User.find_by_id(data['user_id'])
            return jsonify(Return_user.to_object())
        except:
            return {"message": "request failed"}, 500

class Post(Resource):
    # @jwt_required -> commented out for development
    def post(self):
        data = parser.parse_args()
        new_blog = Blog(data['user_id'],data['title'],data['content'],data['tag'])
        new_blog.save_to_db()
        try:
            
            return {"message" :"Post created",
                    "post_id": new_blog.post_id},200
        except:
            return {"message": "Create post failed"}, 500

    def get(self):
        data = parser.parse_args() 
        try:
            return_blog = Blog.find_by_id(data['post_id'])
            return jsonify(return_blog.to_object())
        except:
            return {"message": "Retrieve post failed"}, 500
            
db_api.add_resource(User_Access,"/db/user")
db_api.add_resource(Post,"/db/post")