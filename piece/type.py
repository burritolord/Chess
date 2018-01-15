from enum import Enum


class Type(Enum):
    """ Enumeration class used for assigning the type to a piece. """
    pawn = 0
    rook = 1
    knight = 2
    bishop = 3
    queen = 4
    king = 5
