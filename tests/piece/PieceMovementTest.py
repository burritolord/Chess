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

                    board.move_piece(start, end)
                    self.assertIsNone(board[start], 'There should no longer be a piece on square ' + start)
                    self.assertIsInstance(board[end], piece_class, 'There should be a piece on square ' + end)
                    self.assertTrue(board[end].has_moved, 'Piece has moved')

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
            Type.pawn: Pawn,
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

                    board.move_piece(start, end)
                    self.assertIsNone(board[start], 'There should no longer be a piece on square ' + start)
                    self.assertIsInstance(board[end], piece_class, 'There should be a piece on square ' + end)
                    self.assertTrue(board[end].has_moved, 'Piece has moved')

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

                    board.move_piece(start, end)
                    self.assertIsNone(board[start], 'There should no longer be a piece on square ' + start)
                    self.assertIsInstance(board[end], piece_class, 'There should be a piece on square ' + end)
                    self.assertTrue(board[end].has_moved, 'Piece has moved')

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

                    board.move_piece(start, end)
                    self.assertIsNone(board[start], 'There should no longer be a piece on square ' + start)
                    self.assertIsInstance(board[end], piece_class, 'There should be a piece on square ' + end)
                    self.assertTrue(board[end].has_moved, 'Piece has moved')

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

                    board.move_piece(start, end)
                    self.assertIsNone(board[start], 'There should no longer be a piece on square ' + start)
                    self.assertIsInstance(board[end], piece_class, 'There should be a piece on square ' + end)
                    self.assertTrue(board[end].has_moved, 'Piece has moved')

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

                    board.move_piece(start, end)
                    self.assertIsNone(board[start], 'There should no longer be a piece on square ' + start)
                    self.assertIsInstance(board[end], piece_class, 'There should be a piece on square ' + end)
                    self.assertTrue(board[end].has_moved, 'Piece has moved')

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

                    board.move_piece(start, end)
                    self.assertIsNone(board[start], 'There should no longer be a piece on square ' + start)
                    self.assertIsInstance(board[end], piece_class, 'There should be a piece on square ' + end)
                    self.assertTrue(board[end].has_moved, 'Piece has moved')

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

                    board.move_piece(start, end)
                    self.assertIsNone(board[start], 'There should no longer be a piece on square ' + start)
                    self.assertIsInstance(board[end], piece_class, 'There should be a piece on square ' + end)
                    self.assertTrue(board[end].has_moved, 'Piece has moved')

    def test_king_cant_put_self_in_check(self):
        """
        Place king in middle square. Place rook of opposing color on an immediate front right diagonal square.
        Expected result is the space directly to the right and in front of king is not in legal moves list.
        :return:
        """
        color_group = [(Color.white, Color.black), (Color.black, Color.white)]
        for group in color_group:
            with self.subTest(group=group):
                board = ChessBoard(empty_board=True)
                king_color, rook_color = group
                board['d4'] = King(king_color)
                board['e5'] = Rook(rook_color)

                expected_moves = ['c3', 'c4', 'd3', 'e5']
                legal_moves = board.get_legal_moves('d4')
                legal_moves.sort()
                self.assertListEqual(expected_moves, legal_moves, 'King should not be able to put self in check')

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

                    board.move_piece(castle_info['king_start'], castle_info['king_end'])

                    self.assertEqual(Type.king, board[castle_info['king_end']].type, 'King should have moved two spaces')
                    self.assertEqual(Type.rook, board[castle_info['rook_end']].type, 'Rook should be on other side of king')
                    self.assertIsNone(board[castle_info['rook_start']], 'Rook should have been moved')

    def test_piece_pinned(self):
        """
        Test moving a piece of every type that is the same color as king but pinned by opponents piece.
        Expected result is legal move list for piece should be empty.
        :return:
        """
        # Pawn pined
        board = ChessBoard(empty_board=True)
        board['c3'] = King(Color.white)
        board['d4'] = Pawn(Color.white)
        board['f6'] = Bishop(Color.black)

        legal_moves = board.get_legal_moves('d4')
        self.assertListEqual([], legal_moves, 'Piece should not have any legal moves.')

        # Rook pined
        board = ChessBoard(empty_board=True)
        board['c3'] = King(Color.white)
        board['d4'] = Rook(Color.white)
        board['f6'] = Bishop(Color.black)

        legal_moves = board.get_legal_moves('d4')
        self.assertListEqual([], legal_moves, 'Piece should not have any legal moves.')

        # Knight pined
        board = ChessBoard(empty_board=True)
        board['c3'] = King(Color.white)
        board['d4'] = Knight(Color.white)
        board['f6'] = Bishop(Color.black)

        legal_moves = board.get_legal_moves('d4')
        self.assertListEqual([], legal_moves, 'Piece should not have any legal moves.')

        # Bishop pined
        board = ChessBoard(empty_board=True)
        board['c3'] = King(Color.white)
        board['c5'] = Bishop(Color.white)
        board['c6'] = Rook(Color.black)

        legal_moves = board.get_legal_moves('c5')
        self.assertListEqual([], legal_moves, 'Piece should not have any legal moves.')

        # Queen kinda pined
        board = ChessBoard(empty_board=True)
        board['c3'] = King(Color.white)
        board['c4'] = Queen(Color.white)
        board['c6'] = Rook(Color.black)

        legal_moves = board.get_legal_moves('c4')
        self.assertListEqual(['c5', 'c6'], legal_moves, 'Legal moves dont match expected moves.')


if __name__ == '__main__':
    unittest.main()
