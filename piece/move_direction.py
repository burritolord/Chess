from enum import Enum


class MoveDirection(Enum):
    """
    Enumeration for all possible directions a piece can move.
    """
    FORWARD = 0
    BACKWARD = 1
    LEFT = 2
    RIGHT = 3
    F_LEFT_DIAG = 4
    F_RIGHT_DIAG = 5
    B_LEFT_DIAG = 6
    B_RIGHT_DIAG = 7
    L_SHAPE = 8
