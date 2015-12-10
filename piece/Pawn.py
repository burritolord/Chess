__author__ = 'nick.james'
from piece.Type import Type
from piece.Piece import Piece
from piece.Color import Color
from piece.Move import Move
from piece.MoveDirection import MoveDirection


class Pawn(Piece):
    """ Class for Pawn chess piece. """

    def __init__(self, color):
        """
        Create a Pawn object

        :param color: Color
            Color that this piece should have.
        :return:
        """
        super().__init__(Type.pawn, color)
        self._moves[MoveDirection.forward] = 2
        self._string_value = 'P' if color == Color.white else 'p'

    @property
    def has_moved(self):
        return super().has_moved

    @Piece.has_moved.setter
    def has_moved(self, moved):
        """
        Extends super class version. Changes the moves structure for captures.

        :param moved: bool
            True if the piece has moved, False otherwise.
        :return:
        """
        Piece.has_moved.fset(self, moved)
        self._moves[MoveDirection.forward] = 1

    def get_possible_moves(self, board, current_position):
        """
        Extends functionality from super class. Retrieve all possible moves for this piece.

        :param board:
        :param current_position:
        :return:
        """
        left_offsets = Move.MOVE_OFFSETS[MoveDirection.f_left_diag]
        right_offsets = Move.MOVE_OFFSETS[MoveDirection.f_right_diag]

        # Test front left
        possible_position = board.get_position(current_position, left_offsets[0], left_offsets[1])
        if possible_position is not None:
            piece_on_destination = board.is_position_occupied(possible_position)
            if piece_on_destination and board[possible_position].color != self.color:
                self._moves[MoveDirection.f_left_diag] = 1

        # Test front right
        possible_position = board.get_position(current_position, right_offsets[0], right_offsets[1])
        if possible_position is not None:
            piece_on_destination = board.is_position_occupied(possible_position)
            if piece_on_destination and board[possible_position].color != self.color:
                self._moves[MoveDirection.f_right_diag] = 1

        possible_moves = []
        for move_direction, num_spaces in self._moves.items():
            possible_moves += self._move.get_possible_moves(board, current_position, move_direction, num_spaces)

        return possible_moves




