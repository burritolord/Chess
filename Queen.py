__author__ = 'nick.james'
from Type import Type
from Piece import Piece
from MoveDirection import MoveDirection


class Queen(Piece):
    def __init__(self, color):
        super().__init__(Type.queen, color)
        self._moves[MoveDirection.forward] = -1
        self._moves[MoveDirection.backward] = -1
        self._moves[MoveDirection.left] = -1
        self._moves[MoveDirection.right] = -1
        self._moves[MoveDirection.f_left_diag] = -1
        self._moves[MoveDirection.f_right_diag] = -1
        self._moves[MoveDirection.b_left_diag] = -1
        self._moves[MoveDirection.b_right_diag] = -1

    def __str__(self):
        return 'Q'

