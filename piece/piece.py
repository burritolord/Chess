from abc import ABCMeta


class Piece(metaclass=ABCMeta):

    def __init__(self, piece_type, color):
        self._type = piece_type
        self._color = color
        self._captured = False
        self._string_value = ''
        self._moves = {}

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, piece_type):
        self._type = piece_type

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color

    @property
    def capture(self):
        return self._captured

    @capture.setter
    def capture(self, captured):
        self._captured = captured

    @property
    def move_directions(self):
        return self._moves

    def __str__(self):
        return self._string_value

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(self, other.__class__):
            return self.__dict__ == other.__dict__
        return False

