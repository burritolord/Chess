__author__ = 'nick.james'
from piece.Type import Type
from piece.Piece import Piece
from piece.Color import Color
from piece.MoveDirection import MoveDirection


class Knight(Piece):
    """ Class for knight piece. """

    def __init__(self, color):
        """
        Create a Knight piece.

        :param color:
            Color that this piece should have.
        :return:
        """
        super().__init__(Type.knight, color)
        self._moves[MoveDirection.l_shape] = True
        self._string_value = 'N' if color == Color.white else 'n'

