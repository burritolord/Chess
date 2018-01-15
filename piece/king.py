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
        super().__init__(Type.king, color)
        self._moves[MoveDirection.forward] = 1
        self._moves[MoveDirection.backward] = 1
        self._moves[MoveDirection.left] = 2
        self._moves[MoveDirection.right] = 2
        self._moves[MoveDirection.f_left_diag] = 1
        self._moves[MoveDirection.f_right_diag] = 1
        self._moves[MoveDirection.b_left_diag] = 1
        self._moves[MoveDirection.b_right_diag] = 1

        self._string_value = 'K' if color == Color.white else 'k'

    @property
    def has_moved(self):
        return super().has_moved

    @Piece.has_moved.setter
    def has_moved(self, moved):
        """
        Extends super class version. Changes the moves structure for castling.

        :param moved: bool
            True if the piece has moved, False otherwise.
        :return:
        """
        Piece.has_moved.fset(self, moved)
        self._moves[MoveDirection.left] = 1
        self._moves[MoveDirection.right] = 1

