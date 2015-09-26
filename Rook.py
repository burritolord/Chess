__author__ = 'nick.james'
from Type import Type
from Piece import Piece
from MoveDirection import MoveDirection


class Rook(Piece):
    def __init__(self, color):
        super().__init__(Type.rook, color)
        self._moves[MoveDirection.forward] = -1
        self._moves[MoveDirection.backward] = -1
        self._moves[MoveDirection.left] = -1
        self._moves[MoveDirection.right] = -1

    def __str__(self):
        return 'R'

