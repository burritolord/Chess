from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, HiddenField
from wtforms.validators import DataRequired


class RemoveGame(FlaskForm):
    remove_game_id = StringField('Game id', validators=[DataRequired()])
    submit = SubmitField('remove')
    hidden = HiddenField('Remove Game Form', default='remove_form')
