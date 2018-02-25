from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField


class CurrentGame(FlaskForm):
    game_id = StringField('Game id')
    white_player_id = StringField('Id')
    white_player_name = StringField('Name')
    black_player_id = StringField('Id')
    black_player_name = StringField('Name')
    game_over = StringField('Game over')
    game_board = TextAreaField('Board')
