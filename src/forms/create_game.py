from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, HiddenField


class CreateGame(FlaskForm):
    fen = StringField('Fen')
    submit = SubmitField('create')
    hidden = HiddenField('Create Game Form', default='create_form')
