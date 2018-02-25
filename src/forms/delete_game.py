from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class RemoveGame(FlaskForm):
    remove_game_id = StringField('Game id', validators=[DataRequired()])
    submit = SubmitField('remove')
