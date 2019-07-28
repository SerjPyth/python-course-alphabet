from flask_restful import reqparse

registration_parse = reqparse.RequestParser()
registration_parse.add_argument('username', required=True)
registration_parse.add_argument('password', required=True)
registration_parse.add_argument('role', required=True)
