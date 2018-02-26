from flask_wtf import FlaskForm
from wtforms import StringField


class MovePiece(FlaskForm):
    start_position = StringField('Start position')
    end_position = StringField('End position')
