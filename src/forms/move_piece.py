from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class MovePiece(FlaskForm):
    start_position = StringField('Start position')
    end_position = StringField('End position')
    submit = SubmitField('make move')
