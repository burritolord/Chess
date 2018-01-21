import unittest
from board.chess_board import ChessBoard
from piece.king import King
from piece.pawn import Pawn
from piece.queen import Queen
from piece.bishop import Bishop
from piece.knight import Knight
from piece.rook import Rook
from piece.color import Color


class PieceCaptureTest(unittest.TestCase):

    def test_pawn_capture(self):
        """
        Move a pawn to a square where there is a piece of the opposite color on one of the most immediate diagonal
        squares.
        Expected result is that the square that contains the piece of the opposite color is in the list of possible
        moves for the pawn. Opposing piece is also successfully captured by pawn.
        :return:
        """
        # Test diagonal move when a piece of the opposite color is present
        board = ChessBoard()
        start_position = 'b1'
        capture_position = 'c2'
        board[start_position] = Pawn(Color.WHITE)
        board['c2'] = Bishop(Color.BLACK)
        expected_possible_moves = ['b2', 'b3', 'c2']
        possible_moves = board.get_legal_moves(start_position)
        possible_moves.sort()

        message = 'Expected pawn to be able to move diagonally'
        self.assertListEqual(expected_possible_moves, possible_moves, message)

        # place a second piece and confirm both diagonals show as possible moves
        board['a2'] = Rook(Color.BLACK)
        expected_possible_moves = ['a2', 'b2', 'b3', 'c2']
        possible_moves = board.get_legal_moves(start_position)
        possible_moves.sort()

        message = 'Expected pawn to be able to move diagonally in both directions'
        self.assertListEqual(expected_possible_moves, possible_moves, message)

        # Move pawn to capture a piece
        move_result = board.move_piece(start_position, capture_position)
        message = 'Pawn should have captured piece on ' + capture_position + ' square'
        self.assertIsInstance(board[capture_position], Pawn, message)

        # Test move result
        expected_move_result = {start_position: None, capture_position: Pawn(Color.WHITE)}
        self.assertDictEqual(expected_move_result, move_result, 'Expected move result does not match actual')

    def test_pawn_cant_capture(self):
        """
        Move a pawn to a square where there is a piece of the same color on one of the most immediate diagonal
        squares.
        Expected result is that the square that contains the piece of the same color is not in the list of possible
        moves for the pawn.
        :return:
        """
        board = ChessBoard()
        start_position = 'b1'
        board[start_position] = Pawn(Color.WHITE)
        board['c2'] = Bishop(Color.WHITE)
        expected_possible_moves = ['b2', 'b3']
        possible_moves = board.get_legal_moves(start_position)
        possible_moves.sort()

        message = 'Expected move list does not match actual move list'
        self.assertListEqual(expected_possible_moves, possible_moves, message)

    def test_rook_capture(self):
        """
        Move a rook to square where there are pieces of the opposite color on capture file and rank.
        Expected result is that the squares that contain the pieces of the opposite color are in the list of possible
        moves for the rook. One opposing piece is also successfully captured by rook.
        :return:
        """
        board = ChessBoard()
        start_position = 'b1'
        capture_position = 'e1'
        board[start_position] = Rook(Color.WHITE)
        board['c2'] = Bishop(Color.BLACK)
        board['c8'] = Pawn(Color.BLACK)
        board['e1'] = Bishop(Color.BLACK)

        # Test possible moves with several pieces on possible capture squares
        expected_possible_moves = ['a1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8', 'c1', 'd1', 'e1']
        possible_moves = board.get_legal_moves(start_position)
        possible_moves.sort()

        message = 'Expected move list does not match actual move list'
        self.assertListEqual(expected_possible_moves, possible_moves, message)

        # Confirm piece is captured
        move_result = board.move_piece(start_position, capture_position)
        message = 'Rook should have captured piece on ' + capture_position + ' square'
        self.assertIsInstance(board[capture_position], Rook, message)

        # Test move result
        expected_move_result = {start_position: None, capture_position: Rook(Color.WHITE)}
        self.assertDictEqual(expected_move_result, move_result, 'Expected move result does not match actual')

    def test_rook_cant_capture(self):
        """
        Move rook to a square and another piece of the same color immediately to the right of the rook.
        Expected result is that the square containing the pieces of the same color is not in the list of legal
        moves for the rook.
        :return:
        """
        color_group = [Color.WHITE, Color.BLACK]
        for color in color_group:
            with self.subTest(color=color):
                board = ChessBoard()
                board['d4'] = Rook(color)
                board['e4'] = Pawn(color)

                expected_moves = [
                    'a4', 'b4', 'c4', 'd1', 'd2',
                    'd3', 'd5', 'd6', 'd7', 'd8'
                ]
                legal_moves = board.get_legal_moves('d4')
                legal_moves.sort()
                self.assertListEqual(expected_moves, legal_moves, 'Expected moves does not match legal moves')

    def test_knight_capture(self):
        """
        Move knight to a middle square with a piece on a capture square.
        Expected result is position with opponent piece is in legal move list and piece is captured
        when knight moves to that position.
        :return:
        """
        board = ChessBoard()
        start_position = 'd4'
        capture_position = 'f5'
        board[start_position] = Knight(Color.WHITE)
        board[capture_position] = Bishop(Color.BLACK)
        expected_possible_moves = ['b3', 'b5', 'c2', 'c6', 'e2', 'e6', 'f3', 'f5']
        possible_moves = board.get_legal_moves(start_position)
        possible_moves.sort()

        message = 'Expected move list does not match actual move list'
        self.assertListEqual(expected_possible_moves, possible_moves, message)

        # Move knight to capture a piece
        move_result = board.move_piece(start_position, capture_position)
        message = 'Knight should have captured piece on ' + capture_position + ' square'
        self.assertIsInstance(board[capture_position], Knight, message)

        # Test move result
        expected_move_result = {start_position: None, capture_position: Knight(Color.WHITE)}
        self.assertDictEqual(expected_move_result, move_result, 'Expected move result does not match actual')

    def test_bishop_capture(self):
        """
        Move a bishop to square where there is a piece of the opposite color on capture diagonal.
        Expected result is position with opponent piece is in legal move list and piece is captured
        when bishop moves to that position.
        :return:
        """
        board = ChessBoard()
        start_position = 'd4'
        capture_position = 'h8'
        board[start_position] = Bishop(Color.WHITE)
        board['c5'] = Queen(Color.BLACK)
        board[capture_position] = Pawn(Color.BLACK)
        expected_possible_moves = ['a1', 'b2', 'c3', 'c5', 'e3', 'e5', 'f2', 'f6', 'g1', 'g7', 'h8']
        possible_moves = board.get_legal_moves(start_position)
        possible_moves.sort()

        message = 'Expected move list does not match actual move list'
        self.assertListEqual(expected_possible_moves, possible_moves, message)

        # Move bishop to capture a piece
        move_result = board.move_piece(start_position, capture_position)
        message = 'Bishop should have captured piece on ' + capture_position + ' square'
        self.assertIsInstance(board[capture_position], Bishop, message)

        # Test move result
        expected_move_result = {start_position: None, capture_position: Bishop(Color.WHITE)}
        self.assertDictEqual(expected_move_result, move_result, 'Expected move result does not match actual')

    def test_bishop_cant_capture(self):
        """
        Move bishop to square and place piece of same color in movement path.
        Expected result is that the square containing the piece of the same color is not in the list of legal
        moves.
        :return:
        """
        color_group = [Color.WHITE, Color.BLACK]
        for color in color_group:
            with self.subTest(color=color):
                board = ChessBoard()
                board['b2'] = Bishop(color)
                board['c3'] = Pawn(color)

                expected_moves = ['a1', 'a3', 'c1']
                legal_moves = board.get_legal_moves('b2')
                legal_moves.sort()
                self.assertListEqual(expected_moves, legal_moves, 'Expected list does not match actual legal move list')

    def test_king_capture(self):
        """
        Move king to square right next to piece of opposing color with nothing backing it up.
        Expected result is position with opponent piece is in legal move list and piece is captured
        when king moves to that position.
        :return:
        """
        board = ChessBoard()
        start_position = 'd4'
        capture_position = 'e4'
        board[start_position] = King(Color.WHITE)
        board[capture_position] = Pawn(Color.BLACK)

        expected_legal_moves = ['c3', 'c4', 'c5', 'd5', 'e3', 'e4', 'e5']
        possible_moves = board.get_legal_moves(start_position)
        possible_moves.sort()

        self.assertListEqual(expected_legal_moves, possible_moves, 'Expected move list does not match actual move list')

        # Move king to capture a piece
        move_result = board.move_piece(start_position, capture_position)
        message = 'King should have captured piece on ' + capture_position + ' square'
        self.assertIsInstance(board[capture_position], King, message)

        # Test move result
        expected_move_result = {start_position: None, capture_position: King(Color.WHITE)}
        self.assertDictEqual(expected_move_result, move_result, 'Expected move result does not match actual')

    def test_king_cant_capture(self):
        """
        Test a few scenarios where the king cannot capture another piece.
        Expected result is piece next to king cannot be captured and will not be in legal moves list.
        :return:
        """
        # Test scenario where opponent piece backing up other opponent piece.
        board = ChessBoard()
        start_position = 'd4'
        capture_position = 'd5'
        board[start_position] = King(Color.WHITE)
        board['e4'] = Pawn(Color.BLACK)
        board[capture_position] = Pawn(Color.BLACK)

        expected_legal_moves = ['c3', 'c5', 'd5', 'e3', 'e5']
        legal_moves = board.get_legal_moves(start_position)
        legal_moves.sort()

        self.assertListEqual(expected_legal_moves, legal_moves, 'Expected move list does not match actual move list')

        # Test king has piece of same color directly in front of it
        board = ChessBoard()
        board['d4'] = King(Color.WHITE)
        board['d5'] = Pawn(Color.WHITE)

        expected_legal_moves = ['c3', 'c4', 'c5', 'd3', 'e3', 'e4', 'e5']
        legal_moves = board.get_legal_moves('d4')
        legal_moves.sort()

        self.assertListEqual(expected_legal_moves, legal_moves, 'Expected move list does not match actual move list')

    def test_queen_capture(self):
        """
        Move queen to position where an opponents piece is in the capture path.
        Expected result is opponents piece is in legal move list and piece is captured when queen moves to that
        position.
        :return:
        """
        board = ChessBoard()
        start_position = 'd4'
        capture_position = 'e4'
        board[start_position] = Queen(Color.WHITE)
        board['d5'] = Pawn(Color.BLACK)
        board[capture_position] = Pawn(Color.BLACK)
        expected_possible_moves = ['a1', 'a4', 'a7', 'b2', 'b4', 'b6', 'c3', 'c4', 'c5', 'd1',
                                   'd2', 'd3', 'd5', 'e3', 'e4', 'e5', 'f2', 'f6', 'g1', 'g7', 'h8']
        possible_moves = board.get_legal_moves(start_position)
        possible_moves.sort()

        message = 'Expected move list does not match actual move list'
        self.assertListEqual(expected_possible_moves, possible_moves, message)

        # Move queen to capture a piece
        move_result = board.move_piece(start_position, capture_position)
        message = 'Queen should have captured piece on ' + capture_position + ' square'
        self.assertIsInstance(board[capture_position], Queen, message)

        # Test move result
        expected_move_result = {start_position: None, capture_position: Queen(Color.WHITE)}
        self.assertDictEqual(expected_move_result, move_result, 'Expected move result does not match actual')

    def test_queen_cant_capture(self):
        """
        Move queen to a square and place piece of same color in movement path.
        Expected result is that the square containing the piece of the same color is not in the list of legal
        moves.
        :return:
        """
        board = ChessBoard()
        board['b2'] = Queen(Color.WHITE)
        board['b3'] = Pawn(Color.WHITE)

        expected_legal_moves = ['a1', 'a2', 'a3', 'b1', 'c1',
                                'c2', 'c3', 'd2', 'd4', 'e2',
                                'e5', 'f2', 'f6', 'g2', 'g7',
                                'h2', 'h8']
        legal_moves = board.get_legal_moves('b2')
        legal_moves.sort()

        self.assertListEqual(expected_legal_moves, legal_moves, 'Expected move list does not match actual')

    def test_en_passant_capture(self):
        """
        Test capturing an opponents pawn via en passant.
        Expected result is opponents piece is successfully captured when en passant move is performed.
        :return:
        """
        board = ChessBoard()

        # Check from white perspective
        board['b5'] = Pawn(Color.WHITE)
        board['a7'] = Pawn(Color.BLACK)
        board.move_piece('a7', 'a5')
        move_result = board.move_piece('b5', 'a6')
        self.assertIsNone(board['a5'], 'Expected black pawn to be captured')

        # Test move result
        expected_move_result = {'b5': None, 'a5': None, 'a6': Pawn(Color.WHITE)}
        self.assertDictEqual(expected_move_result, move_result, 'Expected move result does not match actual')

        # Check from black perspective
        board['e4'] = Pawn(Color.BLACK)
        board['d2'] = Pawn(Color.WHITE)
        board.move_piece('d2', 'd4')
        move_result = board.move_piece('e4', 'd3')
        self.assertIsNone(board['d4'], 'Expected black pawn to be captured')

        # Test move result
        expected_move_result = {'e4': None, 'd4': None, 'd3': Pawn(Color.BLACK)}
        self.assertDictEqual(expected_move_result, move_result, 'Expected move result does not match actual')


if __name__ == '__main__':
    unittest.main()
