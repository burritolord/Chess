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
        super().__init__(Type.queen, color)
        self._moves[MoveDirection.forward] = -1
        self._moves[MoveDirection.backward] = -1
        self._moves[MoveDirection.left] = -1
        self._moves[MoveDirection.right] = -1
        self._moves[MoveDirection.f_left_diag] = -1
        self._moves[MoveDirection.f_right_diag] = -1
        self._moves[MoveDirection.b_left_diag] = -1
        self._moves[MoveDirection.b_right_diag] = -1

        self._string_value = 'Q' if color == Color.white else 'q'

