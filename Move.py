__author__ = 'nick.james'
from MoveDirection import MoveDirection


class Move:

    MOVE_OFFSETS = {
        MoveDirection.forward: (0, 1),
        MoveDirection.backward: (1, 0),
        MoveDirection.left: (-1, 0),
        MoveDirection.right: (0, 1),
        MoveDirection.f_left_diag: (-1, 1),
        MoveDirection.f_right_diag: (1, 1),
        MoveDirection.b_left_diag: (-1, -1),
        MoveDirection.b_right_diag: (1, -1),
        MoveDirection.l_shape: [(-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1)]
    }

    def get_possible_moves(self, board, current_position, move_direction, num_spaces):
        possible_moves = []
        piece_on_current_position = board.get_piece(current_position)

        # Handle special case for Knight
        if move_direction == MoveDirection.l_shape:
            for offset in self.MOVE_OFFSETS[move_direction]:
                possible_position = board.get_position(current_position, offset[0], offset[1])
                if possible_position is not None:
                    piece_on_destination = board.get_piece(possible_position)
                    if piece_on_destination is None:
                        possible_moves.append(possible_position)
                    elif piece_on_destination.get_color() != piece_on_current_position.get_color():
                            possible_moves.append(possible_position)

        # Every other piece
        else:
            move_increment_values = (0, 0)
            for count in range(0, num_spaces):
                x_offset, y_offset = self._get_increment_values(move_direction, move_increment_values)
                possible_position = board.get_position(current_position, x_offset, y_offset)
                if possible_position is not None:
                    piece_on_destination = board.get_piece(possible_position)
                    if piece_on_destination is None:
                        possible_moves.append(possible_position)
                    elif piece_on_destination.get_color() != piece_on_current_position.get_color():
                        possible_moves.append(possible_position)
                else:
                    break

        return possible_moves

    def _get_increment_values(self, move_direction, move_offsets):
        increment_values = (0, 0)
        if move_direction != MoveDirection.l_shape:
            increment_values = self.MOVE_OFFSETS[move_direction]
            increment_values = (move_offsets[0] + increment_values[0],
                                move_offsets[1] + increment_values[1])
        return increment_values


