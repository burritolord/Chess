from piece.Type import Type


class BoardError(Exception):
    """
    Base exception for errors raised by board
    """
    pass


class PieceTypeError(BoardError):
    def __init__(self, piece_type, msg=None):
        """
        Exception to be used when an action cannot be performed on piece type

        :param piece_type: Type
            Piece type
        :param msg: str
            Message to display
        """
        if not msg and isinstance(piece_type, Type):
            msg = 'Invalid action for piece type: {}'.format(piece_type.name)
        super(PieceTypeError, self).__init__(msg)
        self._piece_type = piece_type


class EmptyPositionError(BoardError):
    def __init__(self, position, msg=None):
        """
        Exception to be used when position is empty but expected a piece to be present.

        :param position: str
            Algebraic notation position
        :param msg: str
            Message to display
        """
        if not msg:
            msg = 'No piece exist on position: {}'.format(position)
        super(EmptyPositionError, self).__init__(msg)
        self._position = position


class IncorrectPositionError(BoardError):
    def __init__(self, piece_type, position, msg=None):
        """
        Exception to be used when piece is on the incorrect position for the action being performed

        :param piece_type: Type
            Piece type
        :param position: str
            Algebraic notation position
        :param msg: str
            Message to display
        """
        if not msg and isinstance(piece_type, Type):
            msg = 'Invalid action for piece type: {} on position: {}'.format(piece_type.name, position)
        super(IncorrectPositionError, self).__init__(msg)
        self.piece_type = piece_type
        self._position = position


class InvalidPositionError(BoardError):
    def __init__(self, position, msg=None):
        """
        Exception to be used when an invalid position is being used

        :param position: str
            Algebraic notation position
        :param msg: str
            Message to display
        """
        if not msg:
            msg = 'Invalid position: {}'.format(position)
        super(InvalidPositionError, self).__init__(msg)
        self._position = position


class InvalidIndexError(BoardError):
    def __init__(self, index, msg=None):
        """
        Exception to use when an invalid index is used

        :param index: int
            Index value
        :param msg: str
            Message to display
        """
        if not msg:
            msg = 'Invalid index: {}'.format(index)
        super(InvalidIndexError, self).__init__(msg)
        self._index = index
