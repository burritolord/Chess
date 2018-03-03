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

    $('button#test').on('click', function () {
        socket.emit('join_game', {});
    });

    // Move a piece
    $('.move-piece .submit').on('click', move_piece);
    function move_piece() {
        var start = $('.move-piece #start_position').val();
        var end = $('.move-piece #end_position').val();
        var data = {start_position: start, end_position: end};
        socket.emit('move_piece', data);
    }
});