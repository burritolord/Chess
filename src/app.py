from flask import Flask
import string
import random

app = Flask(__name__)
app.secret_key = 'my butthole'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://chess@localhost/chess'
app.config['SQLALCHEMY_ECHO'] = True


@app.before_first_request
def create_db():
    db.create_all()

@app.route('/')
def homepage():
    chars = string.ascii_letters
    email1 = ''.join((random.choice(chars)) for _ in range(10))
    email2 = ''.join((random.choice(chars)) for _ in range(10))
    email3 = ''.join((random.choice(chars)) for _ in range(10))

    u1 = Player(fullname='nick', email=email1, password='blah')
    u2 = Player(fullname='tom', email=email2, password='candy')
    u3 = Player(fullname='jack', email=email3, password='stuff')

    g1 = ChessGame(white_player=u1, black_player=u2)
    g2 = ChessGame(white_player=u1, black_player=u3)
    g3 = ChessGame()

    s1 = GameScore(game=g1, white_score=1, black_score=0)
    s2 = GameScore(game=g2, white_score=.5, black_score=.5)

    s1.game.white_player = u3

    db.session.add(g1)
    db.session.add(g2)
    db.session.add(g3)
    db.session.add(s1)
    db.session.add(s2)
    db.session.commit()

    return "Hola"


if __name__ == '__main__':
    from src.db import db
    from src.models.player import Player
    from src.models.chess_game import ChessGame
    from src.models.game_score import GameScore
    db.init_app(app)

    app.run()
