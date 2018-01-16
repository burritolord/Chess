from piece.type import Type
from piece.piece import Piece
from piece.color import Color
from piece.move_direction import MoveDirection


class Pawn(Piece):
    """ Class for Pawn chess piece. """

    def __init__(self, color):
        """
        Create a Pawn object

        :param color: Color
            Color that this piece should have.
        :return:
        """
        super().__init__(Type.PAWN, color)
        self._moves[MoveDirection.FORWARD] = 2
        self._moves[MoveDirection.F_RIGHT_DIAG] = 1
        self._moves[MoveDirection.F_LEFT_DIAG] = 1
        self._string_value = 'P' if color == Color.WHITE else 'p'




