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

        :param position:
        :return:
        """
        pattern = re.compile('^[a-h][0-8]$')
        match = pattern.match(position)

        return match is not None
