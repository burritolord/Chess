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
        Move a piece of every type one square in the forward left diagonal direction.
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

    def test_pawn_legal_moves(self):
        """
        Move a pawn to each corner and one middle square.
        Expected result is that all the possible moves match the expected list.
        :return:
        """
        start_positions = {
            Color.white: {
                'a1': ['a2', 'a3'],
                'a8': [],
                'h1': ['h2', 'h3'],
                'h8': [],
                'd4': ['d5', 'd6']
            },
            Color.black: {
                'a1': [],
                'a8': ['a6', 'a7'],
                'h1': [],
                'h8': ['h6', 'h7'],
                'd4': ['d2', 'd3']
            }
        }
        for color, positions in start_positions.items():
            for start_position, expected_moves in positions.items():
                with self.subTest(color=color, start_position=start_position, expected_moves=expected_moves):
                    board = ChessBoard(empty_board=True)
                    board[start_position] = Pawn(color)
                    possible_moves = board.get_legal_moves(start_position)
                    possible_moves.sort()

                    message = 'Expected move list does not match actual move list'
                    self.assertListEqual(expected_moves, possible_moves, message)

        # Confirm pawn can only move one square after it is moved
        board = ChessBoard(empty_board=True)
        board['a1'] = Pawn(Color.white)
        board.move_piece('a1', 'a3')
        possible_moves = board.get_legal_moves('a3')
        expected_possible_moves = ['a4']

        self.assertListEqual(expected_possible_moves, possible_moves, 'Pawn should not be able to ')

    def test_pawn_legal_moves_piece_blocking(self):
        """
        Place a pawn on a square and another piece directly in front of it.
        Expected result is there are no legal moves for the pawn that is blocked.
        :return:
        """
        # Piece blocking of diff color and same color
        opposing_colors = [[Color.black, Color.white], [Color.white, Color.black]]
        for opposing_color in opposing_colors:
            start_positions = ['b2', 'g7']
            blocking_positions = ['b3', 'g6']
            pawn_colors = [Color.white, Color.black]
            for start, blocking, pawn_color, opposing in zip(start_positions, blocking_positions, pawn_colors, opposing_color):
                with self.subTest(start=start, blocking=blocking, pawn_color=pawn_color, opposing=opposing):
                    board = ChessBoard(empty_board=True)
                    board[start] = Pawn(pawn_color)
                    board[blocking] = Pawn(opposing)

                    legal_moves = board.get_legal_moves(start)
                    legal_moves.sort()

                    message = 'Pawn should not have any legal moves'
                    self.assertListEqual([], legal_moves, message)

    def test_rook_legal_moves(self):
        """
        Move a rook to each corner and one middle square.
        Expected result is that all the possible moves match the expected list.
        :return:
        """
        start_positions = {
            Color.white: {
                'a1': ['a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h1'],
                'a8': ['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'b8', 'c8', 'd8', 'e8', 'f8', 'g8', 'h8'],
                'h1': ['a1', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'h8'],
                'h8': ['a8', 'b8', 'c8', 'd8', 'e8', 'f8', 'g8', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7'],
                'd4': ['a4', 'b4', 'c4', 'd1', 'd2', 'd3', 'd5', 'd6', 'd7', 'd8', 'e4', 'f4', 'g4', 'h4']
            },
            Color.black: {
                'a1': ['a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h1'],
                'a8': ['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'b8', 'c8', 'd8', 'e8', 'f8', 'g8', 'h8'],
                'h1': ['a1', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'h8'],
                'h8': ['a8', 'b8', 'c8', 'd8', 'e8', 'f8', 'g8', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7'],
                'd4': ['a4', 'b4', 'c4', 'd1', 'd2', 'd3', 'd5', 'd6', 'd7', 'd8', 'e4', 'f4', 'g4', 'h4']
            }
        }
        for color, positions in start_positions.items():
            for start_position, expected_moves in positions.items():
                with self.subTest(color=color, start_position=start_position, expected_moves=expected_moves):
                    board = ChessBoard(empty_board=True)
                    board[start_position] = Rook(color)
                    possible_moves = board.get_legal_moves(start_position)
                    possible_moves.sort()

                    message = 'Expected move list does not match actual move list'
                    self.assertListEqual(expected_moves, possible_moves, message)

    def test_knight_legal_moves(self):
        """
        Move a knight to each corner and one middle square.
        Expected result is that all the possible moves match the expected list.
        :return:
        """
        start_positions = {
            Color.white: {
                'a1': ['b3', 'c2'],
                'a8': ['b6', 'c7'],
                'h1': ['f2', 'g3'],
                'h8': ['f7', 'g6'],
                'd4': ['b3', 'b5', 'c2', 'c6', 'e2', 'e6', 'f3', 'f5'],
                'g7': ['e6', 'e8', 'f5', 'h5']
            },
            Color.black: {
                'a1': ['b3', 'c2'],
                'a8': ['b6', 'c7'],
                'h1': ['f2', 'g3'],
                'h8': ['f7', 'g6'],
                'd4': ['b3', 'b5', 'c2', 'c6', 'e2', 'e6', 'f3', 'f5'],
                'g7': ['e6', 'e8', 'f5', 'h5']
            }
        }
        for color, positions in start_positions.items():
            for start_position, expected_moves in positions.items():
                with self.subTest(color=color, start_position=start_position, expected_moves=expected_moves):
                    board = ChessBoard(empty_board=True)
                    board[start_position] = Knight(color)
                    possible_moves = board.get_legal_moves(start_position)
                    possible_moves.sort()

                    message = 'Expected move list does not match actual move list'
                    self.assertListEqual(expected_moves, possible_moves, message)

    def test_bishop_legal_moves(self):
        """
        Move a bishop to each corner and one middle square.
        Expected result is that all the possible moves match the expected list.
        :return:
        """
        start_positions = {
            Color.white: {
                'a1': ['b2', 'c3', 'd4', 'e5', 'f6', 'g7', 'h8'],
                'a8': ['b7', 'c6', 'd5', 'e4', 'f3', 'g2', 'h1'],
                'h1': ['a8', 'b7', 'c6', 'd5', 'e4', 'f3', 'g2'],
                'h8': ['a1', 'b2', 'c3', 'd4', 'e5', 'f6', 'g7'],
                'd4': ['a1', 'a7', 'b2', 'b6', 'c3', 'c5', 'e3', 'e5', 'f2', 'f6', 'g1', 'g7', 'h8']
            },
            Color.black: {
                'a1': ['b2', 'c3', 'd4', 'e5', 'f6', 'g7', 'h8'],
                'a8': ['b7', 'c6', 'd5', 'e4', 'f3', 'g2', 'h1'],
                'h1': ['a8', 'b7', 'c6', 'd5', 'e4', 'f3', 'g2'],
                'h8': ['a1', 'b2', 'c3', 'd4', 'e5', 'f6', 'g7'],
                'd4': ['a1', 'a7', 'b2', 'b6', 'c3', 'c5', 'e3', 'e5', 'f2', 'f6', 'g1', 'g7', 'h8']
            }
        }
        for color, positions in start_positions.items():
            for start_position, expected_moves in positions.items():
                with self.subTest(color=color, start_position=start_position, expected_moves=expected_moves):
                    board = ChessBoard(empty_board=True)
                    board[start_position] = Bishop(color)
                    possible_moves = board.get_legal_moves(start_position)
                    possible_moves.sort()

                    message = 'Expected move list does not match actual move list'
                    self.assertListEqual(expected_moves, possible_moves, message)

    def test_queen_legal_moves(self):
        """
        Move a queen to each corner and one middle square.
        Expected result is that all the possible moves match the expected list.
        :return:
        """
        start_positions = {
            Color.white: {
                'a1': ['a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8',
                       'b1', 'b2', 'c1', 'c3', 'd1', 'd4', 'e1',
                       'e5', 'f1', 'f6', 'g1', 'g7', 'h1', 'h8'],
                'a8': ['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7',
                       'b7', 'b8', 'c6', 'c8', 'd5', 'd8', 'e4',
                       'e8', 'f3', 'f8', 'g2', 'g8', 'h1', 'h8'],
                'h1': ['a1', 'a8', 'b1', 'b7', 'c1', 'c6', 'd1',
                       'd5', 'e1', 'e4', 'f1', 'f3', 'g1', 'g2',
                       'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'h8'],
                'h8': ['a1', 'a8', 'b2', 'b8', 'c3', 'c8', 'd4',
                       'd8', 'e5', 'e8', 'f6', 'f8', 'g7', 'g8',
                       'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7'],
                'd4': ['a1', 'a4', 'a7', 'b2', 'b4', 'b6', 'c3',
                       'c4', 'c5', 'd1', 'd2', 'd3', 'd5', 'd6',
                       'd7', 'd8', 'e3', 'e4', 'e5', 'f2', 'f4',
                       'f6', 'g1', 'g4', 'g7', 'h4', 'h8']
            },
            Color.black: {
                'a1': ['a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8',
                       'b1', 'b2', 'c1', 'c3', 'd1', 'd4', 'e1',
                       'e5', 'f1', 'f6', 'g1', 'g7', 'h1', 'h8'],
                'a8': ['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7',
                       'b7', 'b8', 'c6', 'c8', 'd5', 'd8', 'e4',
                       'e8', 'f3', 'f8', 'g2', 'g8', 'h1', 'h8'],
                'h1': ['a1', 'a8', 'b1', 'b7', 'c1', 'c6', 'd1',
                       'd5', 'e1', 'e4', 'f1', 'f3', 'g1', 'g2',
                       'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'h8'],
                'h8': ['a1', 'a8', 'b2', 'b8', 'c3', 'c8', 'd4',
                       'd8', 'e5', 'e8', 'f6', 'f8', 'g7', 'g8',
                       'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7'],
                'd4': ['a1', 'a4', 'a7', 'b2', 'b4', 'b6', 'c3',
                       'c4', 'c5', 'd1', 'd2', 'd3', 'd5', 'd6',
                       'd7', 'd8', 'e3', 'e4', 'e5', 'f2', 'f4',
                       'f6', 'g1', 'g4', 'g7', 'h4', 'h8']
            }
        }
        for color, positions in start_positions.items():
            for start_position, expected_moves in positions.items():
                with self.subTest(color=color, start_position=start_position, expected_moves=expected_moves):
                    board = ChessBoard(empty_board=True)
                    board[start_position] = Queen(color)
                    possible_moves = board.get_legal_moves(start_position)
                    possible_moves.sort()

                    message = 'Expected move list does not match actual move list'
                    self.assertListEqual(expected_moves, possible_moves, message)

    def test_king_legal_moves(self):
        """
        Move a king to each corner and one middle square.
        Expected result is that all the possible moves match the expected list.
        :return:
        """
        start_positions = {
            Color.white: {
                'a1': ['a2', 'b1', 'b2'],
                'a8': ['a7', 'b7', 'b8'],
                'h1': ['g1', 'g2', 'h2'],
                'h8': ['g7', 'g8', 'h7'],
                'd4': ['c3', 'c4', 'c5', 'd3', 'd5', 'e3', 'e4', 'e5']
            },
            Color.black: {
                'a1': ['a2', 'b1', 'b2'],
                'a8': ['a7', 'b7', 'b8'],
                'h1': ['g1', 'g2', 'h2'],
                'h8': ['g7', 'g8', 'h7'],
                'd4': ['c3', 'c4', 'c5', 'd3', 'd5', 'e3', 'e4', 'e5']
            }
        }
        for color, positions in start_positions.items():
            for start_position, expected_moves in positions.items():
                with self.subTest(color=color, start_position=start_position, expected_moves=expected_moves):
                    board = ChessBoard(empty_board=True)
                    board[start_position] = King(color)
                    possible_moves = board.get_legal_moves(start_position)
                    possible_moves.sort()

                    message = 'Expected move list does not match actual move list'
                    self.assertListEqual(expected_moves, possible_moves, message)

    def test_pawn_capture(self):
        """
        Move a pawn to a square where there is a piece of the opposite color on one of the most immediate diagonal
        squares.
        Expected result is that the square that contains the piece of the opposite color is in the list of possible
        moves for the pawn. Opposing piece is also successfully captured by pawn.
        :return:
        """
        # Test diagonal move when a piece of the opposite color is present
        board = ChessBoard(empty_board=True)
        start_position = 'b1'
        capture_position = 'c2'
        board[start_position] = Pawn(Color.white)
        board['c2'] = Bishop(Color.black)
        expected_possible_moves = ['b2', 'b3', 'c2']
        possible_moves = board.get_legal_moves(start_position)
        possible_moves.sort()

        message = 'Expected pawn to be able to move diagonally'
        self.assertListEqual(expected_possible_moves, possible_moves, message)

        # place a second piece and confirm both diagonals show as possible moves
        board['a2'] = Rook(Color.black)
        expected_possible_moves = ['a2', 'b2', 'b3', 'c2']
        possible_moves = board.get_legal_moves(start_position)
        possible_moves.sort()

        message = 'Expected pawn to be able to move diagonally in both directions'
        self.assertListEqual(expected_possible_moves, possible_moves, message)

        # Move pawn to capture a piece
        board.move_piece(start_position, capture_position)
        message = 'Pawn should have captured piece on ' + capture_position + ' square'
        self.assertIsInstance(board[capture_position], Pawn, message)

    def test_pawn_cant_capture(self):
        """
        Move a pawn to a square where there is a piece of the same color on one of the most immediate diagonal
        squares.
        Expected result is that the square that contains the piece of the same color is not in the list of possible
        moves for the pawn.
        :return:
        """
        board = ChessBoard(empty_board=True)
        start_position = 'b1'
        board[start_position] = Pawn(Color.white)
        board['c2'] = Bishop(Color.white)
        expected_possible_moves = ['b2', 'b3']
        possible_moves = board.get_legal_moves(start_position)
        possible_moves.sort()

        message = 'Expected move list does not match actual move list'
        self.assertListEqual(expected_possible_moves, possible_moves, message)

    def test_rook_capture(self):
        """
        Move a 
        Expected result is that the squares that contain the pieces of the opposite color are in the list of possible
        moves for the rook. Opposing piece is also successfully captured by rook.
        :return:
        """
        board = ChessBoard(empty_board=True)
        start_position = 'b1'
        capture_position = 'e1'
        board[start_position] = Rook(Color.white)
        board['c2'] = Bishop(Color.black)
        board['c8'] = Pawn(Color.black)
        board['e1'] = Bishop(Color.black)

        # Test possible moves with several pieces on possible capture squares
        expected_possible_moves = ['a1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8', 'c1', 'd1', 'e1']
        possible_moves = board.get_legal_moves(start_position)
        possible_moves.sort()

        message = 'Expected move list does not match actual move list'
        self.assertListEqual(expected_possible_moves, possible_moves, message)

        # Confirm piece is captured
        board.move_piece(start_position, capture_position)
        message = 'Rook should have captured piece on ' + capture_position + ' square'
        self.assertIsInstance(board[capture_position], Rook, message)

    def test_rook_cant_capture(self):
        pass

    def test_knight_capture(self):
        board = ChessBoard(empty_board=True)
        start_position = 'd4'
        capture_position = 'f5'
        board[start_position] = Knight(Color.white)
        board[capture_position] = Bishop(Color.black)
        expected_possible_moves = ['b3', 'b5', 'c2', 'c6', 'e2', 'e6', 'f3', 'f5']
        possible_moves = board.get_legal_moves(start_position)
        possible_moves.sort()

        message = 'Expected move list does not match actual move list'
        self.assertListEqual(expected_possible_moves, possible_moves, message)

        # Move knight to capture a piece
        board.move_piece(start_position, capture_position)
        message = 'Knight should have captured piece on ' + capture_position + ' square'
        self.assertIsInstance(board[capture_position], Knight, message)

    def test_knight_cant_capture(self):
        pass

    def test_bishop_capture(self):
        board = ChessBoard(empty_board=True)
        start_position = 'd4'
        capture_position = 'h8'
        board[start_position] = Bishop(Color.white)
        board['c5'] = Queen(Color.black)
        board[capture_position] = Pawn(Color.black)
        expected_possible_moves = ['a1', 'b2', 'c3', 'c5', 'e3', 'e5', 'f2', 'f6', 'g1', 'g7', 'h8']
        possible_moves = board.get_legal_moves(start_position)
        possible_moves.sort()

        message = 'Expected move list does not match actual move list'
        self.assertListEqual(expected_possible_moves, possible_moves, message)

        # Move bishop to capture a piece
        board.move_piece(start_position, capture_position)
        message = 'Bishop should have captured piece on ' + capture_position + ' square'
        self.assertIsInstance(board[capture_position], Bishop, message)

    def test_bishop_cant_capture(self):
        pass

    def test_king_capture(self):
        board = ChessBoard(empty_board=True)
        start_position = 'd4'
        capture_position = 'd5'
        board[start_position] = King(Color.white)
        board['e4'] = Pawn(Color.black)
        board[capture_position] = Pawn(Color.black)
        expected_possible_moves = ['c3', 'c5', 'd5', 'e3', 'e5']
        possible_moves = board.get_legal_moves(start_position)
        possible_moves.sort()

        message = 'Expected move list does not match actual move list'
        self.assertListEqual(expected_possible_moves, possible_moves, message)

        # Move bishop to capture a piece
        board.move_piece(start_position, capture_position)
        message = 'King should have captured piece on ' + capture_position + ' square'
        self.assertIsInstance(board[capture_position], King, message)

    def test_king_cant_capture(self):
        pass

    def test_queen_capture(self):
        board = ChessBoard(empty_board=True)
        start_position = 'd4'
        capture_position = 'e4'
        board[start_position] = Queen(Color.white)
        board['d5'] = Pawn(Color.black)
        board[capture_position] = Pawn(Color.black)
        expected_possible_moves = ['a1', 'a4', 'a7', 'b2', 'b4', 'b6', 'c3', 'c4', 'c5', 'd1',
                                   'd2', 'd3', 'd5', 'e3', 'e4', 'e5', 'f2', 'f6', 'g1', 'g7', 'h8']
        possible_moves = board.get_legal_moves(start_position)
        possible_moves.sort()

        message = 'Expected move list does not match actual move list'
        self.assertListEqual(expected_possible_moves, possible_moves, message)

        # Move queen to capture a piece
        board.move_piece(start_position, capture_position)
        message = 'Queen should have captured piece on ' + capture_position + ' square'
        self.assertIsInstance(board[capture_position], Queen, message)

    def test_queen_cant_capture(self):
        pass

    def test_en_passant_capture(self):
        """
        Test capturing an opponents pawn via en passant.
        :return:
        """
        board = ChessBoard(empty_board=True)

        # Check from white perspective
        board['b5'] = Pawn(Color.white)
        board['a7'] = Pawn(Color.black)
        board.move_piece('a7', 'a5')
        board.move_piece('b5', 'a6')
        self.assertIsNone(board['a5'], 'Expected black pawn to be captured')

        # Check from black perspective
        board['e4'] = Pawn(Color.black)
        board['d2'] = Pawn(Color.white)
        board.move_piece('d2', 'd4')
        board.move_piece('e4', 'd3')
        self.assertIsNone(board['d4'], 'Expected black pawn to be captured')

if __name__ == '__main__':
    unittest.main()
