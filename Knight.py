__author__ = 'nick.james'
from Type import Type
from Piece import Piece
from MoveDirection import MoveDirection


class Knight(Piece):
    def __init__(self, color):
        super().__init__(Type.knight, color)
        self._moves[MoveDirection.l_shape] = True

    def __str__(self):
        return 'N'

