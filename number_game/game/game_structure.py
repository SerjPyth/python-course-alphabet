from flask_restful import fields

game_structure = {
    'secret_number': fields.Integer,
    'attempt': fields.Integer,
    'range_from': fields.Integer,
    'range_to': fields.Integer,
    'password': fields.String,
    'players': fields.String,
}
