import copy
import re
from piece.pawn import Pawn
from piece.rook import Rook
from piece.knight import Knight
from piece.bishop import Bishop
from piece.queen import Queen
from piece.king import King
from piece.color import Color
from piece.move_direction import MoveDirection


class FenError(Exception):
    """
    Base exception for fen string errors
    """
    pass


class FenIncorrectFormatError(FenError):
    """
    Invalid format exception
    """
    pass


class Fen:
    """
    Class used to parse FEN strings.
    """

    def __init__(self, fen=None):
        """
        Initialize fen object
        :param fen: string
            Valid FEN string
        """
        default_fen = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq -'
        fen = fen if fen else default_fen

        # Basic validation
        pattern = r'([rnbqkRNBQK1-8]+\/)([rnbqkpRNBQKP1-8]+\/){6}([rnbqkRNBQK1-8]+)\s[bw]\s(-|K?Q?k?q?)\s(-|[a-h][36])'
        if not re.match(pattern, fen):
            raise FenIncorrectFormatError('Invalid formatted fen. Valid example: ' + default_fen)

        fen_pieces = re.split(r'\s+', fen)

        self._board = self._parse_board(fen_pieces[0])
        self._current_player = Color.WHITE if fen_pieces[1].lower() == 'w' else Color.BLACK
        self._black_castle = self._parse_castle(fen_pieces[2], Color.BLACK)
        self._white_castle = self._parse_castle(fen_pieces[2], Color.WHITE)
        self._en_passant_position = None if fen_pieces[3] == '-' else fen_pieces[3]

    @property
    def board(self):
        return copy.copy(self._board)

    @property
    def current_player(self):
        return self._current_player

    @property
    def black_castle(self):
        return copy.copy(self._black_castle)

    @property
    def white_castle(self):
        return copy.copy(self._white_castle)

    @property
    def en_passant_position(self):
        return self._en_passant_position

    def _parse_castle(self, castle, color):
        """
        Parse the castle portion of a FEN string

        :param castle: string
            Castle portion of FEN
        :param color: Color
            Color enum
        :return: list
            List containing MoveDirection enum for the direction
            the king can castle in
        """
        if castle == '-':
            return []

        castle_directions = []
        pattern = {Color.WHITE: r'[KQ]', Color.BLACK: r'[kq]'}
        direction = {'k': MoveDirection.RIGHT, 'q': MoveDirection.LEFT}
        for letter in castle:
            match = re.search(pattern[color], letter)
            if match:
                castle_directions.append(direction[match.string.lower()])

        return castle_directions

    def _parse_board(self, fen_board):
        """
        Parse board portion of FEN string

        :param fen_board: string
            Board portion
        :return: dict
            Dictionary of position to Piece objects
        """
        board = {}
        rows = '87654321'
        columns = 'abcdefgh'
        piece_types = {'p': Pawn, 'r': Rook, 'n': Knight, 'b': Bishop, 'q': Queen, 'k': King}
        fen_rows = fen_board.split('/')
        for current_row, row in enumerate(fen_rows):
            current_column = 0
            for letter in row:
                match = re.match(r'[prnbqk]', letter, re.IGNORECASE)
                if match:
                    color = Color.WHITE if match.string.isupper() else Color.BLACK
                    letter = match.string.lower()
                    board[columns[current_column] + rows[current_row]] = piece_types[letter](color)
                    current_column += 1
                elif re.match(r'[1-8]', letter):
                    num = int(letter)
                    current_column += num

        return board
