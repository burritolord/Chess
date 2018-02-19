import unittest
from src.piece.pawn import Pawn
from src.piece.rook import Rook
from src.piece.knight import Knight
from src.piece.bishop import Bishop
from src.piece.queen import Queen
from src.piece.king import King
from src.piece.color import Color
from src.board.fen import Fen
from src.board.fen import FenIncorrectFormatError
from src.piece.move_direction import MoveDirection


class FenTest(unittest.TestCase):

    def test_empty_fen(self):
        """
        Create fen object without supplying a FEN string
        Expect default chess board
        :return:
        """
        fen = Fen()

        expected_board = {
            'a1': Rook(Color.WHITE), 'b1': Knight(Color.WHITE), 'c1': Bishop(Color.WHITE), 'd1': Queen(Color.WHITE),
            'e1': King(Color.WHITE), 'f1': Bishop(Color.WHITE), 'g1': Knight(Color.WHITE), 'h1': Rook(Color.WHITE),
            'a2': Pawn(Color.WHITE), 'b2': Pawn(Color.WHITE), 'c2': Pawn(Color.WHITE), 'd2': Pawn(Color.WHITE),
            'e2': Pawn(Color.WHITE), 'f2': Pawn(Color.WHITE), 'g2': Pawn(Color.WHITE), 'h2': Pawn(Color.WHITE),
            'a8': Rook(Color.BLACK), 'b8': Knight(Color.BLACK), 'c8': Bishop(Color.BLACK), 'd8': Queen(Color.BLACK),
            'e8': King(Color.BLACK), 'f8': Bishop(Color.BLACK), 'g8': Knight(Color.BLACK), 'h8': Rook(Color.BLACK),
            'a7': Pawn(Color.BLACK), 'b7': Pawn(Color.BLACK), 'c7': Pawn(Color.BLACK), 'd7': Pawn(Color.BLACK),
            'e7': Pawn(Color.BLACK), 'f7': Pawn(Color.BLACK), 'g7': Pawn(Color.BLACK), 'h7': Pawn(Color.BLACK),
        }
        self.assertEqual(expected_board, fen.board)

    def test_different_board_setups(self):
        """
        Create Fen object using empty board, middle game, end game
        Expect board config to match expected value
        :return:
        """
        # Empty board
        fen_str = '8/8/8/8/8/8/8/8 w - -'
        expected_board1 = {}
        fen = Fen(fen_str)
        self.assertEqual(expected_board1, fen.board)

        # Partial game
        fen_str = 'r2qkbnr/2pp1ppp/b1n5/1N2p3/4P1Q1/8/PPPP1PPP/R1B1K1NR w KQkq -'
        expected_board2 = {
            'a1': Rook(Color.WHITE), 'c1': Bishop(Color.WHITE), 'e1': King(Color.WHITE), 'g1': Knight(Color.WHITE),
            'h1': Rook(Color.WHITE), 'a2': Pawn(Color.WHITE), 'b2': Pawn(Color.WHITE), 'c2': Pawn(Color.WHITE),
            'd2': Pawn(Color.WHITE), 'f2': Pawn(Color.WHITE), 'g2': Pawn(Color.WHITE), 'h2': Pawn(Color.WHITE),
            'a8': Rook(Color.BLACK), 'd8': Queen(Color.BLACK), 'e8': King(Color.BLACK), 'f8': Bishop(Color.BLACK),
            'g8': Knight(Color.BLACK), 'h8': Rook(Color.BLACK),'c7': Pawn(Color.BLACK), 'd7': Pawn(Color.BLACK),
            'f7': Pawn(Color.BLACK), 'g7': Pawn(Color.BLACK), 'h7': Pawn(Color.BLACK), 'a6': Bishop(Color.BLACK),
            'c6': Knight(Color.BLACK), 'e5': Pawn(Color.BLACK), 'b5': Knight(Color.WHITE), 'e4': Pawn(Color.WHITE),
            'g4': Queen(Color.WHITE)
        }
        fen = Fen(fen_str)
        self.assertEqual(expected_board2, fen.board)

        # End game
        fen_str = '5rk1/7p/8/4p1p1/2nP4/2PB4/bP4QP/2K4R w - -'
        expected_board3 = {
            'c1': King(Color.WHITE), 'h1': Rook(Color.WHITE), 'b2': Pawn(Color.WHITE), 'g2': Queen(Color.WHITE),
            'h2': Pawn(Color.WHITE), 'c3': Pawn(Color.WHITE), 'd3': Bishop(Color.WHITE), 'd4': Pawn(Color.WHITE),
            'a2': Bishop(Color.BLACK), 'c4': Knight(Color.BLACK), 'e5': Pawn(Color.BLACK), 'g5': Pawn(Color.BLACK),
            'h7': Pawn(Color.BLACK), 'f8': Rook(Color.BLACK), 'g8': King(Color.BLACK)
        }
        fen = Fen(fen_str)
        self.assertEqual(expected_board3, fen.board)

    def test_fen_castle_values(self):
        """
        Create FEN string using different combinations for black and white castle
        Expect castle ability for each king to match provided value
        :return:
        """
        castle_values = ['KQ', 'Kk', 'Qq', 'kq', 'Kkq', 'KQk', '-']
        expected_castle = [
            {Color.WHITE: [MoveDirection.LEFT, MoveDirection.RIGHT], Color.BLACK: []},
            {Color.WHITE: [MoveDirection.RIGHT], Color.BLACK: [MoveDirection.LEFT]},
            {Color.WHITE: [MoveDirection.LEFT], Color.BLACK: [MoveDirection.RIGHT]},
            {Color.WHITE: [], Color.BLACK: [MoveDirection.LEFT, MoveDirection.RIGHT]},
            {Color.WHITE: [MoveDirection.RIGHT], Color.BLACK: [MoveDirection.LEFT, MoveDirection.RIGHT]},
            {Color.WHITE: [MoveDirection.LEFT, MoveDirection.RIGHT], Color.BLACK: [MoveDirection.LEFT]},
            {Color.WHITE: [], Color.BLACK: []}
        ]
        fen_str = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w {} -'
        for castle, expected in zip(castle_values, expected_castle):
            with self.subTest(castle=castle, expected=expected):
                fen = Fen(fen_str.format(castle))
                self.assertEqual(expected[Color.WHITE], fen.white_castle)
                self.assertEqual(expected[Color.BLACK], fen.black_castle)

    def test_fen_current_player(self):
        """
        Try using b, w, and - for current player in FEN string.
        Expect current user to match passed in value.
        :return:
        """
        current_player = {'w': Color.WHITE, 'b': Color.BLACK}
        fen_str = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR {} KQ -'
        for player, color in current_player.items():
            fen = Fen(fen_str.format(player))
            self.assertEqual(color, fen.current_player)

    def test_fen_en_passant(self):
        """
        Try various en passant squares including empty.
        Expect en passant value to match expected value.
        :return:
        """
        en_passant_positions = {'a3': 'a3', 'd6': 'd6', '-': None}
        fen_str = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQ {}'
        for position, expected in en_passant_positions.items():
            fen = Fen(fen_str.format(position))
            self.assertEqual(expected, fen.en_passant_position)

    def test_invalid_fen(self):
        """
        Try providing an invalid piece for each section of a FEN string.
        Expect exception to be thrown.
        :return:
        """
        # Enpassant square on row other than 3 or 6
        fen_str = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQ f5'
        with self.assertRaises(FenIncorrectFormatError) as context:
            fen = Fen(fen_str)

        # Incorrect value in board. Use 9 instead of 8
        fen_str = 'rnbqkbnr/pppppppp/9/8/8/8/PPPPPPPP/RNBQKBNR w KQ -'
        with self.assertRaises(FenIncorrectFormatError) as context:
            fen = Fen(fen_str)

        # wrong letter for current player. Use y
        fen_str = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR y KQ -'
        with self.assertRaises(FenIncorrectFormatError) as context:
            fen = Fen(fen_str)

        # Wrong letter in castle info. Use w
        fen_str = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQw -'
        with self.assertRaises(FenIncorrectFormatError) as context:
            fen = Fen(fen_str)
