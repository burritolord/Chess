import string
import random
from src import app, socketio
from flask import render_template, redirect, url_for, request, session
from src import db
from src.models.player import Player
from src.models.chess_game import ChessGame
from src.models.game_score import GameScore
from src.forms.delete_game import RemoveGame
from src.forms.join_game import JoinGame
from src.forms.move_piece import MovePiece
from src.forms.current_game import CurrentGame
from src.forms.create_game import CreateGame
from flask_socketio import SocketIO, emit, join_room, leave_room, close_room, rooms, disconnect
from src.piece.color import Color


@app.route('/')
@app.route('/index')
def homepage():
    return render_template('index.html')


@app.route('/user/add')
def add_users():
    chars = string.ascii_letters
    random1 = ''.join((random.choice(chars)) for _ in range(10))
    random2 = ''.join((random.choice(chars)) for _ in range(10))
    random3 = ''.join((random.choice(chars)) for _ in range(10))

    u1 = Player(fullname='nick james', username=random1, email=random1 + "@blah.com", password='blah')
    u2 = Player(fullname='tom blow', username=random2, email=random2 + "@blah.com", password='candy')
    u3 = Player(fullname='jack black', username=random3, email=random3 + "@blah.com", password='stuff')

    g1 = ChessGame(white_player=u1, black_player=u2)
    g2 = ChessGame(white_player=u1, black_player=u3)
    g3 = ChessGame()

    s1 = GameScore(game=g1, white_score=1, black_score=0)
    s2 = GameScore(game=g2, white_score=.5, black_score=.5)

    s1.game.white_player = u3

    db.session.add(g1)
    db.session.add(g2)
    db.session.add(g3)
    db.session.add(s1)
    db.session.add(s2)
    db.session.commit()

    return "users added"


@app.route('/chess/test', methods=['GET', 'POST'])
def chess_test():
    template_vars = {
        'removegame_form': RemoveGame(),
        'joingame_form': JoinGame(),
        'movepiece_form': MovePiece(),
        'currentgame_form': CurrentGame(),
        'creategame_form': CreateGame(),
        'players': Player.query.all(),
        'games': ChessGame.query.all()
    }

    if 'current_game' in session:
        game = ChessGame.load_by_id(session['current_game'])
        if game:
            wp = game.white_player if game.white_player else None
            bp = game.black_player if game.black_player else None
            template_vars['currentgame_form'].game_id.data = game.id
            template_vars['currentgame_form'].white_player_id.data = wp.id if wp else ''
            template_vars['currentgame_form'].white_player_name.data = wp.username if wp else ''
            template_vars['currentgame_form'].black_player_id.data = bp.id if bp else ''
            template_vars['currentgame_form'].black_player_name.data = bp.username if bp else ''
            template_vars['currentgame_form'].game_over.data = 'True' if game.is_over else 'False'
            template_vars['currentgame_form'].game_board.data = str(game)

    return render_template('chess.html', **template_vars)


@app.route('/chess/test/new-game', methods=['POST'])
def new_game_test():
    form = CreateGame()
    if request.method == 'POST' and form.validate_on_submit():
        # TODO Need to validate fen value
        if form.fen.data:
            game = ChessGame(form.fen.data)
        else:
            game = ChessGame()

        game.save_to_db()

    return redirect(url_for('chess_test'))


@app.route('/chess/test/remove-game', methods=['POST'])
def remove_game_test():
    form = RemoveGame()
    if form.validate_on_submit():
        game = ChessGame.load_by_id(form.remove_game_id.data)
        if game:
            game.delete_from_db()

    return redirect(url_for('chess_test'))


@app.route('/chess/test/join-game', methods=['POST'])
def join_game_test():
    form = JoinGame()
    game = ChessGame.load_by_id(form.join_game_id.data)
    player = Player.load_by_id(form.user_id.data)
    if game and player:
        session['game_room'] = game.id
        session['current_game'] = game.id
        color = form.color.data
        if color == Color.WHITE.value:
            game.white_player = player
            game.save_to_db()
        elif color == Color.BLACK.value:
            game.black_player = player
            game.save_to_db()

    return redirect(url_for('chess_test'))


@socketio.on('move_piece', namespace='/chess-game')
def move_piece_test(json):
    if 'current_game' in session:
        game = ChessGame.load_by_id(session['current_game'])
        result = game.move_piece(json['start_position'], json['end_position'])
        game.save_to_db()
        emit('update_game', {'result': result.to_dict(), 'board': str(game)})


@socketio.on('join_game', namespace='/chess-game')
def join_game_room(json):
    game = ChessGame.load_by_id(session['current_game'])
    if game:
        my_rooms = rooms()
        if game.id not in my_rooms:
            join_room(session['game_room'])
