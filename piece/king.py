from piece.type import Type
from piece.piece import Piece
from piece.color import Color
from piece.move_direction import MoveDirection


class King(Piece):

    def __init__(self, color):
        """
        Create a King piece.

        :param color:
            Color that this piece should have.
        :return:
        """
        super().__init__(Type.KING, color)
        self._moves[MoveDirection.FORWARD] = 1
        self._moves[MoveDirection.BACKWARD] = 1
        self._moves[MoveDirection.LEFT] = 2
        self._moves[MoveDirection.RIGHT] = 2
        self._moves[MoveDirection.F_LEFT_DIAG] = 1
        self._moves[MoveDirection.F_RIGHT_DIAG] = 1
        self._moves[MoveDirection.B_LEFT_DIAG] = 1
        self._moves[MoveDirection.B_RIGHT_DIAG] = 1

        self._string_value = 'K' if color == Color.WHITE else 'k'

