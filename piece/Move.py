__author__ = 'nick.james'
from piece.MoveDirection import MoveDirection


class Move:

    MOVE_OFFSETS = {
        MoveDirection.forward: (0, 1),
        MoveDirection.backward: (0, -1),
        MoveDirection.left: (-1, 0),
        MoveDirection.right: (1, 0),
        MoveDirection.f_left_diag: (-1, 1),
        MoveDirection.f_right_diag: (1, 1),
        MoveDirection.b_left_diag: (-1, -1),
        MoveDirection.b_right_diag: (1, -1),
        MoveDirection.l_shape: [(-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1)]
    }

    def get_possible_moves(self, board, current_position, move_direction, num_spaces):
        possible_moves = []
        piece_on_current_position = board[current_position]
        possible_squares = board.get_possible_positions(current_position, move_direction)

        if piece_on_current_position:
            # Handle special case for Knight
            if move_direction == MoveDirection.l_shape:
                for possible_position in possible_squares:
                    piece_on_destination = board.is_position_occupied(possible_position)
                    if not piece_on_destination:
                        possible_moves.append(possible_position)
                    elif board[possible_position].color != piece_on_current_position.color:
                        possible_moves.append(possible_position)

            # Every other piece
            else:
                piece_num_spaces = piece_on_current_position.move_directions[move_direction]
                num_spaces = len(possible_squares) if piece_num_spaces == -1 else num_spaces
                num_spaces = min(len(possible_squares), num_spaces)

                for count in range(0, num_spaces):
                    piece_on_destination = board.is_position_occupied(possible_squares[count])
                    if not piece_on_destination:
                        possible_moves.append(possible_squares[count])
                    elif board[possible_squares[count]].color != piece_on_current_position.color:
                        possible_moves.append(possible_squares[count])
                        break
                    else:  # Piece is same color as one we are working with
                        break

        return possible_moves

    def get_increment_values(self, move_direction, x_position, y_position):
        increment_values = (0, 0)
        if move_direction != MoveDirection.l_shape:
            x_increment, y_increment = self.MOVE_OFFSETS[move_direction]
            increment_values = (x_position + x_increment, y_position + y_increment)
        return increment_values


