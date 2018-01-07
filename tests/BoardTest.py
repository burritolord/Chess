import unittest
from board.ChessBoard import ChessBoard
from piece.King import King
from piece.Pawn import Pawn
from piece.Queen import Queen
from piece.Bishop import Bishop
from piece.Knight import Knight
from piece.Rook import Rook
from piece.Color import Color
from piece.MoveDirection import MoveDirection


class BoardStateTest(unittest.TestCase):

    def test_pawn_check(self):
        """
        Test that a pawn will put a king of the opposite color in check
        :return:
        """
        piece_positions = [('c2', 'b1'), ('a2', 'b1')]
        for positions in piece_positions:
            pawn_position, king_position = positions
            with self.subTest(pawn_position=pawn_position, king_position=king_position):
                board = ChessBoard(empty_board=True)
                board[pawn_position] = Pawn(Color.black)
                board[king_position] = King(Color.white)
                self.assertTrue(board.is_check(Color.white), 'Pawn should put king in check')

    def test_knight_check(self):
        """
        Test that a knight will put a king of the opposite color in check
        :return:
        """
        piece_positions = [('a1', 'b3'), ('a1', 'c2'),
                           ('d4', 'e6'), ('d4', 'f5'),
                           ('d4', 'f3'), ('d4', 'e2'),
                           ('d4', 'c2'), ('d4', 'b3'),
                           ('d4', 'b5'), ('d4', 'c6')]
        for positions in piece_positions:
            knight_position, king_position = positions
            with self.subTest(knight_position=knight_position, king_position=king_position):
                board = ChessBoard(empty_board=True)
                board[knight_position] = Knight(Color.black)
                board[king_position] = King(Color.white)
                self.assertTrue(board.is_check(Color.white), 'Knight should put king in check')

    def test_bishop_check(self):
        """
        Test that a bishop will put a king of the opposite color in check
        :return:
        """
        piece_positions = [('a1', 'h8'), ('a8', 'h1'),
                           ('h8', 'a1'), ('h1', 'a8')]
        for positions in piece_positions:
            bishop_position, king_position = positions
            with self.subTest(bishop_position=bishop_position, king_position=king_position):
                board = ChessBoard(empty_board=True)
                board[bishop_position] = Bishop(Color.black)
                board[king_position] = King(Color.white)
                self.assertTrue(board.is_check(Color.white), 'Bishop should put king in check')

    def test_rook_check(self):
        """
        Test that a rook will put a king of the opposite color in check
        :return:
        """
        piece_positions = [('a1', 'a8'), ('a1', 'h1'),
                           ('a8', 'a1'), ('a8', 'h8'),
                           ('h8', 'a8'), ('h8', 'h1'),
                           ('h1', 'a1'), ('h1', 'h8')]
        for positions in piece_positions:
            rook_position, king_position = positions
            with self.subTest(rook_position=rook_position, king_position=king_position):
                board = ChessBoard(empty_board=True)
                board[rook_position] = Rook(Color.black)
                board[king_position] = King(Color.white)
                self.assertTrue(board.is_check(Color.white), 'Rook should put king in check')

    def test_queen_check(self):
        """
        Test that a queen will put a king of the opposite color in check
        :return:
        """
        piece_positions = [('a1', 'a8'), ('a1', 'h1'), ('a1', 'h8'),
                           ('a8', 'a1'), ('a8', 'h8'), ('a8', 'h8'),
                           ('h8', 'a1'), ('h8', 'a8'), ('h8', 'h1'),
                           ('h1', 'a1'), ('h1', 'a8'), ('h1', 'h8')]
        for positions in piece_positions:
            queen_position, king_position = positions
            with self.subTest(queen_position=queen_position, king_position=king_position):
                board = ChessBoard(empty_board=True)
                board[queen_position] = Queen(Color.black)
                board[king_position] = King(Color.white)
                self.assertTrue(board.is_check(Color.white), 'Queen should put king in check')

    def test_pawn_checkmate(self):
        """
        Test that a pawn will put a king of the opposite color in checkmate
        :return:
        """
        board = ChessBoard(empty_board=True)
        board['a1'] = King(Color.white)
        board['a2'] = Pawn(Color.white)
        board['b1'] = Bishop(Color.white)
        board['b2'] = Pawn(Color.black)
        board['c3'] = Pawn(Color.black)
        self.assertTrue(board.is_checkmate(Color.white), 'King should be in checkmate')

    def test_rook_checkmate(self):
        """
        Test that a rook will put a king of the opposite color in checkmate
        :return:
        """
        board = ChessBoard(empty_board=True)
        board['a3'] = King(Color.white)
        board['a5'] = Rook(Color.black)
        board['b8'] = Rook(Color.black)
        self.assertTrue(board.is_checkmate(Color.white), 'King should be in checkmate')

    def test_knight_checkmate(self):
        """
        Test that a knight will put a king of the opposite color in checkmate
        :return:
        """
        board = ChessBoard(empty_board=True)
        board['b4'] = Bishop(Color.black)
        board['c5'] = Rook(Color.black)
        board['d1'] = King(Color.white)
        board['e3'] = Knight(Color.black)
        board['f3'] = Pawn(Color.black)
        self.assertTrue(board.is_checkmate(Color.white), 'King should be in checkmate')

    def test_bishop_checkmate(self):
        """
        Test that a queen will put a king of the opposite color in checkmate
        :return:
        """
        board = ChessBoard(empty_board=True)
        board['a8'] = King(Color.white)
        board['a6'] = Knight(Color.black)
        board['b6'] = King(Color.black)
        board['c6'] = Bishop(Color.black)
        self.assertTrue(board.is_checkmate(Color.white), 'King should be in checkmate')

    def test_queen_checkmate(self):
        """
        Test that a queen will put a king of the opposite color in checkmate
        :return:
        """
        board = ChessBoard(empty_board=True)
        board['d6'] = King(Color.black)
        board['c5'] = Pawn(Color.black)
        board['e5'] = Pawn(Color.black)
        board['a5'] = Bishop(Color.white)
        board['d5'] = Queen(Color.white)
        board['d2'] = Rook(Color.white)
        board['g6'] = Knight(Color.white)
        self.assertTrue(board.is_checkmate(Color.black), 'King should be in checkmate')

    def test_is_stalemate(self):
        """
        Test case where it is a players move and they have no valid moves left.
        Expected result is a stalemate has occurred.
        :return:
        """
        board = ChessBoard(empty_board=True)
        board['a1'] = King(Color.black)
        board['b4'] = Rook(Color.white)
        board['c2'] = King(Color.white)
        board['c4'] = Bishop(Color.white)

        is_stalemate = board.is_stalemate(Color.black)
        self.assertTrue(is_stalemate, 'Board configuration should result in stalemate')

    def test_is_not_stalemate(self):
        """
        Configure board where white player has one legal move.
        Expected result is stalemate has not occurred.
        :return:
        """
        # Try for king
        board = ChessBoard(empty_board=True)
        board['a8'] = King(Color.black)
        board['c1'] = Rook(Color.white)
        board['d7'] = Rook(Color.white)

        is_stalemate = board.is_stalemate(Color.black)
        self.assertFalse(is_stalemate, 'Board configuration should not result in stalemate')

        # Try for piece other than king
        board = ChessBoard(empty_board=True)
        board['a8'] = King(Color.black)
        board['b1'] = Rook(Color.white)
        board['d7'] = Rook(Color.white)
        board['f2'] = Pawn(Color.black)

        is_stalemate = board.is_stalemate(Color.black)
        self.assertFalse(is_stalemate, 'Board configuration should not result in stalemate')

    def test_can_en_passant(self):
        """
        Test that a pawn can perform en passant move.
        :return:
        """
        board = ChessBoard(empty_board=True)

        # En passant from white's perspective.
        board['b5'] = Pawn(Color.white)
        board['a7'] = Pawn(Color.black)
        board.move_piece('a7', 'a5')
        self.assertTrue(board.can_en_passant('b5', MoveDirection.f_left_diag), 'Pawn should be able to perform en passant')

        # En passant from black's perspective.
        board['g4'] = Pawn(Color.black)
        board['h2'] = Pawn(Color.white)
        board.move_piece('h2', 'h4')
        self.assertTrue(board.can_en_passant('g4', MoveDirection.f_left_diag), 'Pawn should be able to perform en passant')

    def test_cannot_en_passant(self):
        """
        Test that a pawn cannot perform en passant move.
        :return:
        """
        board = ChessBoard(empty_board=True)

        # Confirm pawn that just moved 2 spaces can't perform enpassant.
        board['b5'] = Pawn(Color.white)
        board['a7'] = Pawn(Color.black)
        board.move_piece('a7', 'a5')
        self.assertFalse(board.can_en_passant('a5', MoveDirection.f_left_diag), 'Pawn should not be able to perform en passant')

        # Confirm when all condition have been met but push pawn moved one square twice, en passant can't happen.
        board['g4'] = Pawn(Color.black)
        board['h2'] = Pawn(Color.white)
        board.move_piece('h2', 'h3')
        board.move_piece('h3', 'h4')
        self.assertFalse(board.can_en_passant('g4', MoveDirection.f_left_diag), 'Pawn should be able to perform en passant')

    def test_can_castle(self):
        """
        Test that a king can perform a castle
        :return:
        """
        board = ChessBoard(empty_board=True)

        # Check from white perspective
        board['a1'] = Rook(Color.white)
        board['e1'] = King(Color.white)
        board['h1'] = Rook(Color.white)
        self.assertTrue(board.can_castle(Color.white, MoveDirection.left), 'King should be able to castle')
        self.assertTrue(board.can_castle(Color.white, MoveDirection.right), 'King should be able to castle')

        # Check from black perspective
        board['a8'] = Rook(Color.black)
        board['e8'] = King(Color.black)
        board['h8'] = Rook(Color.black)
        self.assertTrue(board.can_castle(Color.black, MoveDirection.left), 'King should be able to castle')
        self.assertTrue(board.can_castle(Color.black, MoveDirection.right), 'King should be able to castle')

    def test_cannot_castle(self):
        """
        Test cases where a king cannot castle.
        Expected result is king cannot castle through check, from check, into check, after moving, if
        the rook has moved.
        :return:
        """
        # Check case where king would pass through check
        board = ChessBoard(empty_board=True)
        board['a1'] = Rook(Color.white)
        board['e1'] = King(Color.white)
        board['d5'] = Rook(Color.black)

        expected_moves = ['e2', 'f1', 'f2']
        legal_moves = board.get_legal_moves('e1')
        legal_moves.sort()
        self.assertListEqual(expected_moves, legal_moves, 'Expected moves does not match actual')

        # King in check
        board.move_piece('d5', 'e5')
        expected_moves = ['d1', 'd2', 'f1', 'f2']
        legal_moves = board.get_legal_moves('e1')
        legal_moves.sort()
        self.assertListEqual(expected_moves, legal_moves, 'Expected moves does not match actual')

        # King ends in check
        board.move_piece('e5', 'c5')
        expected_moves = ['d1', 'd2', 'e2', 'f1', 'f2']
        legal_moves = board.get_legal_moves('e1')
        legal_moves.sort()
        self.assertListEqual(expected_moves, legal_moves, 'Expected moves does not match actual')

        # Check after king moves
        board = ChessBoard(empty_board=True)
        board['a1'] = Rook(Color.white)
        board['e1'] = King(Color.white)
        board.move_piece('e1', 'd1')

        expected_moves = ['c1', 'c2', 'd2', 'e1', 'e2']
        legal_moves = board.get_legal_moves('d1')
        legal_moves.sort()
        self.assertListEqual(expected_moves, legal_moves, 'Expected moves does not match actual')

        # Check after rook moves
        board = ChessBoard(empty_board=True)
        board['a1'] = Rook(Color.white)
        board['e1'] = King(Color.white)
        board.move_piece('a1', 'b1')

        expected_moves = ['d1', 'd2', 'e2', 'f1', 'f2']
        legal_moves = board.get_legal_moves('e1')
        legal_moves.sort()
        self.assertListEqual(expected_moves, legal_moves, 'Expected moves does not match actual')

    def test_promoting_pawn(self):
        """
        Move a pawn from starting position all the way to the last row.
        Expected result is pawn can be promoted and once promoted, new piece is on position pawn was on. Promoted pawn
        should no longer exist on board.
        :return:
        """
        pass

    def test_cannot_promote_piece(self):
        """
        Test a couple scenarios where pawn cannot be promoted.
        Expected result is pawn will not be promoted when it is not on the last row and after it has already been
        promoted.
        :return:
        """
        pass


if __name__ == '__main__':
    unittest.main()
