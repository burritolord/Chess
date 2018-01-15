import unittest
from board.chess_board import ChessBoard
from piece.king import King
from piece.pawn import Pawn
from piece.queen import Queen
from piece.bishop import Bishop
from piece.knight import Knight
from piece.rook import Rook
from piece.color import Color
from piece.type import Type


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
                    self.assertDictEqual(expected_result, move_result, 'Expected move result does not match actual')

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
                    self.assertDictEqual(expected_result, move_result, 'Expected move result does not match actual')

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
                    self.assertDictEqual(expected_result, move_result, 'Expected move result does not match actual')

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
                    self.assertDictEqual(expected_result, move_result, 'Expected move result does not match actual')

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
                    self.assertDictEqual(expected_result, move_result, 'Expected move result does not match actual')

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
                    self.assertDictEqual(expected_result, move_result, 'Expected move result does not match actual')

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
                    self.assertDictEqual(expected_result, move_result, 'Expected move result does not match actual')

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
                    self.assertDictEqual(expected_result, move_result, 'Expected move result does not match actual')

    def test_move_l_shape(self):
        """
        Move knight in every possible direction.
        Expected result is that the knight no longer exist on the starting square, but on the ending square.
        :return:
        """
        start_position = 'd4'
        end_positions = ['b3', 'b5', 'c2', 'c6', 'e2', 'e6', 'f3', 'f5']
        piece_colors = [Color.white, Color.black]

        for color in piece_colors:
            for end_position in end_positions:
                with self.subTest(color=color, end_position=end_position):
                    board = ChessBoard(empty_board=True)
                    board[start_position] = Knight(color)
                    self.assertFalse(board[start_position].has_moved, 'Piece has never moved')

                    move_result = board.move_piece(start_position, end_position)
                    self.assertIsNone(board[start_position], 'There should no longer be a piece on start position')
                    self.assertIsInstance(board[end_position], Knight, 'There should be a piece on end position')
                    self.assertTrue(board[end_position].has_moved, 'Piece has moved flag not updated')

                    expected_result = {start_position: None, end_position: Knight(color)}
                    self.assertDictEqual(expected_result, move_result, 'Expected move result does not match actual')

    def test_king_perform_castle(self):
        """
        Perform castle to left and right with black king and white king.
        Expected result is king is moved two places to the left or right and the rook in that direction is
        moved on the other side of the king.
        :return:
        """
        castle_expected_result = {
            Color.white: [
                {'king_move': ('e1', 'c1'), 'rook_move': ('a1', 'd1')},
                {'king_move': ('e1', 'g1'), 'rook_move': ('h1', 'f1')}
            ],
            Color.black: [
                {'king_move': ('e8', 'c8'), 'rook_move': ('a8', 'd8')},
                {'king_move': ('e8', 'g8'), 'rook_move': ('h8', 'f8')}
            ]
        }

        for color, left_right_castle in castle_expected_result.items():
            for castle_info in left_right_castle:
                with self.subTest(color=color, castle_info=castle_info):
                    board = ChessBoard(empty_board=True)
                    king_start, king_end = castle_info['king_move']
                    rook_start, rook_end = castle_info['rook_move']
                    board[king_start] = King(color)
                    board[rook_start] = Rook(color)

                    move_result = board.move_piece(king_start, king_end)

                    self.assertEqual(Type.king, board[king_end].type, 'King should have moved two spaces')
                    self.assertEqual(Type.rook, board[rook_end].type, 'Rook should be on other side of king')
                    self.assertIsNone(board[rook_start], 'Rook should have been moved')

                    expected_result = {
                        king_start: None,
                        king_end: King(color),
                        rook_start: None,
                        rook_end: Rook(color),
                    }
                    self.assertDictEqual(expected_result, move_result, 'Expected move result does not match actual')


if __name__ == '__main__':
    unittest.main()
