from  flask_restx import Namespace,Resource, fields
from flask import request
from  api.orders.orders import User 
from werkzeug.security import generate_password_hash, check_password_hash
from http import HTTPStatus
from api.utils import db

auth_namespace = Namespace('auth', description="a namspace for authentication")


signup_model = auth_namespace.model(
    'User',{
        'id': fields.Integer(),
        'username': fields.String(required=True, description="A username "),
        'email': fields.String(required=True, description="An email"),
        'password': fields.String(required=True, description="A password"),
        
    }
)

user_model=auth_namespace.model(
    'User',{'id': fields.Integer(),
        'username': fields.String(required=True, description="A username "),
        'email': fields.String(required=True, description="An email"),
        'password_hash': fields.String(required=True, description="A password"),
        'is_active': fields.Boolean(description="This shows that user is active"),
        'is_staff':fields.Boolean(description="Thiw show is activ admin")

    }
)

@auth_namespace.route('/signup')
class SignUp(Resource):

    @auth_namespace.expect(signup_model)
    @auth_namespace.marshal_with(user_model)
    def post(self):
        """
            Create a new user account 
        """

        data = request.get_json()
        
        new_user =User(
            username = data.get('username'),
            email = data.get('email'),
            password_hash =generate_password_hash(data.get('password')),
        )

        db.session.add(self)
        db.session.commit()

        return new_user, HTTPStatus.CREATED

@auth_namespace.route('/login')
class Login(Resource):

    def post(self):
        """ 
            Generate a JWT pair 
        """
        pass



# @auth_namespace.route('/signup')
# class SignUp(Resource):

#     @auth_namespace.expect(signup_model)
#     @auth_namespace.marshal_with(signup_model)
#     def post(self):
#         """
#             Create a new user account 
#         """
#         data = request.get_json()

#         # Dataların yoxlanması
#         if not data:
#             return {"error": "Request data is missing"}, HTTPStatus.BAD_REQUEST

#         if not data.get('username') or not data.get('email') or not data.get('password'):
#             return {"error": "Username, email, and password are required"}, HTTPStatus.BAD_REQUEST

#         # Şifrənin hash-lənməsi
#         hashed_password = generate_password_hash(data.get('password'))

#         new_user = User(
#             username=data.get('username'),
#             email=data.get('email'),
#             password_hash=hashed_password,
#         )

#         db.session.add(new_user)
#         db.session.commit()

#         return new_user, HTTPStatus.CREATED
