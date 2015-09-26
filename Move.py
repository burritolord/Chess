__author__ = 'nick.james'


class Move:
    forward = 8
    backward = -8
    left = -1
    right = 1
    f_left_diag = 7
    f_right_diag = 9
    b_left_diag = -7
    b_right_diag = -9
    l_shape = [-17, -15, -10, -6, 6, 10, 15, 17]

    def move_piece(self, board, start_position, end_position):
        pass