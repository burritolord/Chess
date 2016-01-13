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
        """
        Move a piece of every type one square forward.
        Expected result is that the piece no longer exist on the starting square, but on the ending square.
        :return:
        """
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
        """
        Move a piece of every type one square in the forward right diagonal direction.
        Expected result is that the piece no longer exist on the starting square, but on the ending square.
        :return:
        """
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
        """
        Move a piece of every type one square to the right.
        Expected result is that the piece no longer exist on the starting square, but on the ending square.
        :return:
        """
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
        """
        Move a piece of every type one square in the back right diagonal direction.
        Expected result is that the piece no longer exist on the starting square, but on the ending square.
        :return:
        """
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

    def test_move_backward(self):
        """
        Move a piece of every type one square backward.
        Expected result is that the piece no longer exist on the starting square, but on the ending square.
        :return:
        """
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
        """
        Move a piece of every type one square in the back left diagonal direction.
        Expected result is that the piece no longer exist on the starting square, but on the ending square.
        :return:
        """
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
        """
        Move a piece of every type one square left.
        Expected result is that the piece no longer exist on the starting square, but on the ending square.
        :return:
        """
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
        """
        Move a piece of every type one square in the forward left diagonal direction.
        Expected result is that the piece no longer exist on the starting square, but on the ending square.
        :return:
        """
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

    def test_move_forward_piece_blocking(self):
        pass

    def test_move_forward_right_diagonal_piece_blocking(self):
        pass

    def test_move_right_piece_blocking(self):
        pass

    def test_move_back_right_diagonal_piece_blocking(self):
        pass

    def test_move_backward_piece_blocking(self):
        pass

    def test_move_back_left_diagonal_piece_blocking(self):
        pass

    def test_move_left_piece_blocking(self):
        pass

    def test_move_forward_left_diagonal_piece_blocking(self):
        pass

    # ------------------------------------------------------------------------------------------------------------------------------------------------
    def test_pawn_possible_moves(self):
        """
        Move a pawn to each corner and one middle square.
        Expected result is that all the possible moves match the expected list.
        :return:
        """
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
                possible_moves.sort()

                message = 'Expected move list does not match actual move list'
                self.assertListEqual(start_positions[start_position], possible_moves, message)

        # Confirm pawn can only move one square after it is moved
        board = ChessBoard(empty_board=True)
        board['a1'] = Pawn(Color.white)
        board.move_piece('a1', 'a3')
        possible_moves = board.get_possible_moves('a3')
        expected_possible_moves = ['a4']

        self.assertListEqual(expected_possible_moves, possible_moves, 'Pawn should not be able to ')

    def test_rook_possible_moves(self):
        """
        Move a rook to each corner and one middle square.
        Expected result is that all the possible moves match the expected list.
        :return:
        """
        start_positions = {'a1': ['a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h1'],
                           'a8': ['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'b8', 'c8', 'd8', 'e8', 'f8', 'g8', 'h8'],
                           'h1': ['a1', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'h8'],
                           'h8': ['a8', 'b8', 'c8', 'd8', 'e8', 'f8', 'g8', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7'],
                           'd4': ['a4', 'b4', 'c4', 'd1', 'd2', 'd3', 'd5', 'd6', 'd7', 'd8', 'e4', 'f4', 'g4', 'h4']
                           }
        for start_position, expected_possible_moves in start_positions.items():
            with self.subTest(start_position=start_position, expected_possible_moves=expected_possible_moves):
                board = ChessBoard(empty_board=True)
                board[start_position] = Rook(Color.white)
                possible_moves = board.get_possible_moves(start_position)
                possible_moves.sort()

                message = 'Expected move list does not match actual move list'
                self.assertListEqual(expected_possible_moves, possible_moves, message)

    def test_knight_possible_moves(self):
        """
        Move a knight to each corner and one middle square.
        Expected result is that all the possible moves match the expected list.
        :return:
        """
        start_positions = {'a1': ['b3', 'c2'],
                           'a8': ['b6', 'c7'],
                           'h1': ['f2', 'g3'],
                           'h8': ['f7', 'g6'],
                           'd4': ['b3', 'b5', 'c2', 'c6', 'e2', 'e6', 'f3', 'f5']
                           }
        for start_position, expected_possible_moves in start_positions.items():
            with self.subTest(start_position=start_position, expected_possible_moves=expected_possible_moves):
                board = ChessBoard(empty_board=True)
                board[start_position] = Knight(Color.white)
                possible_moves = board.get_possible_moves(start_position)
                possible_moves.sort()

                message = 'Expected move list does not match actual move list'
                self.assertListEqual(expected_possible_moves, possible_moves, message)

    def test_bishop_possible_moves(self):
        """
        Move a bishop to each corner and one middle square.
        Expected result is that all the possible moves match the expected list.
        :return:
        """
        start_positions = {'a1': ['b2', 'c3', 'd4', 'e5', 'f6', 'g7', 'h8'],
                           'a8': ['b7', 'c6', 'd5', 'e4', 'f3', 'g2', 'h1'],
                           'h1': ['a8', 'b7', 'c6', 'd5', 'e4', 'f3', 'g2'],
                           'h8': ['a1', 'b2', 'c3', 'd4', 'e5', 'f6', 'g7'],
                           'd4': ['a1', 'a7', 'b2', 'b6', 'c3', 'c5', 'e3', 'e5', 'f2', 'f6', 'g1', 'g7', 'h8']
                           }
        for start_position, expected_possible_moves in start_positions.items():
            with self.subTest(start_position=start_position, expected_possible_moves=expected_possible_moves):
                board = ChessBoard(empty_board=True)
                board[start_position] = Bishop(Color.white)
                possible_moves = board.get_possible_moves(start_position)
                possible_moves.sort()

                message = 'Expected move list does not match actual move list'
                self.assertListEqual(expected_possible_moves, possible_moves, message)

    def test_queen_possible_moves(self):
        """
        Move a queen to each corner and one middle square.
        Expected result is that all the possible moves match the expected list.
        :return:
        """
        start_positions = {'a1': ['a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8',
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
        for start_position, expected_possible_moves in start_positions.items():
            with self.subTest(start_position=start_position, expected_possible_moves=expected_possible_moves):
                board = ChessBoard(empty_board=True)
                board[start_position] = Queen(Color.white)
                possible_moves = board.get_possible_moves(start_position)
                possible_moves.sort()

                message = 'Expected move list does not match actual move list'
                self.assertListEqual(expected_possible_moves, possible_moves, message)

    def test_king_possible_moves(self):
        """
        Move a king to each corner and one middle square.
        Expected result is that all the possible moves match the expected list.
        :return:
        """
        start_positions = {'a1': ['a2', 'b1', 'b2'],
                           'a8': ['a7', 'b7', 'b8'],
                           'h1': ['g1', 'g2', 'h2'],
                           'h8': ['g7', 'g8', 'h7'],
                           'd4': ['c3', 'c4', 'c5', 'd3', 'd5', 'e3', 'e4', 'e5']
                           }
        for start_position, expected_possible_moves in start_positions.items():
            with self.subTest(start_position=start_position, expected_possible_moves=expected_possible_moves):
                board = ChessBoard(empty_board=True)
                board[start_position] = King(Color.white)
                possible_moves = board.get_possible_moves(start_position)
                possible_moves.sort()

                message = 'Expected move list does not match actual move list'
                self.assertListEqual(expected_possible_moves, possible_moves, message)

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
        possible_moves = board.get_possible_moves(start_position)
        possible_moves.sort()

        message = 'Expected pawn to be able to move diagonally'
        self.assertListEqual(expected_possible_moves, possible_moves, message)

        # place a second piece and confirm both diagonals show as possible moves
        board['a2'] = Rook(Color.black)
        expected_possible_moves = ['a2', 'b2', 'b3', 'c2']
        possible_moves = board.get_possible_moves(start_position)
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
        possible_moves = board.get_possible_moves(start_position)
        possible_moves.sort()

        message = 'Expected move list does not match actual move list'
        self.assertListEqual(expected_possible_moves, possible_moves, message)

    def test_rook_capture(self):
        """
        Place a black piece on a square on file 2 and another on rank . Move the rook to the square occupied by a
        Expected result is that the squares that contain the pieces of the opposite color are in the list of possible
        moves for the rook. Opposing piece is also successfully captured by pawn.
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
        possible_moves = board.get_possible_moves(start_position)
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
        possible_moves = board.get_possible_moves(start_position)
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
        possible_moves = board.get_possible_moves(start_position)
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
        capture_position = 'e4'
        board[start_position] = King(Color.white)
        board['d5'] = Pawn(Color.black)
        board[capture_position] = Pawn(Color.black)
        expected_possible_moves = ['c3', 'c4', 'c5', 'd3', 'd5', 'e3', 'e4', 'e5']
        possible_moves = board.get_possible_moves(start_position)
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
        possible_moves = board.get_possible_moves(start_position)
        possible_moves.sort()

        message = 'Expected move list does not match actual move list'
        self.assertListEqual(expected_possible_moves, possible_moves, message)

        # Move queen to capture a piece
        board.move_piece(start_position, capture_position)
        message = 'Queen should have captured piece on ' + capture_position + ' square'
        self.assertIsInstance(board[capture_position], Queen, message)

    def test_queen_cant_capture(self):
        pass

if __name__ == '__main__':
    unittest.main()