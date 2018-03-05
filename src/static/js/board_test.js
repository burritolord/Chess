$(document).ready(function() {
    var socket = io.connect('http://' + document.domain + ':' + location.port + '/chess-game');

    // Update game info
    socket.on('update_game', function (game_data) {
        var x = 1;
        console.log(game_data);

        // Game id
        if (game_data.hasOwnProperty('game_id')) {
            $('#game_id').val(game_data.game_id)
        }

        // Update board
        if (game_data.hasOwnProperty('board_string')) {
            $('#game_board').val(game_data.board_string);
        }

        // Update current player
        if (game_data.hasOwnProperty('current_player')) {
            $('#current_player').val(game_data.current_player.username);
        }

        // Update white player
        if (game_data.hasOwnProperty('white_player')) {
            $('#white_player_id').val(game_data.white_player.id);
            $('#white_player_name').val(game_data.white_player.username);
        }

        // Update black player
        if (game_data.hasOwnProperty('black_player')) {
            $('#black_player_id').val(game_data.black_player.id);
            $('#black_player_name').val(game_data.black_player.username);
        }

        // Update game over
        if (game_data.hasOwnProperty('game_over')) {
            $('#game_over').val(game_data.game_over);
        }

        // Update player list

        // Update en passant

        // Update check

        // Update checkmate

        // Update draw

        // Update pawn promotion
    });

    $('.join-game .submit').on('click', function () {
        var game_id = $('.join-game #join_game_id').val();
        var user_id = $('.join-game #user_id').val();
        var color = $('.join-game #color').val();
        socket.emit('join_game', {game_id: game_id, user_id: user_id, color: color});
    });

    // Move a piece
    $('.move-piece .submit').on('click', move_piece);
    function move_piece() {
        var start = $('.move-piece #start_position').val();
        var end = $('.move-piece #end_position').val();
        var data = {start_position: start, end_position: end};
        socket.emit('move_piece', data);
    }

    $('#test').on('click', function () {
        socket.emit('test', {})
    });
});