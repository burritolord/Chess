__author__ = 'nick.james'

from Move import Move
from abc import ABCMeta
from MoveDirection import MoveDirection


class Piece(metaclass=ABCMeta):
    def __init__(self, type, color):
        self._has_moved = False
        self._type = type
        self._color = color
        self._captured = False
        self._string_value = ''
        self._move = Move()
        self._moves = {}

    def get_type(self):
        return self._type

    def set_type(self, type):
        self._type = type

    def get_color(self):
        return self._color

    def set_color(self, color):
        self._color = color

    def get_capture(self):
        return self._captured

    def set_capture(self, captured):
        self._captured = captured

    def get_has_moved(self):
        return self._has_moved

    def set_has_moved(self, moved):
        self._has_moved = moved

    def get_all_move_directions(self):
        return self._moves

    def get_possible_moves(self, board, current_position):
        possible_moves = []
        move = Move()
        for move_direction, num_spaces in self._moves.items():
            possible_moves += move.get_possible_moves(board, current_position, move_direction, num_spaces)

        return possible_moves

    def __str__(self):
        return self._string_value

