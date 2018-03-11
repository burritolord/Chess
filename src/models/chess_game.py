from src.board.chess_board import ChessBoard
from src.board.fen import Fen
from src.piece.move_direction import MoveDirection
from src.piece.color import Color
from src.piece.queen import Queen
from src.piece.bishop import Bishop
from src.piece.knight import Knight
from src.piece.rook import Rook
from src.models.game_score import GameScore
from src import db
from src.piece.type import Type
from src.utils.chess_helper import ChessHelper
from src.board.exception import *


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

    def to_dict(self):
        """
        Return dictionary version of object
        :return:
        """
        # TODO learn how to use JSONEncoder
        updated_positions = {}
        for position, piece in self.update_positions.items():
            if piece:
                updated_positions[position] = piece.to_dict()
            else:
                updated_positions[position] = piece

        king_in_check = self.king_in_check.to_dict() if self.king_in_check else self.king_in_check
        king_in_checkmate = self.king_in_checkmate.to_dict() if self.king_in_checkmate else self.king_in_checkmate



        return {
            'update_positions': updated_positions,
            'king_in_check': king_in_check,
            'king_in_checkmate': king_in_checkmate,
            'pawn_promote': self._pawn_promote,
            'draw': self.draw
        }

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
    def pawn_promote_info(self):
        # - [color]
        # - [promote_types]: Types of pieces the pawn can promote to
        return self._pawn_promote

    @pawn_promote_info.setter
    def pawn_promote_info(self, position):
        self._pawn_promote = position

    @property
    def draw(self):
        return self._draw

    @draw.setter
    def draw(self, draw):
        self._draw = draw

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(self, other.__class__):
            return self.__dict__ == other.__dict__
        return False


