from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField


class CurrentGame(FlaskForm):
    game_id = StringField('Game id')
    white_player_id = StringField('White Player id')
    white_player_name = StringField('White Player name')
    black_player_id = StringField('Black Player id')
    black_player_name = StringField('Black Player name')
    current_player = StringField('Current player')
    game_over = StringField('Game over')
    game_board = TextAreaField('Board')
