class Player:
    def __init__(self):
        self._id = None
        self._name = None
        self._color = None

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def color(self):
        return self._color