__author__ = 'nick.james'

from MoveDirection import MoveDirection
from abc import ABCMeta


class Piece(metaclass=ABCMeta):
    def __init__(self, type, color):
        self._has_moved = False
        self._type = type
        self._color = color
        self._captured = False
        self._moves = {
            MoveDirection.forward: 0,
            MoveDirection.backward: 0,
            MoveDirection.left: 0,
            MoveDirection.right: 0,
            MoveDirection.f_left_diag: 0,
            MoveDirection.f_right_diag: 0,
            MoveDirection.b_left_diag: 0,
            MoveDirection.b_right_diag: 0,
            MoveDirection.l_shape: False
        }

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

    def __str__(self):
        pass

