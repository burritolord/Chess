from piece.Type import Type
from piece.Piece import Piece
from piece.Color import Color
from piece.MoveDirection import MoveDirection


class Bishop(Piece):
    """ Class for the Bishop piece. """

    def __init__(self, color):
        """
        Create a Bishop object.

        :param color: Color
            Color that this piece should have.
        :return:
        """
        super().__init__(Type.bishop, color)
        self._moves[MoveDirection.f_left_diag] = -1
        self._moves[MoveDirection.f_right_diag] = -1
        self._moves[MoveDirection.b_left_diag] = -1
        self._moves[MoveDirection.b_right_diag] = -1

        self._string_value = 'B' if color == Color.white else 'b'

