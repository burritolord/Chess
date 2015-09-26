__author__ = 'nick.james'
from Type import Type
from Piece import Piece
from MoveDirection import MoveDirection


class Bishop(Piece):

    def __init__(self, color):
        super().__init__(Type.bishop, color)
        self._moves[MoveDirection.f_left_diag] = -1
        self._moves[MoveDirection.f_right_diag] = -1
        self._moves[MoveDirection.b_left_diag] = -1
        self._moves[MoveDirection.b_right_diag] = -1

    def __str__(self):
        return 'B'

