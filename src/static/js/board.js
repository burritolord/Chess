$(document).ready(function() {
    var socket = io.connect('http://' + document.domain + ':' + location.port + '/chess-game');

    // Update game info
    socket.on('update_game', function (game_data) {
        var white_player = 1;
        if (game_data.hasOwnProperty('room')) {
            ROOM = game_data.room;
        }
        // Update board

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

    // Join a game
    // $('form.join-game').on('submit', function () {
    //     // var gid = $('.join-game #join_game_id').val();
    //     // var uid = $('.join-game #user_id').val();
    //     // var color = $('.join-game #color').val();
    //     // var data = {game_id: gid, player_id: uid, color: color};
    //     socket.emit('join_game', {data: 'test'});
    // });

    // Move a piece
    $('.move-piece .submit').on('click', move_piece);
    function move_piece() {
        // var data = {game_id: gid, player_id: uid, color: color};
        // socket.emit('join_game', data);
    }
});