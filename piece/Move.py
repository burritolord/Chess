__author__ = 'nick.james'
from piece.MoveDirection import MoveDirection
from piece.Color import Color
from piece.Type import Type

class Move:

    MOVE_OFFSETS = {
        Color.white: {MoveDirection.forward: (0, 1),
                      MoveDirection.backward: (0, -1),
                      MoveDirection.left: (-1, 0),
                      MoveDirection.right: (1, 0),
                      MoveDirection.f_left_diag: (-1, 1),
                      MoveDirection.f_right_diag: (1, 1),
                      MoveDirection.b_left_diag: (-1, -1),
                      MoveDirection.b_right_diag: (1, -1),
                      MoveDirection.l_shape: [(-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1)]
                      },
        Color.black: {MoveDirection.forward: (0, -1),
                      MoveDirection.backward: (0, 1),
                      MoveDirection.left: (1, 0),
                      MoveDirection.right: (-1, 0),
                      MoveDirection.f_left_diag: (1, -1),
                      MoveDirection.f_right_diag: (-1, -1),
                      MoveDirection.b_left_diag: (1, 1),
                      MoveDirection.b_right_diag: (-1, 1),
                      MoveDirection.l_shape: [(-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1)]
                      }
    }

    def get_possible_moves(self, board, current_position, move_direction, num_spaces):
        possible_moves = []
        piece_on_position = board[current_position]

        if piece_on_position:
            possible_positions = board.get_possible_positions(current_position, move_direction, piece_on_position.color)

            # Handle special case for Knight
            if move_direction == MoveDirection.l_shape:
                for possible_position in possible_positions:
                    piece_on_destination = board.is_position_occupied(possible_position)
                    if not piece_on_destination:
                        possible_moves.append(possible_position)
                    elif board[possible_position].color != piece_on_position.color:
                        possible_moves.append(possible_position)

            # Every other piece
            else:
                piece_num_spaces = piece_on_position.move_directions[move_direction]
                num_spaces = len(possible_positions) if piece_num_spaces == -1 else num_spaces
                num_spaces = min(len(possible_positions), num_spaces)

                for possible_position in possible_positions[0:num_spaces]:
                    destination_occupied = board.is_position_occupied(possible_position)

                    #TODO clean up the following code
                    if piece_on_position.type == Type.king:
                        if not destination_occupied:
                            if not board.is_check(piece_on_position.color, possible_position):
                                possible_moves.append(possible_position)
                        elif board[possible_position].color != piece_on_position.color:
                            if not board.is_check(piece_on_position.color, possible_position):
                                possible_moves.append(possible_position)
                                break
                        else:  # Piece is same color as one we are working with
                            break
                    else:
                        if not destination_occupied:
                            possible_moves.append(possible_position)
                        elif board[possible_position].color != piece_on_position.color:
                            possible_moves.append(possible_position)
                            break
                        else:  # Piece is same color as one we are working with
                            break

        return possible_moves


