from flask_restful import Resource, reqparse 
from flask_backend.models import Login, Revoked_Token
from flask_backend import auth_api, db
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)

parser = reqparse.RequestParser()
parser.add_argument('username', help = 'This field cannot be blank', required = True)
parser.add_argument('password', help = 'This field cannot be blank', required = True)

class Register_User(Resource):
    def post(self):
        data = parser.parse_args()
        if Login.find_by_username(data['username']):
            return {'message': 'User {} already exists'. format(data['username'])}, 400    
        new_user = Login(
            username = data['username'],
            plaintext_password = data['password']
        )
        try:
            new_user.save_to_db()
            return {"message" : data['username'] + " has been created"}, 200
        except:
            db.session.close()
            return {'message': 'Something went wrong'}, 500

class Login_User(Resource):
    def post(self):
        data = parser.parse_args()
        current_user = Login.find_by_username(data['username'])
        if not current_user:
            return {'message': 'Incorrect username/password'}
        if current_user.is_correct_password(data['password']):
            access_token = create_access_token(identity = data['username'])
            refresh_token = create_refresh_token(identity = data['username'])
            return {
                "user_id": current_user.user_id,
                'access_token': access_token,
                'refresh_token': refresh_token
            }
        else:
            db.session.close()
            return {'message': 'Incorrect username/password'}

class Logout_Access(Resource):
    @jwt_required
    def post(self):
        jti = get_raw_jwt()['jti']
        try:
            revoked_token = RevokedTokenModel(jti = jti)
            revoked_token.save_to_db()
            return {'message': 'Access token has been revoked'}
        except:
            db.session.close()
            return {'message': 'Something went wrong'}, 500
      
      
class Logout_Refresh(Resource):
    @jwt_refresh_token_required
    def post(self):
        jti = get_raw_jwt()['jti']
        try:
            revoked_token = RevokedTokenModel(jti = jti)
            revoked_token.save_to_db()
            return {'message': 'Refresh token has been revoked'}
        except:
            db.session.close()
            return {'message': 'Something went wrong'}, 500
      
      
class Token_Refresh(Resource):
    @jwt_refresh_token_required
    def post(self):
        current_user = get_jwt_identity()
        access_token = create_access_token(identity = current_user)
        return {'access_token': access_token}

auth_api.add_resource(Register_User,"/auth/register")
auth_api.add_resource(Login_User,"/auth/login")
auth_api.add_resource(Token_Refresh,"/auth/refresh")
auth_api.add_resource(Logout_Access,"/auth/logoutAccess")
auth_api.add_resource(Logout_Refresh,"/auth/logoutRefresh")


