from enum import Enum


class Type(Enum):
    """ Enumeration class used for assigning the type to a piece. """
    PAWN = 0
    ROOK = 1
    KNIGHT = 2
    BISHOP = 3
    QUEEN = 4
    KING = 5
