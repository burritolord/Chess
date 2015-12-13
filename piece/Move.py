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

        # Handle special case for Knight
        if move_direction == MoveDirection.l_shape:
            current_x_coord, current_y_coord = board.position_to_coordinates(current_position)
            for x_offset, y_offset in self.MOVE_OFFSETS[move_direction]:
                possible_position = board.get_position(current_position, x_offset, y_offset)
                if possible_position is not None:
                    no_y_shift_position = board.get_position(current_position, x_offset, 0)
                    no_y_shift_x, no_y_shift_y = board.position_to_coordinates(no_y_shift_position)
                    if current_y_coord == no_y_shift_y:
                        piece_on_destination = board.is_position_occupied(possible_position)
                        if not piece_on_destination:
                            possible_moves.append(possible_position)
                        elif board[possible_position].color != piece_on_current_position.color:
                                possible_moves.append(possible_position)

        # Every other piece
        else:
            x_offset, y_offset = 0, 0
            max_movement = board.get_dimension() - 1
            board_length = board.get_dimension()
            num_spaces = board.get_dimension() - 1 if num_spaces == -1 else num_spaces
            current_x_coord, current_y_coord = board.position_to_coordinates(current_position)

            if move_direction == MoveDirection.forward:
                max_movement = board_length - current_y_coord - 1
            elif move_direction == MoveDirection.f_right_diag:
                from_right = board_length - current_x_coord - 1
                from_top = board_length - current_y_coord - 1
                max_movement = min(from_top, from_right)
            elif move_direction == MoveDirection.right:
                max_movement = board_length - current_x_coord - 1
            elif move_direction == MoveDirection.b_right_diag:
                from_right = board_length - current_x_coord - 1
                max_movement = min(current_y_coord, from_right)
            elif move_direction == MoveDirection.backward:
                max_movement = current_y_coord
            elif move_direction == MoveDirection.b_left_diag:
                max_movement = min(current_y_coord, current_x_coord)
            elif move_direction == MoveDirection.left:
                max_movement = current_x_coord
            elif move_direction == MoveDirection.f_left_diag:
                from_top = board_length - current_y_coord - 1
                max_movement = min(from_top, current_x_coord)
            num_spaces = min(num_spaces, max_movement)

            for count in range(0, num_spaces):
                x_offset, y_offset = self._get_increment_values(move_direction, x_offset, y_offset)
                possible_position = board.get_position(current_position, x_offset, y_offset)
                piece_on_destination = board.is_position_occupied(possible_position)

                if not piece_on_destination:
                    possible_moves.append(possible_position)
                elif board[possible_position].color != piece_on_current_position.color:
                    possible_moves.append(possible_position)
                else:  # Piece is same color as one we are working with
                    break

        return possible_moves

    def _get_increment_values(self, move_direction, x_position, y_position):
        increment_values = (0, 0)
        if move_direction != MoveDirection.l_shape:
            x_increment, y_increment = self.MOVE_OFFSETS[move_direction]
            increment_values = (x_position + x_increment, y_position + y_increment)
        return increment_values


