from flask_restful import Resource, marshal_with
from flask import session
from db import db
from models import Game
# from utils import check_login
from .game_structure import game_structure
from .parser import game_parse


DEFAULT_NUMBER_OF_ATTEMPTS = 3
DEFAULT_RANGE_NUMBER = [0, 10]


class GameResources(Resource):
    # method_decorators = [check_login]

    @marshal_with(game_structure)
    def get(self):
        return Game.query.all()

    @marshal_with(game_structure)
    def post(self):
        args = game_parse.parse_args()
        args['author_id'] = session.get['user_id']

        # if not args.get('secret_number'):
        #     del args['secret_number']
        if not args.get('attempts'):
            args['attempts'] = DEFAULT_RANGE_NUMBER
        if not args.get('range_from'):
            args['range_from'] = DEFAULT_RANGE_NUMBER[0]
        if not args.get('range_to'):
            args['range_to'] = DEFAULT_RANGE_NUMBER[1]

        new_game = Game(**args)

        db.session.add(new_game)
        db.session.commit()

        return new_game


class PlayGame(Resource):
    # method_decorators = [check_login]

    def get(self, game_id):
        game = Game.query.get(game_id)
        result = f"Guess the number from range {game.range_from} - {game.range_to}, " \
            f"You have {game.attempts} tries"

        return result
