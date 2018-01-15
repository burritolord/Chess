
# Maintain who's turn it is
# Maintain board state
# Check for end game: win, lose, draw
from board.chess_board import ChessBoard
from piece.color import Color
from game.player import Player


class ChessGame:

    def __init__(self):
        self._id = None
        self._board = ChessBoard()
        self._current_player = Color.WHITE
        self._game_over = False
        self._white_player_id = None
        self._black_player_id = None

    def get_legal_moves(self, position):
        return self._board.get_legal_moves(position)

    def is_game_over(self):
        stalemate = self._board.is_stalemate(self._current_player)
        checkmate = self._board.is_checkmate(self._current_player)
        pass

    def move_piece(self, start_position, end_position):
        """

        :param start_position:
        :param end_position:
        :return:
        """
        #TODO make sure in algebraic notation and UTF8
        self._board.move_piece(start_position, end_position)
        self._current_player = Color.WHITE if self._current_player == Color.BLACK else Color.WHITE

        # Return object of some sort indicating what happened and what can happen
        # - Pieces removed from board
        # - King in check
        # - Piece promotion available
        # - Checkmate
        # - Draw

    def load(self, game_id):
        pass

    @property
    def current_player(self):
        """

        :return Player:
        """
        return self._current_player

    def promote_piece(self, position, piece_type):
        pass

    def get_game_state(self):
        """
        Return
        :return:
        """
        pass
        # [state]: InProgress, CheckMate, Check, Draw
        # [king]: color of king in check or checkmate
        # [winner]: Player id, player name, player color


