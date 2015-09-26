__author__ = 'nick.james'
from enum import Enum


class MoveDirection(Enum):
    forward = 0
    backward = 1
    left = 2
    right = 3
    f_left_diag = 4
    f_right_diag = 5
    b_left_diag = 6
    b_right_diag = 7
    l_shape = 8