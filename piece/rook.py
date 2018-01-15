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
        super().__init__(Type.rook, color)
        self._moves[MoveDirection.forward] = -1
        self._moves[MoveDirection.backward] = -1
        self._moves[MoveDirection.left] = -1
        self._moves[MoveDirection.right] = -1

        self._string_value = 'R' if color == Color.white else 'r'

