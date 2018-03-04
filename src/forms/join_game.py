from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
from src.piece.color import Color


class JoinGame(FlaskForm):
    join_game_id = StringField('Game id', validators=[DataRequired()])
    user_id = StringField('User id', validators=[DataRequired()])
    color = SelectField('Color', choices=[(str(Color.WHITE.value), 'White'), (str(Color.BLACK.value), 'Black')])
