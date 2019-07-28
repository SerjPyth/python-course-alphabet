from flask import Blueprint
from flask_restful import Api
from authorisation.routes import RegisterResources, LoginResources, LogoutResources

auth = Blueprint("auth", __name__)
auth_api = Api(auth)
auth_api.add_resource(RegisterResources, '/register')
auth_api.add_resource(LoginResources, '/login')
auth_api.add_resource(LogoutResources, '/logout')