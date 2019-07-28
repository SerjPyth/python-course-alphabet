from os import abort
from flask_restful import Resource, reqparse, marshal_with
from requests import session
from authorisation.user_structure import user_structure
from number_game.models import GameUser
from flask import request
from .parser import registration_parse
from db import db


class RegisterResources(Resource):
    @marshal_with(user_structure)
    def post(self):
        args = registration_parse.parse_args()
        name = args['username']
        check_name = GameUser.query.filter_by(username=name).all()
        if check_name:
            abort(401, 'This username is already in use')
        new_user = GameUser(**args)
        db.session.add(new_user)
        db.session.commit()
        return new_user


class LoginResources(Resource):
    def get(self):
        name = request.get.args('username')
        new_user = GameUser.query.filter_by(username=name).first()
        if request.args.get('password') == new_user.password:
            session['logged_in'] = True
            session['user_id'] = new_user.id
            session['role'] = new_user.role

            return 'ok, correct login'

        return 'you have entered wrong password'


class LogoutResources(Resource):
    def get(self):
        session['logged_in'] = False
        return 'You have successfully logged out'
