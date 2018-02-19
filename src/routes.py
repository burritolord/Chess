from src import app, socketio
from flask import render_template
# from src import db
# from src.models.player import Player
# from src.models.chess_game import ChessGame
# from src.models.game_score import GameScore
# import string
# import random


@app.route('/')
@app.route('/index')
def homepage():
    # chars = string.ascii_letters
    # email1 = ''.join((random.choice(chars)) for _ in range(10))
    # email2 = ''.join((random.choice(chars)) for _ in range(10))
    # email3 = ''.join((random.choice(chars)) for _ in range(10))
    #
    # u1 = Player(fullname='nick', email=email1, password='blah')
    # u2 = Player(fullname='tom', email=email2, password='candy')
    # u3 = Player(fullname='jack', email=email3, password='stuff')
    #
    # g1 = ChessGame(white_player=u1, black_player=u2)
    # g2 = ChessGame(white_player=u1, black_player=u3)
    # g3 = ChessGame()
    #
    # s1 = GameScore(game=g1, white_score=1, black_score=0)
    # s2 = GameScore(game=g2, white_score=.5, black_score=.5)
    #
    # s1.game.white_player = u3
    #
    # db.session.add(g1)
    # db.session.add(g2)
    # db.session.add(g3)
    # db.session.add(s1)
    # db.session.add(s2)
    # db.session.commit()

    return render_template('index.html')


@app.route('/chess')
def chess():
    return render_template('chess.html')
