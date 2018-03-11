import re
from src.board.exception import *

class ChessHelper:
    """
    Helper class for chess game.
    """

    @classmethod
    def to_string(cls, value):
        """
        Convert string value to utf-8 encoding

        :param value:
        :return:
        """
        if isinstance(value, str):
            return value
        return value.decode('utf-8')

    @classmethod
    def is_valid_position(cls, position):
        """
        Check if provided position is valid algebraic notation

        :param position: string
            Valid or invalid algebraic notation
        :return: boolean
            True if position is valid, False otherwise
        """
        pattern = re.compile('^[a-h][0-8]$')
        match = pattern.match(position)

        return match is not None

    @classmethod
    def validate_position(cls, position, msg=None):
        """
        Convert position to UTF-8 if it is not already and confirm it is valid algebraic notation.

        :param position: string
            String value that should be in algebraic notation.
        :return:
        :raises: InvalidPositionError
            If position is not valid algebraic notation.
        """
        encoded_position = cls.to_string(position)
        valid = cls.is_valid_position(encoded_position)
        if not valid:
            raise InvalidPositionError(encoded_position, msg)
