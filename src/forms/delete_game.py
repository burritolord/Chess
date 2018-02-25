from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class RemoveGame(FlaskForm):
    game_id = StringField('Game id')
    submit = SubmitField('remove')
