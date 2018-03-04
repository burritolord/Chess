$(document).ready(function() {
    var socket = io.connect('http://' + document.domain + ':' + location.port + '/chess-game');

    // Update game info
    socket.on('update_game', function (game_data) {
        var x = 1;
        console.log(game_data);

        // Update board
        if (game_data.hasOwnProperty('board')) {
            $('#game_board').val(game_data['board']);
        }

        // Update users

        // Update player list

        // Update current player

        // Update game over

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