import re


class ChessHelper:
    """

    """

    @staticmethod
    def to_string(value):
        """

        :param value:
        :return:
        """
        if isinstance(value, str):
            return value
        return value.decode('utf-8')

    @staticmethod
    def is_valid_position(position):
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
