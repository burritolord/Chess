import unittest
from src.board.chess_board import ChessBoard
from src.piece.king import King
from src.piece.pawn import Pawn
from src.piece.queen import Queen
from src.piece.bishop import Bishop
from src.piece.knight import Knight
from src.piece.rook import Rook
from src.piece.color import Color
from src.piece.type import Type
from src.piece.move_direction import MoveDirection


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
        piece_colors = [Color.WHITE, Color.BLACK]
        piece_types = {
            Type.PAWN: Pawn,
            Type.KING: King,
            Type.QUEEN: Queen,
            Type.ROOK: Rook
        }

        for start, end, color in zip(start_positions, end_positions, piece_colors):
            for t, piece_class in piece_types.items():
                with self.subTest(t=t, piece_class=piece_class, start=start, end=end, color=color):
                    board = ChessBoard()
                    board[start] = piece_class(color)

                    move_result = board.move_piece(start, end)
                    self.assertIsNone(board[start], 'There should no longer be a piece on square ' + start)
                    self.assertIsInstance(board[end], piece_class, 'There should be a piece on square ' + end)

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
        piece_colors = [Color.WHITE, Color.BLACK]
        piece_types = {
            Type.BISHOP: Bishop,
            Type.KING: King,
            Type.QUEEN: Queen,
        }
        for start, end, color in zip(start_positions, end_positions, piece_colors):
            for t, piece_class in piece_types.items():
                with self.subTest(t=t, piece_class=piece_class, start=start, end=end, color=color):
                    board = ChessBoard()
                    board[start] = piece_class(color)

                    move_result = board.move_piece(start, end)
                    self.assertIsNone(board[start], 'There should no longer be a piece on square ' + start)
                    self.assertIsInstance(board[end], piece_class, 'There should be a piece on square ' + end)

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
        piece_colors = [Color.WHITE, Color.BLACK]
        piece_types = {
            Type.KING: King,
            Type.QUEEN: Queen,
            Type.ROOK: Rook
        }
        for start, end, color in zip(start_positions, end_positions, piece_colors):
            for t, piece_class in piece_types.items():
                with self.subTest(t=t, piece_class=piece_class, start=start, end=end, color=color):
                    board = ChessBoard()
                    board[start] = piece_class(color)

                    move_result = board.move_piece(start, end)
                    self.assertIsNone(board[start], 'There should no longer be a piece on square ' + start)
                    self.assertIsInstance(board[end], piece_class, 'There should be a piece on square ' + end)

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
        piece_colors = [Color.WHITE, Color.BLACK]
        piece_types = {
            Type.KING: King,
            Type.QUEEN: Queen,
            Type.BISHOP: Bishop
        }
        for start, end, color in zip(start_positions, end_positions, piece_colors):
            for t, piece_class in piece_types.items():
                with self.subTest(t=t, piece_class=piece_class, start=start, end=end, color=color):
                    board = ChessBoard()
                    board[start] = piece_class(color)

                    move_result = board.move_piece(start, end)
                    self.assertIsNone(board[start], 'There should no longer be a piece on square ' + start)
                    self.assertIsInstance(board[end], piece_class, 'There should be a piece on square ' + end)

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
        piece_colors = [Color.WHITE, Color.BLACK]
        piece_types = {
            Type.KING: King,
            Type.QUEEN: Queen,
            Type.ROOK: Rook
        }
        for start, end, color in zip(start_positions, end_positions, piece_colors):
            for t, piece_class in piece_types.items():
                with self.subTest(t=t, piece_class=piece_class, start=start, end=end, color=color):
                    board = ChessBoard()
                    board[start] = piece_class(color)

                    move_result = board.move_piece(start, end)
                    self.assertIsNone(board[start], 'There should no longer be a piece on square ' + start)
                    self.assertIsInstance(board[end], piece_class, 'There should be a piece on square ' + end)

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
        piece_colors = [Color.WHITE, Color.BLACK]
        piece_types = {
            Type.KING: King,
            Type.QUEEN: Queen,
            Type.BISHOP: Bishop
        }
        for start, end, color in zip(start_positions, end_positions, piece_colors):
            for t, piece_class in piece_types.items():
                with self.subTest(t=t, piece_class=piece_class, start=start, end=end, color=color):
                    board = ChessBoard()
                    board[start] = piece_class(color)

                    move_result = board.move_piece(start, end)
                    self.assertIsNone(board[start], 'There should no longer be a piece on square ' + start)
                    self.assertIsInstance(board[end], piece_class, 'There should be a piece on square ' + end)

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
        piece_colors = [Color.WHITE, Color.BLACK]
        piece_types = {
            Type.KING: King,
            Type.QUEEN: Queen,
            Type.ROOK: Rook
        }
        for start, end, color in zip(start_positions, end_positions, piece_colors):
            for t, piece_class in piece_types.items():
                with self.subTest(t=t, piece_class=piece_class, start=start, end=end, color=color):
                    board = ChessBoard()
                    board[start] = piece_class(color)

                    move_result = board.move_piece(start, end)
                    self.assertIsNone(board[start], 'There should no longer be a piece on square ' + start)
                    self.assertIsInstance(board[end], piece_class, 'There should be a piece on square ' + end)

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
        piece_colors = [Color.WHITE, Color.BLACK]
        piece_types = {
            Type.KING: King,
            Type.QUEEN: Queen,
            Type.BISHOP: Bishop
        }
        for start, end, color in zip(start_positions, end_positions, piece_colors):
            for t, piece_class in piece_types.items():
                with self.subTest(t=t, piece_class=piece_class, start=start, end=end, color=color):
                    board = ChessBoard()
                    board[start] = piece_class(color)

                    move_result = board.move_piece(start, end)
                    self.assertIsNone(board[start], 'There should no longer be a piece on square ' + start)
                    self.assertIsInstance(board[end], piece_class, 'There should be a piece on square ' + end)

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
        piece_colors = [Color.WHITE, Color.BLACK]

        for color in piece_colors:
            for end_position in end_positions:
                with self.subTest(color=color, end_position=end_position):
                    board = ChessBoard()
                    board[start_position] = Knight(color)

                    move_result = board.move_piece(start_position, end_position)
                    self.assertIsNone(board[start_position], 'There should no longer be a piece on start position')
                    self.assertIsInstance(board[end_position], Knight, 'There should be a piece on end position')

                    expected_result = {start_position: None, end_position: Knight(color)}
                    self.assertDictEqual(expected_result, move_result, 'Expected move result does not match actual')

    def test_pawn_movement_adjusted_after_moving(self):
        """
        Move a pawn of each color
        Expected result is pawn cannot move forward two squares once it has moved.
        :return:
        """
        board = ChessBoard()
        positions = {
            Color.WHITE: ('b2', 'b3'),
            Color.BLACK: ('b7', 'b6')
        }
        expected_directions = {
            MoveDirection.FORWARD: 1,
            MoveDirection.F_RIGHT_DIAG: 1,
            MoveDirection.F_LEFT_DIAG: 1
        }
        for color in [Color.BLACK, Color.WHITE]:
            with self.subTest(color=color, movement=positions[color]):
                start_pos, end_pos = positions[color]
                board[start_pos] = Pawn(color)
                board.move_piece(start_pos, end_pos)

                self.assertDictEqual(expected_directions, board[end_pos].move_directions, 'Incorrect move_directions')

    def test_king_movement_adjusted_after_moving(self):
        """
        Move a king of each color
        Expected result is king cannot move left or right two squares once it has moved.
        :return:
        """
        board = ChessBoard()
        positions = {
            Color.WHITE: ('e1', 'e2'),
            Color.BLACK: ('e8', 'e7')
        }
        expected_directions = {
            MoveDirection.FORWARD: 1,
            MoveDirection.F_RIGHT_DIAG: 1,
            MoveDirection.RIGHT: 1,
            MoveDirection.B_RIGHT_DIAG: 1,
            MoveDirection.BACKWARD: 1,
            MoveDirection.B_LEFT_DIAG: 1,
            MoveDirection.LEFT: 1,
            MoveDirection.F_LEFT_DIAG: 1
        }

        for color in [Color.BLACK, Color.WHITE]:
            with self.subTest(color=color, movement=positions[color]):
                start_pos, end_pos = positions[color]
                board[start_pos] = King(color)
                board.move_piece(start_pos, end_pos)

                self.assertDictEqual(expected_directions, board[end_pos].move_directions, 'Incorrect move_directions')

    def test_king_movement_adjusted_after_left_rook_moves(self):
        """
        Move the king side rook for white and black player
        Expected result is king can no longer castle king side.
        :return:
        """
        board = ChessBoard()
        king_positions = {
            Color.WHITE: 'e1',
            Color.BLACK: 'e8'
        }
        rook_positions = {
            Color.WHITE: ('a1', 'e2'),
            Color.BLACK: ('h8', 'h7')
        }
        expected_directions = {
            MoveDirection.FORWARD: 1,
            MoveDirection.F_RIGHT_DIAG: 1,
            MoveDirection.RIGHT: 2,
            MoveDirection.B_RIGHT_DIAG: 1,
            MoveDirection.BACKWARD: 1,
            MoveDirection.B_LEFT_DIAG: 1,
            MoveDirection.LEFT: 1,
            MoveDirection.F_LEFT_DIAG: 1
        }

        for color in [Color.BLACK, Color.WHITE]:
            with self.subTest(color=color, king_pos=king_positions[color], rook_pos=rook_positions[color]):
                king_pos = king_positions[color]
                rook_start, rook_end = rook_positions[color]
                board[king_pos] = King(color)
                board[rook_start] = Rook(color)
                board.move_piece(rook_start, rook_end)

                self.assertDictEqual(expected_directions, board[king_pos].move_directions, 'Incorrect move_directions')

    def test_king_movement_adjusted_after_right_rook_moves(self):
        """
        Move the queen side rook for white and black player
        Expected result is king can no longer castle queen side.
        :return:
        """
        board = ChessBoard()
        king_positions = {
            Color.WHITE: 'e1',
            Color.BLACK: 'e8'
        }
        rook_positions = {
            Color.WHITE: ('h1', 'h2'),
            Color.BLACK: ('a8', 'a7')
        }
        expected_directions = {
            MoveDirection.FORWARD: 1,
            MoveDirection.F_RIGHT_DIAG: 1,
            MoveDirection.RIGHT: 1,
            MoveDirection.B_RIGHT_DIAG: 1,
            MoveDirection.BACKWARD: 1,
            MoveDirection.B_LEFT_DIAG: 1,
            MoveDirection.LEFT: 2,
            MoveDirection.F_LEFT_DIAG: 1
        }

        for color in [Color.BLACK, Color.WHITE]:
            with self.subTest(color=color, king_pos=king_positions[color], rook_pos=rook_positions[color]):
                king_pos = king_positions[color]
                rook_start, rook_end = rook_positions[color]
                board[king_pos] = King(color)
                board[rook_start] = Rook(color)
                board.move_piece(rook_start, rook_end)

                self.assertDictEqual(expected_directions, board[king_pos].move_directions, 'Incorrect move_directions')

    def test_king_perform_castle(self):
        """
        Perform castle to left and right with black king and white king.
        Expected result is king is moved two places to the left or right and the rook in that direction is
        moved on the other side of the king.
        :return:
        """
        castle_expected_result = {
            Color.WHITE: [
                {'king_move': ('e1', 'c1'), 'rook_move': ('a1', 'd1')},
                {'king_move': ('e1', 'g1'), 'rook_move': ('h1', 'f1')}
            ],
            Color.BLACK: [
                {'king_move': ('e8', 'c8'), 'rook_move': ('a8', 'd8')},
                {'king_move': ('e8', 'g8'), 'rook_move': ('h8', 'f8')}
            ]
        }

        for color, left_right_castle in castle_expected_result.items():
            for castle_info in left_right_castle:
                with self.subTest(color=color, castle_info=castle_info):
                    board = ChessBoard()
                    king_start, king_end = castle_info['king_move']
                    rook_start, rook_end = castle_info['rook_move']
                    board[king_start] = King(color)
                    board[rook_start] = Rook(color)

                    move_result = board.move_piece(king_start, king_end)

                    self.assertEqual(Type.KING, board[king_end].type, 'King should have moved two spaces')
                    self.assertEqual(Type.ROOK, board[rook_end].type, 'Rook should be on other side of king')
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
