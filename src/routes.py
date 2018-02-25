from src import app, socketio
from flask import render_template, redirect, url_for, request
from src import db
from src.models.player import Player
from src.models.chess_game import ChessGame
from src.models.game_score import GameScore
from src.forms.delete_game import RemoveGame
from src.forms.join_game import JoinGame
from src.forms.move_piece import MovePiece
from src.forms.current_game import CurrentGame
from src.forms.create_game import CreateGame
import string
import random
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


@app.route('/chess', methods=['GET', 'POST'])
def chess():
    removegame_form = RemoveGame()
    joingame_form = JoinGame()
    movepiece_form = MovePiece()
    creategame_form = CreateGame()
    currentgame_form = CurrentGame()
    template_vars = {
        'removegame_form': removegame_form,
        'joingame_form': joingame_form,
        'movepiece_form': movepiece_form,
        'currentgame_form': currentgame_form,
        'creategame_form': creategame_form
    }

    if request.method == 'POST' and creategame_form.validate_on_submit() and creategame_form.hidden.data == 'create_form':
        chessgame = ChessGame()
        chessgame.save_to_db()
        return redirect(url_for('chess'))

    if request.method == 'POST' and removegame_form.validate_on_submit() and removegame_form.hidden.data == 'remove_form':
        game = ChessGame.load_by_id(removegame_form.remove_game_id.data)
        if game:
            game.delete_from_db()
            return redirect(url_for('chess'))

    if request.method == 'POST' and joingame_form.validate_on_submit() and joingame_form.hidden.data == 'join_form':
        game = ChessGame.load_by_id(joingame_form.join_game_id.data)
        player = Player.load_by_id(joingame_form.user_id.data)
        if game and player:
            color = joingame_form.color.data
            if int(color) == Color.WHITE.value:
                game.white_player = player
                game.save_to_db()
                template_vars['new_game'] = game
            elif int(color) == Color.BLACK.value:
                game.black_player = player
                game.save_to_db()
                template_vars['new_game'] = game

            return redirect(url_for('chess'))


    template_vars['players'] = Player.query.all()
    template_vars['games'] = ChessGame.query.all()

    return render_template('chess.html', **template_vars)


@socketio.on('new_game', namespace='/chess-game')
def new_game(json):
    # create new room
    chessgame = ChessGame()
    chessgame.save_to_db()
    join_room(chessgame.id)

    emit_data = {
        'room': chessgame.id,
        'game_id': chessgame.id,
        'board': str(chessgame),
        'white_player': '' if not chessgame.white_player else chessgame.white_player.username,
        'black_player': '' if not chessgame.black_player else chessgame.black_player.username
    }

    emit('game_created', emit_data)


@socketio.on('remove_game', namespace='/chess-game')
def remove_game(json):
    chessgame = ChessGame.load_by_id(json['game_id'])
    if chessgame:
        chessgame.delete_from_db()


@socketio.on('join_game', namespace='/chess-game')
def join_game(json):
    # Need concept of session to add current user but for now, just add
    # supplied user
    updated_values = {}
    chessgame = ChessGame.load_by_id(json['game_id'])
    player = Player.load_by_id(json['player_id'])
    if chessgame and player:
        join_room(chessgame.id)
        if int(json['color']) == Color.WHITE.value:
            updated_values['white_player_username'] = player.username
            updated_values['white_player_id'] = player.id
            chessgame.white_player = player
            chessgame.save_to_db()
            emit('update_game', updated_values, room=chessgame.id)
        elif int(json['color']) == Color.BLACK.value:
            updated_values['black_player_username'] = player.username
            updated_values['black_player_id'] = player.id
            chessgame.black_player = player
            chessgame.save_to_db()
            emit('update_game', updated_values, room=chessgame.id)

    # Emit error?



@socketio.on('move_piece')
def move_piece(json):
    emit('board_update', {'data': 'message received'})
    print(str(json))


@socketio.on('add_player')
def add_player(json):
    pass