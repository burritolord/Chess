__author__ = 'nick.james'
from Type import Type
from Piece import Piece
from Color import Color
from MoveDirection import MoveDirection


class Pawn(Piece):
    def __init__(self, color):
        super().__init__(Type.pawn, color)
        self._moves[MoveDirection.forward] = 2
        self._moves[MoveDirection.f_left_diag] = 1
        self._moves[MoveDirection.f_right_diag] = 1

        self._string_value = 'P' if color == Color.white else 'p'
