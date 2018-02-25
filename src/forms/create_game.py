from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class CreateGame(FlaskForm):
    fen = StringField('Fen')
    submit = SubmitField('create')
