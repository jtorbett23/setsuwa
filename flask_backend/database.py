from flask_restful import Resource, reqparse 
from flask_backend.models import User, Post
from flask_backend import db_api
from flask import jsonify
from flask_jwt_extended import jwt_required

parser = reqparse.RequestParser()
parser.add_argument('id', help = 'This field cannot be blank')

class User_Access(Resource):
    # @jwt_required -> commented out for development
    def get(self):
        data = parser.parse_args() 
        try:
            user = User.find_by_id(data['id'])
            return jsonify(user.to_object())
        except:
            return {"message": "request failed"}, 500

db_api.add_resource(User_Access,"/db/user")