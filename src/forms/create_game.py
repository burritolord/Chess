from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class CreateGame(FlaskForm):
    fen = StringField('Fen', default='rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq -')
    submit = SubmitField('create')
