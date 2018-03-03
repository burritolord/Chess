from enum import Enum


class Type(Enum):
    """ Enumeration class used for assigning the type to a piece. """
    PAWN = 'pawn'
    ROOK = 'rook'
    KNIGHT = 'knight'
    BISHOP = 'bishop'
    QUEEN = 'queen'
    KING = 'king'