class ChessGame(db.Model):
    """
    Create new chess game
    """
    __tablename__ = 'game'

    id = db.Column(db.Integer, primary_key=True)
    fen = db.Column(db.String(100))
    white_player_id = db.Column(db.Integer, db.ForeignKey('players.id'))
    black_player_id = db.Column(db.Integer, db.ForeignKey('players.id'))
    is_over = db.Column(db.Boolean, default=False)

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

        self.fen = fen if fen else 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq -'
        fen = Fen(self.fen, validate=False)
        self._board = ChessBoard(fen)

    @property
    def board(self):
        return self._board

    @board.setter
    def board(self, board):
        self._board = board

    def get_legal_moves(self, position):
        """
        Retrieve possible legal moves for a piece on a position.

        :param position: string
            Algebraic notation position.
        :return:
        """
        try:
            ChessHelper.validate_position(position)
        except InvalidPositionError as e:
            # Maybe log error here
            # Reraise exception either way
            raise
        else:
            return self._board.get_legal_moves(position)

    def move_piece(self, start_position, end_position):
        """
        Move a piece from start_position to end_position.

        :param start_position:
        :param end_position:
        :return:
        """
        try:
            ChessHelper.validate_position(start_position)
            ChessHelper.validate_position(end_position)
        except InvalidPositionError as e:
            # Maybe log error here
            # Reraise exception either way
            raise
        else:
            current_fen = Fen(self.fen)
            current_player = current_fen.current_player
            next_player = Color.WHITE if current_player == Color.BLACK else Color.BLACK
            move_result = MoveResult()

            # If moving a pawn to the end of the board, dont update anything on the board.
            # Instead, just return the pawn promote info.
            if self.can_promote_pawn(start_position, end_position):
                player = self._get_player_by_color(current_player)
                promote_info = {
                    'player': player,
                    'promote_types': self.get_pawn_promote_types()
                }
                move_result.pawn_promote_info = promote_info
                return move_result

            move_result.update_positions = self._board.move_piece(start_position, end_position)

            # Determine which directions castling is possible for.
            castle_info = {Color.BLACK: [], Color.WHITE: []}
            for color in [Color.WHITE, Color.BLACK]:
                for direction in [MoveDirection.LEFT, MoveDirection.RIGHT]:
                    if self._board.can_castle(color, direction):
                        castle_info[color].append(direction)

            # Generate and save fen string after move
            next_fen = Fen()
            next_fen_str = next_fen.generate_fen(
                self._board.get_board_pieces(),
                next_player,
                castle_info[Color.WHITE],
                castle_info[Color.BLACK],
                self._board.get_enpassant_position()
            )
            self.fen = next_fen_str

            # If checkmate or draw, set game over flag. Also create game_score object and fill
            # the move results object.
            is_checkmate = self._board.is_checkmate(next_player)
            is_stalemate = self._board.is_stalemate(next_player)
            if is_checkmate or is_stalemate:
                self.is_over = True
                if is_checkmate:
                    if current_player == Color.WHITE:
                        self.score = GameScore(game=self, white_score=1)
                        player_in_checkmate = self.black_player
                        player_in_checkmate.color = Color.BLACK
                    else:
                        self.score = GameScore(game=self, black_score=1)
                        player_in_checkmate = self.white_player
                        player_in_checkmate.color = Color.WHITE
                    move_result.king_in_checkmate = player_in_checkmate
                else:
                    self.score = GameScore(game=self, white_score=0.5, black_score=0.5)
                    move_result.draw = True

            # If it is check, add info to move_result.
            is_check = self._board.is_check(next_player)
            if is_check:
                if current_player == Color.WHITE:
                    player_in_check = self._get_player_by_color(Color.BLACK)
                else:
                    player_in_check = self._get_player_by_color(Color.WHITE)
                move_result.king_in_check = player_in_check

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
        if current_player:
            current_player.color = Color.WHITE if current_player_color == Color.WHITE else Color.BLACK

        return current_player

    def promote_pawn(self, start_position, end_position, piece_type):
        """
        Promote a pawn to another piece type.

        :param start_position: string
            Algebraic notation for pawn position.
        :param end_position: string
            Algebraic notation for destination position.
        :param piece_type: Type
            Value from Type enum
        :return:
        """
        try:
            ChessHelper.validate_position(start_position)
            ChessHelper.validate_position(end_position)
        except InvalidPositionError as e:
            # Maybe log error here
            # Reraise exception either way
            raise
        else:
            if piece_type not in self.get_pawn_promote_types():
                raise PieceTypeError(piece_type, 'Cannot promote pawn to supplied piece type')
            if self._board[start_position] is None:
                raise EmptyPositionError(start_position)
            # TODO confirm pawn on second to last row

            piece = self._board[start_position]
            piece_class = {
                Type.ROOK: Rook,
                Type.KNIGHT: Knight,
                Type.BISHOP: Bishop,
                Type.QUEEN: Queen
            }
            self._board[start_position] = piece_class[piece_type](piece.color)

            return self.move_piece(start_position, end_position)

    def get_winner(self):
        """
        Return winner of game.

        :return:
        """
        # Check if score obj exist. If so, return winner
        pass

    @classmethod
    def get_pawn_promote_types(cls):
        """
        Retrieve the piece types a pawn can promote to.

        :return: Type[]
        """
        return [Type.ROOK, Type.KNIGHT, Type.BISHOP, Type.QUEEN]

    def can_promote_pawn(self, start_position, end_position):
        """
        Test if pawn promotion is possible for the provided position.

        :param start_position: string
            Algebraic notation position.
        :param end_position: string
            Algebraic notation position.
        :return:
        """
        try:
            ChessHelper.validate_position(start_position)
            ChessHelper.validate_position(end_position)
        except InvalidPositionError as e:
            # Maybe log error here
            # Reraise exception either way
            raise
        else:
            if self._board[start_position] is None:
                return False

            piece = self._board[start_position]
            if piece.type != Type.PAWN:
                return False

            _, start_row = self._board.position_to_row_and_column(start_position, piece.color)
            _, end_row = self._board.position_to_row_and_column(end_position, piece.color)
            if start_row == self._board.get_dimension() - 2 and end_row == self._board.get_dimension() - 1:
                return True

            return False

    def save_to_db(self):
        """
        Save game to db.

        :return:
        """
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        """
        Delete this game from the db.

        :return:
        """
        db.session.delete(self)
        db.session.commit()

    def to_dict(self):
        """
        Return dictionary for game.
        :return:
        """
        current_player = self.current_player
        white_player = self.white_player
        black_player = self.black_player

        return {
            'game_id': self.id,
            'current_player': current_player.to_dict() if current_player else None,
            'white_player': white_player.to_dict() if white_player else None,
            'black_player': black_player.to_dict() if black_player else None,
            'game_over': self.is_over,
            'board': {position: piece.to_dict() for position, piece in self.board.get_board_pieces().items() if piece}
        }


    @classmethod
    def load_by_id(cls, game_id):
        game = cls.query.get(game_id)
        if game:
            game.board = ChessBoard(Fen(game.fen))
        return game

    def _get_player_by_color(self, color):
        """
        Retrieve the player associated with the provided color.

        :param color: Color
        :return: Player
        """
        if color == Color.WHITE:
            player = self.white_player
            player.color = Color.WHITE
        else:
            player = self.black_player
            player.color = Color.BLACK

        return player

    def __str__(self):
        return str(self._board)


if __name__ == '__main__':
    g1 = ChessGame()
    # db.session.add(g1)
    # db.session.commit()
