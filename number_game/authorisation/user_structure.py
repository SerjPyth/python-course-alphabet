from flask_restful import fields

user_structure = {
    "id": fields.Integer,
    "username": fields.String,
    "password": fields.String,
    "role": fields.String
}