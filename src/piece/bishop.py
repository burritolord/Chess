from src.piece.type import Type
from src.piece.piece import Piece
from src.piece.color import Color
from src.piece.move_direction import MoveDirection


class Bishop(Piece):
    """ Class for the Bishop piece. """

    def __init__(self, color):
        """
        Create a Bishop object.

        :param color: Color
            Color that this piece should have.
        :return:
        """
        super().__init__(Type.BISHOP, color)
        self._moves[MoveDirection.F_LEFT_DIAG] = -1
        self._moves[MoveDirection.F_RIGHT_DIAG] = -1
        self._moves[MoveDirection.B_LEFT_DIAG] = -1
        self._moves[MoveDirection.B_RIGHT_DIAG] = -1

        self._string_value = 'B' if color == Color.WHITE else 'b'

