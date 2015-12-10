__author__ = 'nick.james'

from abc import ABCMeta
from piece.Move import Move


class Piece(metaclass=ABCMeta):
    def __init__(self, piece_type, color):
        self._has_moved = False
        self._type = piece_type
        self._color = color
        self._captured = False
        self._string_value = ''
        self._move = Move()
        self._moves = {}

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, piece_type):
        self._type = piece_type

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color

    @property
    def capture(self):
        return self._captured

    @capture.setter
    def capture(self, captured):
        self._captured = captured

    @property
    def has_moved(self):
        return self._has_moved

    @has_moved.setter
    def has_moved(self, moved):
        self._has_moved = moved

    @property
    def move_directions(self):
        return self._moves

    def get_possible_moves(self, board, current_position):
        possible_moves = []
        for move_direction, num_spaces in self._moves.items():
            possible_moves += self._move.get_possible_moves(board, current_position, move_direction, num_spaces)

        return possible_moves

    def __str__(self):
        return self._string_value

