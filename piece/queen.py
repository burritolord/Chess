from piece.type import Type
from piece.piece import Piece
from piece.color import Color
from piece.move_direction import MoveDirection


class Queen(Piece):

    def __init__(self, color):
        """
        Create a Queen piece.

        :param color:
            Color that this piece should have.
        :return:
        """
        super().__init__(Type.QUEEN, color)
        self._moves[MoveDirection.FORWARD] = -1
        self._moves[MoveDirection.BACKWARD] = -1
        self._moves[MoveDirection.LEFT] = -1
        self._moves[MoveDirection.RIGHT] = -1
        self._moves[MoveDirection.F_LEFT_DIAG] = -1
        self._moves[MoveDirection.F_RIGHT_DIAG] = -1
        self._moves[MoveDirection.B_LEFT_DIAG] = -1
        self._moves[MoveDirection.B_RIGHT_DIAG] = -1

        self._string_value = 'Q' if color == Color.WHITE else 'q'

