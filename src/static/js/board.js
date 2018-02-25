$(document).ready(function() {
    var socket = io.connect('http://' + document.domain + ':' + location.port + '/chess-game');
    var ROOM;
    // socket.on('connect', function() {
    //
    // });

    // Handle updated board.
    socket.on('game_created', function (data) {
        console.log(data);
        ROOM = data.room;
        add_to_game_table(data);
    });

    // Update game info
    socket.on('update_game', function (data) {
        var white_player = 1;
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

    // Create a new game
    $('.new-game .submit').on('click', new_game);
    function new_game() {
        socket.emit('new_game', {});
    }

    // Remove a game
    $('.remove-game .submit').on('click', remove_game);
    function remove_game() {
        var id = $('.remove-game #game_id').val();
        var data = {game_id: id};
        socket.emit('remove_game', data);

        remove_from_game_table(data)
    }

    // Join a game
    $('.join-game .submit').on('click', join_game);
    function join_game() {
        var gid = $('.join-game #game_id').val();
        var uid = $('.join-game #user_id').val();
        var color = $('.join-game #color').val();
        var data = {game_id: gid, player_id: uid, color: color};
        socket.emit('join_game', data);
    }

    function add_to_game_table(data) {
        var new_game = "<tr id='game-" + data.game_id + "'><td>" + data.game_id + "</td><td>" + data.white_player + "</td><td>" + data.black_player + "</td></tr>";
        $("#games").append(new_game);
    }

    function remove_from_game_table(data) {
        var $game_row = $("#games #game-" + data.game_id);
        if ($game_row.length !== 0) {
            $game_row.remove();
        }
    }
    function move_piece(event) {
        socket.emit('move_piece', {data: 'I\'m connected!'});
    }
});