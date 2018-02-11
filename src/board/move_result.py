class MoveResult:
    """
    Contain info on results of performing a move.
    """

    def __init__(self):
        self._update_positions = {}
        self._king_in_check = None
        self._king_in_checkmate = None
        self._pawn_promote = None
        self._draw = False

    @property
    def update_positions(self):
        return self._update_positions

    @update_positions.setter
    def update_positions(self, positions):
        self._update_positions = positions

    @property
    def king_in_check(self):
        return self._king_in_check

    @king_in_check.setter
    def king_in_check(self, king):
        self._king_in_check = king

    @property
    def king_in_checkmate(self):
        return self._king_in_checkmate

    @king_in_checkmate.setter
    def king_in_checkmate(self, king):
        self._king_in_checkmate = king

    @property
    def pawn_promote_position(self):
        return self._pawn_promote

    @pawn_promote_position.setter
    def pawn_promote_position(self, position):
        self._pawn_promote = position

    @property
    def draw(self):
        return self._draw

    @draw.setter
    def draw(self, draw):
        self._draw = draw
