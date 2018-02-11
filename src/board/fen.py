import copy
import re
from src.piece.pawn import Pawn
from src.piece.rook import Rook
from src.piece.knight import Knight
from src.piece.bishop import Bishop
from src.piece.queen import Queen
from src.piece.king import King
from src.piece.color import Color
from src.piece.move_direction import MoveDirection


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

    @classmethod
    def generate_fen(cls, board, current_player, white_castle, black_castle, en_passant):
        # TODO add some validation
        rows = '87654321'
        columns = 'abcdefgh'
        possible_positions = [column + row for row in rows for column in columns]
        board_sections = ['' for _ in range(8)]

        count_between = 0
        for position, index in zip(possible_positions, [i for i in range(0, 8) for _ in range(0, 8)]):
            if board[position]:
                section_piece = "{}{}".format(count_between, board[position]) if count_between else str(board[position])
                board_sections[index] += section_piece
                count_between = 0
                continue

            # If reached the end of the row, reset count between and add the count to the board section
            if count_between == 7:
                board_sections[index] += str(count_between + 1)
                count_between = 0
            else:
                count_between += 1

        fen_board = '/'.join(board_sections)

        fen_current_player = 'w' if current_player == Color.WHITE else 'b'

        fen_white_castle = ''
        for direction in white_castle:
            fen_white_castle += 'K' if direction == MoveDirection.RIGHT else 'Q'

        fen_black_castle = ''
        for direction in black_castle:
            fen_black_castle += 'k' if direction == MoveDirection.RIGHT else 'q'

        fen_castle_info = '{}{}'.format(fen_white_castle, fen_black_castle)
        fen_castle_info = fen_castle_info if fen_castle_info else '-'

        fen_enpassant = en_passant if en_passant else '-'

        return '{} {} {} {}'.format(fen_board, fen_current_player, fen_castle_info, fen_enpassant)

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
