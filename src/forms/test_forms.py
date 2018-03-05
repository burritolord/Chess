from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired
from src.piece.color import Color


class CreateGame(FlaskForm):
    fen = StringField('Fen', default='rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq -')
    submit = SubmitField('create')


class CurrentGame(FlaskForm):
    game_id = StringField('Game id')
    white_player_id = StringField('White Player id')
    white_player_name = StringField('White Player name')
    black_player_id = StringField('Black Player id')
    black_player_name = StringField('Black Player name')
    current_player = StringField('Current player name')
    game_over = StringField('Game over')
    game_board = TextAreaField('Board')


class RemoveGame(FlaskForm):
    remove_game_id = StringField('Game id', validators=[DataRequired()])
    submit = SubmitField('remove')


class JoinGame(FlaskForm):
    join_game_id = StringField('Game id', validators=[DataRequired()])
    user_id = StringField('User id', validators=[DataRequired()])
    color = SelectField('Color', choices=[(str(Color.WHITE.value), 'White'), (str(Color.BLACK.value), 'Black')])


class MovePiece(FlaskForm):
    start_position = StringField('Start position')
    end_position = StringField('End position')
