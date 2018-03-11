$(document).ready(function() {
    var socket = io.connect('http://' + document.domain + ':' + location.port + '/chess-game');

    // Update game info
    socket.on('update_game', function (game_data) {
        var piece;
        var piece_data;
        var position;
        var $board_position;
        console.log(game_data);

        // Update board after move
        if (game_data.hasOwnProperty('result')) {
            for (position in game_data.result.update_positions) {
                $board_position = $('.board_position[data-position="' + position + '"]');
                if (game_data.result.update_positions[position]) {
                    piece_data = game_data.result.update_positions[position]
                    piece = '<svg class="piece" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="45px" height="45px">\n' +
                            '<use xlink:href="#' + piece_data.color + '-' + piece_data.type + '" x="0" y="0" ></use>\n' +
                            '</svg>';
                    // Remove the piece first just in case same location selected
                    $board_position.empty();
                    $board_position.append(piece);
                }
                else {
                    $board_position.empty();
                }
            }
        }
    });

    // Log errors
    socket.on('error', function (error_data) {
       console.log(error_data.error)
    });

    $('.join-game .submit').on('click', function () {
        var game_id = $('.join-game #join_game_id').val();
        var user_id = $('.join-game #user_id').val();
        var color = $('.join-game #color').val();
        socket.emit('join_game', {game_id: game_id, user_id: user_id, color: color});
    });

    // Move a piece
    $('.board_position').on('click', move_piece);
    function move_piece(event) {
        var $target = $(this);
        var temp_start_pos = '';
        var has_svg;
        var data;

        if (typeof move_piece.start_position == 'undefined') {
            move_piece.start_position = '';
        }

        // Ignore click if it is the first one and it is on a black position
        has_svg = $target.has('svg').length;
        if (!move_piece.start_position && has_svg) {
            move_piece.start_position = $target.data('position');
        }
        else if(move_piece.start_position) {
            temp_start_pos = move_piece.start_position;
            move_piece.start_position = '';
            data = {start_position: temp_start_pos, end_position: $target.data('position')};
            socket.emit('move_piece', data);
        }
    }

});