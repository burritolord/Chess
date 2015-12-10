
class ChessHelper:
    @staticmethod
    def to_string(value):
        if isinstance(value, str):
            return value
        return value.decode('utf-8')