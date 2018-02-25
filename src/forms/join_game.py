from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from src.piece.color import Color


class JoinGame(FlaskForm):
    game_id = StringField('Game id')
    user_id = StringField('User id')
    color = SelectField('Color', choices=[(Color.WHITE.value, 'White'), (Color.BLACK.value, 'Black')])
    submit = SubmitField('join')
