from piece.type import Type
from piece.piece import Piece
from piece.color import Color
from piece.move_direction import MoveDirection


class Knight(Piece):
    """ Class for knight piece. """

    def __init__(self, color):
        """
        Create a Knight piece.

        :param color:
            Color that this piece should have.
        :return:
        """
        super().__init__(Type.KNIGHT, color)
        self._moves[MoveDirection.L_SHAPE] = True
        self._string_value = 'N' if color == Color.WHITE else 'n'

