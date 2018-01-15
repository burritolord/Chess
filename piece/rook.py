from piece.type import Type
from piece.piece import Piece
from piece.color import Color
from piece.move_direction import MoveDirection


class Rook(Piece):

    def __init__(self, color):
        """
        Create a Rook piece.

        :param color:
            Color that this piece should have.
        :return:
        """
        super().__init__(Type.ROOK, color)
        self._moves[MoveDirection.FORWARD] = -1
        self._moves[MoveDirection.BACKWARD] = -1
        self._moves[MoveDirection.LEFT] = -1
        self._moves[MoveDirection.RIGHT] = -1

        self._string_value = 'R' if color == Color.WHITE else 'r'

