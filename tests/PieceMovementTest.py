__author__ = 'nick.james'
import unittest
from board.ChessBoard import ChessBoard
from piece.King import King
from piece.Pawn import Pawn
from piece.Queen import Queen
from piece.Bishop import Bishop
from piece.Knight import Knight
from piece.Rook import Rook
from piece.Move import Move
from piece.MoveDirection import MoveDirection
from piece.Color import Color
from piece.Type import Type


class PieceMovementTest(unittest.TestCase):

    def setUp(self):
        self.piece_types = {
            Type.pawn: Pawn,
            Type.bishop: Bishop,
            Type.king: King,
            Type.knight: Knight,
            Type.queen: Queen,
            Type.rook: Rook
        }

    def test_move_forward(self):
        start_position = 'a1'
        end_position = 'a2'
        piece_types = {
            Type.pawn: Pawn,
            Type.king: King,
            Type.queen: Queen,
            Type.rook: Rook
        }

        for t, piece_class in piece_types.items():
            with self.subTest(t=t, piece_class=piece_class, start_position=start_position):
                board = ChessBoard(empty_board=True)
                board[start_position] = piece_class(Color.white)
                self.assertFalse(board[start_position].has_moved, 'Piece has never moved')

                board.move_piece(start_position, end_position)
                self.assertIsNone(board[start_position], 'There should no longer be a piece on square ' + start_position)
                self.assertIsInstance(board[end_position], piece_class, 'There should be a piece on square ' + end_position)
                self.assertTrue(board[end_position].has_moved, 'Piece has moved')

    def test_move_forward_right_diagonal(self):
        start_position = 'a1'
        end_position = 'b2'
        self.piece_types = {
            Type.pawn: Pawn,
            Type.bishop: Bishop,
            Type.king: King,
            Type.queen: Queen,
        }
        for t, piece_class in self.piece_types.items():
            with self.subTest(t=t, piece_class=piece_class, start_position=start_position):
                board = ChessBoard(empty_board=True)
                board[start_position] = piece_class(Color.white)
                self.assertFalse(board[start_position].has_moved, 'Piece has never moved')

                board.move_piece(start_position, end_position)
                self.assertIsNone(board[start_position], 'There should no longer be a piece on square ' + start_position)
                self.assertIsInstance(board[end_position], piece_class, 'There should be a piece on square ' + end_position)
                self.assertTrue(board[end_position].has_moved, 'Piece has moved')

    def test_move_right(self):
        start_position = 'a1'
        end_position = 'b1'
        self.piece_types = {
            Type.king: King,
            Type.queen: Queen,
            Type.rook: Rook
        }
        for t, piece_class in self.piece_types.items():
            with self.subTest(t=t, piece_class=piece_class, start_position=start_position):
                board = ChessBoard(empty_board=True)
                board[start_position] = piece_class(Color.white)
                self.assertFalse(board[start_position].has_moved, 'Piece has never moved')

                board.move_piece(start_position, end_position)
                self.assertIsNone(board[start_position], 'There should no longer be a piece on square ' + start_position)
                self.assertIsInstance(board[end_position], piece_class, 'There should be a piece on square ' + end_position)
                self.assertTrue(board[end_position].has_moved, 'Piece has moved')

    def test_move_back_right_diagonal(self):
        start_position = 'a2'
        end_position = 'b1'
        self.piece_types = {
            Type.king: King,
            Type.queen: Queen,
            Type.bishop: Bishop
        }
        for t, piece_class in self.piece_types.items():
            with self.subTest(t=t, piece_class=piece_class, start_position=start_position):
                board = ChessBoard(empty_board=True)
                board[start_position] = piece_class(Color.white)
                self.assertFalse(board[start_position].has_moved, 'Piece has never moved')

                board.move_piece(start_position, end_position)
                self.assertIsNone(board[start_position], 'There should no longer be a piece on square ' + start_position)
                self.assertIsInstance(board[end_position], piece_class, 'There should be a piece on square ' + end_position)
                self.assertTrue(board[end_position].has_moved, 'Piece has moved')

    def test_move_backwards(self):
        start_position = 'a2'
        end_position = 'a1'
        self.piece_types = {
            Type.king: King,
            Type.queen: Queen,
            Type.rook: Rook
        }
        for t, piece_class in self.piece_types.items():
            with self.subTest(t=t, piece_class=piece_class, start_position=start_position):
                board = ChessBoard(empty_board=True)
                board[start_position] = piece_class(Color.white)
                self.assertFalse(board[start_position].has_moved, 'Piece has never moved')

                board.move_piece(start_position, end_position)
                self.assertIsNone(board[start_position], 'There should no longer be a piece on square ' + start_position)
                self.assertIsInstance(board[end_position], piece_class, 'There should be a piece on square ' + end_position)
                self.assertTrue(board[end_position].has_moved, 'Piece has moved')

    def test_move_back_left_diagonal(self):
        start_position = 'b2'
        end_position = 'a1'
        self.piece_types = {
            Type.king: King,
            Type.queen: Queen,
            Type.bishop: Bishop
        }
        for t, piece_class in self.piece_types.items():
            with self.subTest(t=t, piece_class=piece_class, start_position=start_position):
                board = ChessBoard(empty_board=True)
                board[start_position] = piece_class(Color.white)
                self.assertFalse(board[start_position].has_moved, 'Piece has never moved')

                board.move_piece(start_position, end_position)
                self.assertIsNone(board[start_position], 'There should no longer be a piece on square ' + start_position)
                self.assertIsInstance(board[end_position], piece_class, 'There should be a piece on square ' + end_position)
                self.assertTrue(board[end_position].has_moved, 'Piece has moved')

    def test_move_left(self):
        start_position = 'b1'
        end_position = 'a1'
        self.piece_types = {
            Type.king: King,
            Type.queen: Queen,
            Type.rook: Rook
        }
        for t, piece_class in self.piece_types.items():
            with self.subTest(t=t, piece_class=piece_class, start_position=start_position):
                board = ChessBoard(empty_board=True)
                board[start_position] = piece_class(Color.white)
                self.assertFalse(board[start_position].has_moved, 'Piece has never moved')

                board.move_piece(start_position, end_position)
                self.assertIsNone(board[start_position], 'There should no longer be a piece on square ' + start_position)
                self.assertIsInstance(board[end_position], piece_class, 'There should be a piece on square ' + end_position)
                self.assertTrue(board[end_position].has_moved, 'Piece has moved')

    def test_move_forward_left_diagonal(self):
        start_position = 'b1'
        end_position = 'a2'
        self.piece_types = {
            Type.king: King,
            Type.queen: Queen,
            Type.bishop: Bishop
        }
        for t, piece_class in self.piece_types.items():
            with self.subTest(t=t, piece_class=piece_class, start_position=start_position):
                board = ChessBoard(empty_board=True)
                board[start_position] = piece_class(Color.white)
                self.assertFalse(board[start_position].has_moved, 'Piece has never moved')

                board.move_piece(start_position, end_position)
                self.assertIsNone(board[start_position], 'There should no longer be a piece on square ' + start_position)
                self.assertIsInstance(board[end_position], piece_class, 'There should be a piece on square ' + end_position)
                self.assertTrue(board[end_position].has_moved, 'Piece has moved')
    # ------------------------------------------------------------------------------------------------------------------------------------------------
    def test_pawn_possible_moves(self):
        start_positions = {'a1': ['a2', 'a3'],
                           'a8': [],
                           'h1': ['h2', 'h3'],
                           'h8': [],
                           'd4': ['d5', 'd6']
                           }
        for start_position, expected_possible_moves in start_positions.items():
            with self.subTest(start_position=start_position, expected_possible_moves=expected_possible_moves):
                board = ChessBoard(empty_board=True)
                board[start_position] = Pawn(Color.white)
                possible_moves = board.get_possible_moves(start_position)

                message = 'Expected move count does not match actual move count'
                self.assertEqual(len(start_positions[start_position]), len(possible_moves), message)
                for position in expected_possible_moves:
                    self.assertIn(position, possible_moves, '"' + position + '" should one of the possible moves')

    def test_pawn_diagonal_diff_color_moves(self):
        # Test diagonal move when a piece of the opposite color is present
        board = ChessBoard(empty_board=True)
        start_position = 'b1'
        board[start_position] = Pawn(Color.white)
        board['c2'] = Bishop(Color.black)
        expected_possible_moves = ['b2', 'b3', 'c2']
        possible_moves = board.get_possible_moves(start_position)

        message = 'Expected move count does not match actual move count'
        self.assertEqual(len(expected_possible_moves), len(possible_moves), message)
        for position in expected_possible_moves:
            self.assertIn(position, possible_moves, '"' + position + '" should one of the possible moves')

        board['a2'] = Rook(Color.black)
        expected_possible_moves = ['b2', 'b3', 'a2', 'c2']
        possible_moves = board.get_possible_moves(start_position)

        message = 'Expected move count does not match actual move count'
        self.assertEqual(len(expected_possible_moves), len(possible_moves), message)
        for position in expected_possible_moves:
            self.assertIn(position, possible_moves, '"' + position + '" should one of the possible moves')

    def test_pawn_diagonal_same_color_moves(self):
        board = ChessBoard(empty_board=True)
        start_position = 'b1'
        board[start_position] = Pawn(Color.white)
        board['c2'] = Bishop(Color.white)
        expected_possible_moves = ['b2', 'b3']
        possible_moves = board.get_possible_moves(start_position)

        message = 'Expected move count does not match actual move count'
        self.assertEqual(len(expected_possible_moves), len(possible_moves), message)
        for position in expected_possible_moves:
            self.assertIn(position, possible_moves, '"' + position + '" should one of the possible moves')

    def test_rook_possible_moves(self):
        start_positions = {'a1': ['a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h1'],
                           'a8': ['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'b8', 'c8', 'd8', 'e8', 'f8', 'g8', 'h8'],
                           'h1': ['h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'h8', 'a1', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1'],
                           'h8': ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'a8', 'b8', 'c8', 'd8', 'e8', 'f8', 'g8'],
                           'd4': ['d1', 'd2', 'd3', 'd5', 'd6', 'd7', 'd8', 'a4', 'b4', 'c4', 'e4', 'f4', 'g4', 'h4']
                           }
        for start_position, expected_possible_moves in start_positions.items():
            with self.subTest(start_position=start_position, expected_possible_moves=expected_possible_moves):
                board = ChessBoard(empty_board=True)
                board[start_position] = Rook(Color.white)
                possible_moves = board.get_possible_moves(start_position)

                message = 'Expected move count does not match actual move count'
                self.assertEqual(len(start_positions[start_position]), len(possible_moves), message)
                for position in expected_possible_moves:
                    self.assertIn(position, possible_moves, '"' + position + '" should one of the possible moves')

    def test_knight_possible_moves(self):
        start_positions = {'a1': ['c2', 'b3'],
                           'a8': ['c7', 'b6'],
                           'h1': ['f2', 'g3'],
                           'h8': ['f7', 'g6'],
                           'd4': ['b3', 'b5', 'c6', 'e6', 'f5', 'f3', 'e2', 'c2']
                           }
        for start_position, expected_possible_moves in start_positions.items():
            with self.subTest(start_position=start_position, expected_possible_moves=expected_possible_moves):
                board = ChessBoard(empty_board=True)
                board[start_position] = Knight(Color.white)
                possible_moves = board.get_possible_moves(start_position)

                message = 'Expected move count does not match actual move count'
                self.assertEqual(len(start_positions[start_position]), len(possible_moves), message)
                for position in expected_possible_moves:
                    self.assertIn(position, possible_moves, '"' + position + '" should one of the possible moves')

    def test_bishop_possible_moves(self):
        start_positions = {'a1': ['b2', 'c3', 'd4', 'e5', 'f6', 'g7', 'h8'],
                           'a8': ['b7', 'c6', 'd5', 'e4', 'f3', 'g2', 'h1'],
                           'h1': ['a8', 'b7', 'c6', 'd5', 'e4', 'f3', 'g2'],
                           'h8': ['a1', 'b2', 'c3', 'd4', 'e5', 'f6', 'g7'],
                           'd4': ['a7', 'b6', 'c5', 'e3', 'f2', 'g1', 'a1', 'b2', 'c3', 'e5', 'f6', 'g7', 'h8']
                           }
        for start_position, expected_possible_moves in start_positions.items():
            with self.subTest(start_position=start_position, expected_possible_moves=expected_possible_moves):
                board = ChessBoard(empty_board=True)
                board[start_position] = Bishop(Color.white)
                possible_moves = board.get_possible_moves(start_position)

                message = 'Expected move count does not match actual move count'
                self.assertEqual(len(start_positions[start_position]), len(possible_moves), message)
                for position in expected_possible_moves:
                    self.assertIn(position, possible_moves, '"' + position + '" should one of the possible moves')

    def test_queen_possible_moves(self):
        pass

    def test_king_possible_moves(self):
        pass

    def test_check(self):
        pass

if __name__ == '__main__':
    unittest.main()