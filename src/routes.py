from src import app, socketio
from flask import render_template, redirect, url_for, request, session, flash
from src import db
from src.models.player import Player
from src.models.chess_game import ChessGame
from src.models.game_score import GameScore
from src.forms.test_forms import RemoveGame, JoinGame, MovePiece, CurrentGame, CreateGame
from flask_socketio import SocketIO, emit, join_room, leave_room, close_room, rooms, disconnect
from src.piece.color import Color
from src.forms.forms import LoginForm, RegistrationForm
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse
import os


@app.route('/')
@app.route('/index')
@login_required
def index():
    basedir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(basedir, 'static/images/my_chess_sprites.svg')
    template_vars = {}
    with open(file_path, 'r') as f:
        template_vars['sprite'] = f.read()

    if 'current_game' in session:
        game = ChessGame.load_by_id(session['current_game'])
        template_vars['game'] = game.to_dict()

    return render_template('index.html', **template_vars)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = Player.load_by_username(form.username.data)
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = Player(username=form.username.data, password=form.password.data)
        user.save_to_db()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


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
            template_vars['currentgame_form'].current_player.data = game.current_player.username
            template_vars['currentgame_form'].game_over.data = 'True' if game.is_over else 'False'
            template_vars['currentgame_form'].game_board.data = str(game)

    return render_template('chess_test.html', **template_vars)


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
            if 'current_game' in session and session['current_game'] == game.id:
                del session['current_game']
                session.modified = True
            game.delete_from_db()

    return redirect(url_for('chess_test'))


@socketio.on('connect', namespace='/chess-game')
def connect():
    if 'current_game' in session:
        join_room(session['current_game'])


@socketio.on('move_piece', namespace='/chess-game')
def move_piece_test(json):
    if 'current_game' in session and 'game_room' in session:
        game = ChessGame.load_by_id(session['current_game'])
        result = game.move_piece(json['start_position'], json['end_position'])
        game.save_to_db()

        game_dict = game.to_dict()
        game_dict['result'] = result.to_dict()
        game_dict['board_string'] = str(game)

        emit('update_game', game_dict, room=session['game_room'])


@socketio.on('join_game', namespace='/chess-game')
def join_game_room(json):
    game = ChessGame.load_by_id(json['game_id'])
    player = Player.load_by_id(json['user_id'])
    if game and player:
        join_room(game.id)
        session['game_room'] = game.id
        session['current_game'] = game.id
        if json['color'] == Color.WHITE.value:
            game.white_player = player
            game.save_to_db()
        else:
            game.black_player = player
            game.save_to_db()

        game_dict = game.to_dict()
        game_dict['board_string'] = str(game)

        emit('update_game', game_dict)


@socketio.on('test', namespace='/chess-game')
def test(json):
    room = rooms()
