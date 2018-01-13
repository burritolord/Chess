import unittest
from board.ChessBoard import ChessBoard
from piece.King import King
from piece.Pawn import Pawn
from piece.Queen import Queen
from piece.Bishop import Bishop
from piece.Knight import Knight
from piece.Rook import Rook
from piece.Color import Color
from piece.Type import Type


class PieceMovementTest(unittest.TestCase):
    """
    Test piece movement.
    """

    def test_move_forward(self):
        """
        Move a piece of every type one square forward.
        Expected result is that the piece no longer exist on the starting square, but on the ending square.
        :return:
        """
        start_positions = ['a1', 'h8']
        end_positions = ['a2', 'h7']
        piece_colors = [Color.white, Color.black]
        piece_types = {
            Type.pawn: Pawn,
            Type.king: King,
            Type.queen: Queen,
            Type.rook: Rook
        }

        for start, end, color in zip(start_positions, end_positions, piece_colors):
            for t, piece_class in piece_types.items():
                with self.subTest(t=t, piece_class=piece_class, start=start, end=end, color=color):
                    board = ChessBoard(empty_board=True)
                    board[start] = piece_class(color)
                    self.assertFalse(board[start].has_moved, 'Piece has never moved')

                    move_result = board.move_piece(start, end)
                    self.assertIsNone(board[start], 'There should no longer be a piece on square ' + start)
                    self.assertIsInstance(board[end], piece_class, 'There should be a piece on square ' + end)
                    self.assertTrue(board[end].has_moved, 'Piece has moved')

                    expected_result = {start: None, end: piece_class(color)}
                    self.assertIn(start, move_result, 'Starting position should be in move_result')
                    self.assertIn(end, move_result, 'Ending position should be in move_result')
                    self.assertEqual(expected_result[start], move_result[start], 'Start position should be empty')
                    self.assertEqual(expected_result[end].type, move_result[end].type, 'Piece type should match')
                    self.assertEqual(expected_result[end].color, move_result[end].color, 'Piece color should match')

    def test_move_forward_right_diagonal(self):
        """
        Move a piece of every type one square in the forward right diagonal direction.
        Expected result is that the piece no longer exist on the starting square, but on the ending square.
        :return:
        """
        start_positions = ['a1', 'h8']
        end_positions = ['b2', 'g7']
        piece_colors = [Color.white, Color.black]
        piece_types = {
            Type.bishop: Bishop,
            Type.king: King,
            Type.queen: Queen,
        }
        for start, end, color in zip(start_positions, end_positions, piece_colors):
            for t, piece_class in piece_types.items():
                with self.subTest(t=t, piece_class=piece_class, start=start, end=end, color=color):
                    board = ChessBoard(empty_board=True)
                    board[start] = piece_class(color)
                    self.assertFalse(board[start].has_moved, 'Piece has never moved')

                    move_result = board.move_piece(start, end)
                    self.assertIsNone(board[start], 'There should no longer be a piece on square ' + start)
                    self.assertIsInstance(board[end], piece_class, 'There should be a piece on square ' + end)
                    self.assertTrue(board[end].has_moved, 'Piece has moved')

                    expected_result = {start: None, end: piece_class(color)}
                    self.assertIn(start, move_result, 'Starting position should be in move_result')
                    self.assertIn(end, move_result, 'Ending position should be in move_result')
                    self.assertEqual(expected_result[start], move_result[start], 'Start position should be empty')
                    self.assertEqual(expected_result[end].type, move_result[end].type, 'Piece type should match')
                    self.assertEqual(expected_result[end].color, move_result[end].color, 'Piece color should match')

    def test_move_right(self):
        """
        Move a piece of every type one square to the right.
        Expected result is that the piece no longer exist on the starting square, but on the ending square.
        :return:
        """
        start_positions = ['a1', 'h8']
        end_positions = ['b1', 'g8']
        piece_colors = [Color.white, Color.black]
        piece_types = {
            Type.king: King,
            Type.queen: Queen,
            Type.rook: Rook
        }
        for start, end, color in zip(start_positions, end_positions, piece_colors):
            for t, piece_class in piece_types.items():
                with self.subTest(t=t, piece_class=piece_class, start=start, end=end, color=color):
                    board = ChessBoard(empty_board=True)
                    board[start] = piece_class(color)
                    self.assertFalse(board[start].has_moved, 'Piece has never moved')

                    move_result = board.move_piece(start, end)
                    self.assertIsNone(board[start], 'There should no longer be a piece on square ' + start)
                    self.assertIsInstance(board[end], piece_class, 'There should be a piece on square ' + end)
                    self.assertTrue(board[end].has_moved, 'Piece has moved')

                    expected_result = {start: None, end: piece_class(color)}
                    self.assertIn(start, move_result, 'Starting position should be in move_result')
                    self.assertIn(end, move_result, 'Ending position should be in move_result')
                    self.assertEqual(expected_result[start], move_result[start], 'Start position should be empty')
                    self.assertEqual(expected_result[end].type, move_result[end].type, 'Piece type should match')
                    self.assertEqual(expected_result[end].color, move_result[end].color, 'Piece color should match')

    def test_move_back_right_diagonal(self):
        """
        Move a piece of every type one square in the back right diagonal direction.
        Expected result is that the piece no longer exist on the starting square, but on the ending square.
        :return:
        """
        start_positions = ['a2', 'h7']
        end_positions = ['b1', 'g8']
        piece_colors = [Color.white, Color.black]
        piece_types = {
            Type.king: King,
            Type.queen: Queen,
            Type.bishop: Bishop
        }
        for start, end, color in zip(start_positions, end_positions, piece_colors):
            for t, piece_class in piece_types.items():
                with self.subTest(t=t, piece_class=piece_class, start=start, end=end, color=color):
                    board = ChessBoard(empty_board=True)
                    board[start] = piece_class(color)
                    self.assertFalse(board[start].has_moved, 'Piece has never moved')

                    move_result = board.move_piece(start, end)
                    self.assertIsNone(board[start], 'There should no longer be a piece on square ' + start)
                    self.assertIsInstance(board[end], piece_class, 'There should be a piece on square ' + end)
                    self.assertTrue(board[end].has_moved, 'Piece has moved')

                    expected_result = {start: None, end: piece_class(color)}
                    self.assertIn(start, move_result, 'Starting position should be in move_result')
                    self.assertIn(end, move_result, 'Ending position should be in move_result')
                    self.assertEqual(expected_result[start], move_result[start], 'Start position should be empty')
                    self.assertEqual(expected_result[end].type, move_result[end].type, 'Piece type should match')
                    self.assertEqual(expected_result[end].color, move_result[end].color, 'Piece color should match')

    def test_move_backward(self):
        """
        Move a piece of every type one square backward.
        Expected result is that the piece no longer exist on the starting square, but on the ending square.
        :return:
        """
        start_positions = ['a2', 'h7']
        end_positions = ['a1', 'h8']
        piece_colors = [Color.white, Color.black]
        piece_types = {
            Type.king: King,
            Type.queen: Queen,
            Type.rook: Rook
        }
        for start, end, color in zip(start_positions, end_positions, piece_colors):
            for t, piece_class in piece_types.items():
                with self.subTest(t=t, piece_class=piece_class, start=start, end=end, color=color):
                    board = ChessBoard(empty_board=True)
                    board[start] = piece_class(color)
                    self.assertFalse(board[start].has_moved, 'Piece has never moved')

                    move_result = board.move_piece(start, end)
                    self.assertIsNone(board[start], 'There should no longer be a piece on square ' + start)
                    self.assertIsInstance(board[end], piece_class, 'There should be a piece on square ' + end)
                    self.assertTrue(board[end].has_moved, 'Piece has moved')

                    expected_result = {start: None, end: piece_class(color)}
                    self.assertIn(start, move_result, 'Starting position should be in move_result')
                    self.assertIn(end, move_result, 'Ending position should be in move_result')
                    self.assertEqual(expected_result[start], move_result[start], 'Start position should be empty')
                    self.assertEqual(expected_result[end].type, move_result[end].type, 'Piece type should match')
                    self.assertEqual(expected_result[end].color, move_result[end].color, 'Piece color should match')

    def test_move_back_left_diagonal(self):
        """
        Move a piece of every type one square in the back left diagonal direction.
        Expected result is that the piece no longer exist on the starting square, but on the ending square.
        :return:
        """
        start_positions = ['b2', 'g7']
        end_positions = ['a1', 'h8']
        piece_colors = [Color.white, Color.black]
        piece_types = {
            Type.king: King,
            Type.queen: Queen,
            Type.bishop: Bishop
        }
        for start, end, color in zip(start_positions, end_positions, piece_colors):
            for t, piece_class in piece_types.items():
                with self.subTest(t=t, piece_class=piece_class, start=start, end=end, color=color):
                    board = ChessBoard(empty_board=True)
                    board[start] = piece_class(color)
                    self.assertFalse(board[start].has_moved, 'Piece has never moved')

                    move_result = board.move_piece(start, end)
                    self.assertIsNone(board[start], 'There should no longer be a piece on square ' + start)
                    self.assertIsInstance(board[end], piece_class, 'There should be a piece on square ' + end)
                    self.assertTrue(board[end].has_moved, 'Piece has moved')

                    expected_result = {start: None, end: piece_class(color)}
                    self.assertIn(start, move_result, 'Starting position should be in move_result')
                    self.assertIn(end, move_result, 'Ending position should be in move_result')
                    self.assertEqual(expected_result[start], move_result[start], 'Start position should be empty')
                    self.assertEqual(expected_result[end].type, move_result[end].type, 'Piece type should match')
                    self.assertEqual(expected_result[end].color, move_result[end].color, 'Piece color should match')

    def test_move_left(self):
        """
        Move a piece of every type one square left.
        Expected result is that the piece no longer exist on the starting square, but on the ending square.
        :return:
        """
        start_positions = ['b1', 'g8']
        end_positions = ['a1', 'h8']
        piece_colors = [Color.white, Color.black]
        piece_types = {
            Type.king: King,
            Type.queen: Queen,
            Type.rook: Rook
        }
        for start, end, color in zip(start_positions, end_positions, piece_colors):
            for t, piece_class in piece_types.items():
                with self.subTest(t=t, piece_class=piece_class, start=start, end=end, color=color):
                    board = ChessBoard(empty_board=True)
                    board[start] = piece_class(color)
                    self.assertFalse(board[start].has_moved, 'Piece has never moved')

                    move_result = board.move_piece(start, end)
                    self.assertIsNone(board[start], 'There should no longer be a piece on square ' + start)
                    self.assertIsInstance(board[end], piece_class, 'There should be a piece on square ' + end)
                    self.assertTrue(board[end].has_moved, 'Piece has moved')

                    expected_result = {start: None, end: piece_class(color)}
                    self.assertIn(start, move_result, 'Starting position should be in move_result')
                    self.assertIn(end, move_result, 'Ending position should be in move_result')
                    self.assertEqual(expected_result[start], move_result[start], 'Start position should be empty')
                    self.assertEqual(expected_result[end].type, move_result[end].type, 'Piece type should match')
                    self.assertEqual(expected_result[end].color, move_result[end].color, 'Piece color should match')

    def test_move_forward_left_diagonal(self):
        """
        Move a piece of every type that can move diagonally one square in the forward left diagonal direction.
        Expected result is that the piece no longer exist on the starting square, but on the ending square.
        :return:
        """
        start_positions = ['b1', 'g8']
        end_positions = ['a2', 'h7']
        piece_colors = [Color.white, Color.black]
        piece_types = {
            Type.king: King,
            Type.queen: Queen,
            Type.bishop: Bishop
        }
        for start, end, color in zip(start_positions, end_positions, piece_colors):
            for t, piece_class in piece_types.items():
                with self.subTest(t=t, piece_class=piece_class, start=start, end=end, color=color):
                    board = ChessBoard(empty_board=True)
                    board[start] = piece_class(color)
                    self.assertFalse(board[start].has_moved, 'Piece has never moved')

                    move_result = board.move_piece(start, end)
                    self.assertIsNone(board[start], 'There should no longer be a piece on square ' + start)
                    self.assertIsInstance(board[end], piece_class, 'There should be a piece on square ' + end)
                    self.assertTrue(board[end].has_moved, 'Piece has moved')

                    expected_result = {start: None, end: piece_class(color)}
                    self.assertIn(start, move_result, 'Starting position should be in move_result')
                    self.assertIn(end, move_result, 'Ending position should be in move_result')
                    self.assertEqual(expected_result[start], move_result[start], 'Start position should be empty')
                    self.assertEqual(expected_result[end].type, move_result[end].type, 'Piece type should match')
                    self.assertEqual(expected_result[end].color, move_result[end].color, 'Piece color should match')

    def test_king_perform_castle(self):
        """
        Perform castle to left and right with black king and white king.
        Expected result is king is moved two places to the left or right and the rook in that direction is
        moved on the other side of the king.
        :return:
        """
        castle_expected_result = {
            Color.white: [
                {
                    'king_start': 'e1',
                    'rook_start': 'a1',
                    'king_end': 'c1',
                    'rook_end': 'd1'
                },
                {
                    'king_start': 'e1',
                    'rook_start': 'h1',
                    'king_end': 'g1',
                    'rook_end': 'f1'
                },
            ],
            Color.black: [
                {
                    'king_start': 'e8',
                    'rook_start': 'a8',
                    'king_end': 'c8',
                    'rook_end': 'd8'
                },
                {
                    'king_start': 'e8',
                    'rook_start': 'h8',
                    'king_end': 'g8',
                    'rook_end': 'f8'
                },
            ]
        }

        for color, left_right_castle in castle_expected_result.items():
            for castle_info in left_right_castle:
                with self.subTest(color=color, castle_info=castle_info):
                    board = ChessBoard(empty_board=True)
                    board[castle_info['king_start']] = King(color)
                    board[castle_info['rook_start']] = Rook(color)

                    move_result = board.move_piece(castle_info['king_start'], castle_info['king_end'])

                    self.assertEqual(Type.king, board[castle_info['king_end']].type, 'King should have moved two spaces')
                    self.assertEqual(Type.rook, board[castle_info['rook_end']].type, 'Rook should be on other side of king')
                    self.assertIsNone(board[castle_info['rook_start']], 'Rook should have been moved')

                    expected_result = {
                        castle_info['king_start']: None,
                        castle_info['king_end']: King(color),
                        castle_info['rook_start']: None,
                        castle_info['rook_end']: Rook(color),
                    }
                    self.assertIn(castle_info['king_start'], move_result, 'King starting position should be in move_result')
                    self.assertIn(castle_info['king_end'], move_result, 'King ending position should be in move_result')
                    self.assertIn(castle_info['rook_start'], move_result, 'Rook starting position should be in move_result')
                    self.assertIn(castle_info['rook_end'], move_result, 'Rook ending position should be in move_result')
                    self.assertEqual(expected_result[castle_info['king_start']], move_result[castle_info['king_start']])
                    self.assertEqual(expected_result[castle_info['rook_start']], move_result[castle_info['rook_start']])
                    self.assertEqual(expected_result[castle_info['king_end']].type, move_result[castle_info['king_end']].type)
                    self.assertEqual(expected_result[castle_info['king_end']].color, move_result[castle_info['king_end']].color)
                    self.assertEqual(expected_result[castle_info['rook_end']].type, move_result[castle_info['rook_end']].type)
                    self.assertEqual(expected_result[castle_info['rook_end']].color, move_result[castle_info['rook_end']].color,)


if __name__ == '__main__':
    unittest.main()
