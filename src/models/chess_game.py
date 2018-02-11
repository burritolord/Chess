
# Maintain who's turn it is
# Maintain board state
# Check for end game: win, lose, draw
from src.board.chess_board import ChessBoard
from src.piece.move_direction import MoveDirection
from src.piece.color import Color
from src.board.fen import Fen
from src.models.game_score import GameScore
from src.db import db
from src.board.move_result import MoveResult


class ChessGame(db.Model):
    __tablename__ = 'game'

    id = db.Column(db.Integer, primary_key=True)
    fen = db.Column(db.String(100))
    white_player_id = db.Column(db.Integer, db.ForeignKey('players.id'))
    black_player_id = db.Column(db.Integer, db.ForeignKey('players.id'))
    game_over = db.Column(db.Boolean, default=False)

    white_player = db.relationship("Player", foreign_keys=white_player_id)
    black_player = db.relationship("Player", foreign_keys=black_player_id)
    score = db.relationship("GameScore", uselist=False, back_populates="game")

    def __init__(self, fen=None, **kwargs):
        """
        Generate a ChessGame object.

        :param fen: string
            Fen notation string to initialize game.
        :param kwargs:
        """
        super().__init__(**kwargs)

        fen = fen if Fen(fen) else Fen('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq -')
        self._board = ChessBoard(fen)

    def get_legal_moves(self, position):
        """
        Retrieve possible legal moves for a piece on a position.

        :param position: string
            Algebraic notation position.
        :return:
        """
        return self._board.get_legal_moves(position)

    def move_piece(self, start_position, end_position):
        """
        Move a piece from start_position to end_position.

        :param start_position:
        :param end_position:
        :return:
        """
        # TODO make sure in algebraic notation and UTF8
        current_fen = Fen(self.fen)
        current_player = current_fen.current_player
        move_result = MoveResult()

        move_result.update_positions = self._board.move_piece(start_position, end_position)

        # Determine which directions castling is possible for.
        next_player = Color.WHITE if current_player == Color.BLACK else Color.BLACK
        castle_info = {Color.BLACK: [], Color.WHITE: []}
        for color in [Color.WHITE, Color.BLACK]:
            for direction in [MoveDirection.LEFT, MoveDirection.RIGHT]:
                if self._board.can_castle(color, direction):
                    castle_info[color].append(direction)

        # Generate and save fen string after move
        next_fen = Fen()
        next_fen_str = next_fen.generate_fen(
            self._board.get_board_pieces(),
            next_player, castle_info[Color.WHITE],
            castle_info[Color.BLACK],
            self._board.get_enpassant_position()
        )
        self.fen = next_fen_str

        # If checkmate or draw, set game over flag. Also create game_score object and fill
        # the move results object.
        is_checkmate = self._board.is_checkmate(next_player)
        is_stalemate = self._board.is_stalemate(next_player)
        if is_checkmate or is_stalemate:
            self.game_over = True
            if is_checkmate:
                if current_player == Color.WHITE:
                    self.score = GameScore(game=self, white_score=1)
                    player_in_checkmate = self.black_player
                    player_in_checkmate.color = 'black'
                else:
                    self.score = GameScore(game=self, black_score=1)
                    player_in_checkmate = self.white_player
                    player_in_checkmate.color = 'white'
                move_result.king_in_checkmate = player_in_checkmate
            else:
                self.score = GameScore(game=self, white_score=0.5, black_score=0.5)
                move_result.draw = True

        # If it is check, add info to move_result.
        is_check = self._board.is_check(next_player)
        if is_check:
            if current_player == Color.WHITE:
                player_in_check = self.black_player
                player_in_check.color = 'black'
            else:
                player_in_check = self.white_player
                player_in_check.color = 'white'
            move_result.king_in_check = player_in_check

        move_result.pawn_promote_position = end_position if self._board.can_promote_pawn(end_position) else None

        return move_result

    @property
    def current_player(self):
        """
        Retrieve the current player

        :return Player:
            Player object with color set.
        """
        fen = Fen(self.fen)
        current_player_color = fen.current_player
        current_player = self.white_player if current_player_color == Color.WHITE else self.black_player
        # Dynamically add color field so UI can know player info and color.
        current_player.color = 'white' if current_player_color == Color.WHITE else 'black'

        return current_player

    def promote_piece(self, position, promotion_type):
        """
        Promote a pawn to another piece type.

        :param position: string
            Algebraic notation for pawn position.
        :param promotion_type: Type
            Value from Type enum
        :return:
        """
        self._board.promote_pawn(position, promotion_type)

    def get_winner(self):
        """
        Return winner of game.

        :return:
        """
        # Check if score obj exist. If so, return winner
        pass

if __name__ == '__main__':
    g1 = ChessGame(fen='fen stuff')
    db.session.add(g1)
    db.session.commit()