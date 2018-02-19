import unittest
from src.board.chess_board import ChessBoard
from src.piece.king import King
from src.piece.pawn import Pawn
from src.piece.queen import Queen
from src.piece.bishop import Bishop
from src.piece.knight import Knight
from src.piece.rook import Rook
from src.piece.color import Color
from src.board.fen import Fen
from src.piece.move_direction import MoveDirection
from src.board.exception import *


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
                board = ChessBoard()
                board[pawn_position] = Pawn(Color.BLACK)
                board[king_position] = King(Color.WHITE)
                self.assertTrue(board.is_check(Color.WHITE), 'Pawn should put king in check')

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
                board = ChessBoard()
                board[knight_position] = Knight(Color.BLACK)
                board[king_position] = King(Color.WHITE)
                self.assertTrue(board.is_check(Color.WHITE), 'Knight should put king in check')

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
                board = ChessBoard()
                board[bishop_position] = Bishop(Color.BLACK)
                board[king_position] = King(Color.WHITE)
                self.assertTrue(board.is_check(Color.WHITE), 'Bishop should put king in check')

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
                board = ChessBoard()
                board[rook_position] = Rook(Color.BLACK)
                board[king_position] = King(Color.WHITE)
                self.assertTrue(board.is_check(Color.WHITE), 'Rook should put king in check')

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
                board = ChessBoard()
                board[queen_position] = Queen(Color.BLACK)
                board[king_position] = King(Color.WHITE)
                self.assertTrue(board.is_check(Color.WHITE), 'Queen should put king in check')

    def test_pawn_checkmate(self):
        """
        Test that a pawn will put a king of the opposite color in checkmate
        :return:
        """
        board = ChessBoard()
        board['a1'] = King(Color.WHITE)
        board['a2'] = Pawn(Color.WHITE)
        board['b1'] = Bishop(Color.WHITE)
        board['b2'] = Pawn(Color.BLACK)
        board['c3'] = Pawn(Color.BLACK)
        self.assertTrue(board.is_checkmate(Color.WHITE), 'King should be in checkmate')

    def test_rook_checkmate(self):
        """
        Test that a rook will put a king of the opposite color in checkmate
        :return:
        """
        board = ChessBoard()
        board['a3'] = King(Color.WHITE)
        board['a5'] = Rook(Color.BLACK)
        board['b8'] = Rook(Color.BLACK)
        self.assertTrue(board.is_checkmate(Color.WHITE), 'King should be in checkmate')

    def test_knight_checkmate(self):
        """
        Test that a knight will put a king of the opposite color in checkmate
        :return:
        """
        board = ChessBoard()
        board['b4'] = Bishop(Color.BLACK)
        board['c5'] = Rook(Color.BLACK)
        board['d1'] = King(Color.WHITE)
        board['e3'] = Knight(Color.BLACK)
        board['f3'] = Pawn(Color.BLACK)
        self.assertTrue(board.is_checkmate(Color.WHITE), 'King should be in checkmate')

    def test_bishop_checkmate(self):
        """
        Test that a queen will put a king of the opposite color in checkmate
        :return:
        """
        board = ChessBoard()
        board['a8'] = King(Color.WHITE)
        board['a6'] = Knight(Color.BLACK)
        board['b6'] = King(Color.BLACK)
        board['c6'] = Bishop(Color.BLACK)
        self.assertTrue(board.is_checkmate(Color.WHITE), 'King should be in checkmate')

    def test_queen_checkmate(self):
        """
        Test that a queen will put a king of the opposite color in checkmate
        :return:
        """
        board = ChessBoard()
        board['d6'] = King(Color.BLACK)
        board['c5'] = Pawn(Color.BLACK)
        board['e5'] = Pawn(Color.BLACK)
        board['a5'] = Bishop(Color.WHITE)
        board['d5'] = Queen(Color.WHITE)
        board['d2'] = Rook(Color.WHITE)
        board['g6'] = Knight(Color.WHITE)
        self.assertTrue(board.is_checkmate(Color.BLACK), 'King should be in checkmate')

    def test_is_stalemate(self):
        """
        Test case where it is a players move and they have no valid moves left.
        Expected result is a stalemate has occurred.
        :return:
        """
        board = ChessBoard()
        board['a1'] = King(Color.BLACK)
        board['b4'] = Rook(Color.WHITE)
        board['c2'] = King(Color.WHITE)
        board['c4'] = Bishop(Color.WHITE)

        is_stalemate = board.is_stalemate(Color.BLACK)
        self.assertTrue(is_stalemate, 'Board configuration should result in stalemate')

    def test_is_not_stalemate(self):
        """
        Configure board where white player has one legal move.
        Expected result is stalemate has not occurred.
        :return:
        """
        # Try for king
        board = ChessBoard()
        board['a8'] = King(Color.BLACK)
        board['c1'] = Rook(Color.WHITE)
        board['d7'] = Rook(Color.WHITE)

        is_stalemate = board.is_stalemate(Color.BLACK)
        self.assertFalse(is_stalemate, 'Board configuration should not result in stalemate')

        # Try for piece other than king
        board = ChessBoard()
        board['a8'] = King(Color.BLACK)
        board['b1'] = Rook(Color.WHITE)
        board['d7'] = Rook(Color.WHITE)
        board['f2'] = Pawn(Color.BLACK)

        is_stalemate = board.is_stalemate(Color.BLACK)
        self.assertFalse(is_stalemate, 'Board configuration should not result in stalemate')

    def test_can_en_passant(self):
        """
        Test that a pawn can perform en passant move.
        :return:
        """
        board = ChessBoard()

        # En passant from white's perspective.
        board['b5'] = Pawn(Color.WHITE)
        board['a7'] = Pawn(Color.BLACK)
        board.move_piece('a7', 'a5')
        self.assertTrue(board.can_en_passant('b5', MoveDirection.F_LEFT_DIAG), 'Pawn should be able to perform en passant')

        # En passant from black's perspective.
        board['g4'] = Pawn(Color.BLACK)
        board['h2'] = Pawn(Color.WHITE)
        board.move_piece('h2', 'h4')
        self.assertTrue(board.can_en_passant('g4', MoveDirection.F_LEFT_DIAG), 'Pawn should be able to perform en passant')

    def test_cannot_en_passant(self):
        """
        Test that a pawn cannot perform en passant move.
        :return:
        """
        board = ChessBoard()

        # Confirm pawn that just moved 2 spaces can't perform enpassant.
        board['b5'] = Pawn(Color.WHITE)
        board['a7'] = Pawn(Color.BLACK)
        board.move_piece('a7', 'a5')
        self.assertFalse(board.can_en_passant('a5', MoveDirection.F_LEFT_DIAG), 'Pawn should not be able to perform en passant')

        # Confirm when all condition have been met but push pawn moved one square twice, en passant can't happen.
        board['g4'] = Pawn(Color.BLACK)
        board['h2'] = Pawn(Color.WHITE)
        board.move_piece('h2', 'h3')
        board.move_piece('h3', 'h4')
        self.assertFalse(board.can_en_passant('g4', MoveDirection.F_LEFT_DIAG), 'Pawn should be able to perform en passant')

    def test_can_castle(self):
        """
        Test that a king can perform a castle
        :return:
        """
        board = ChessBoard()

        # Check from white perspective
        board['a1'] = Rook(Color.WHITE)
        board['e1'] = King(Color.WHITE)
        board['h1'] = Rook(Color.WHITE)
        self.assertTrue(board.can_castle(Color.WHITE, MoveDirection.LEFT), 'King should be able to castle')
        self.assertTrue(board.can_castle(Color.WHITE, MoveDirection.RIGHT), 'King should be able to castle')

        # Check from black perspective
        board['a8'] = Rook(Color.BLACK)
        board['e8'] = King(Color.BLACK)
        board['h8'] = Rook(Color.BLACK)
        self.assertTrue(board.can_castle(Color.BLACK, MoveDirection.LEFT), 'King should be able to castle')
        self.assertTrue(board.can_castle(Color.BLACK, MoveDirection.RIGHT), 'King should be able to castle')

    def test_cannot_castle(self):
        """
        Test cases where a king cannot castle.
        Expected result is king cannot castle through check, from check, into check, after moving, if
        the rook has moved.
        :return:
        """
        # Check case where king would pass through check
        board = ChessBoard()
        board['a1'] = Rook(Color.WHITE)
        board['e1'] = King(Color.WHITE)
        board['d5'] = Rook(Color.BLACK)

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
        board = ChessBoard()
        board['a1'] = Rook(Color.WHITE)
        board['e1'] = King(Color.WHITE)
        board.move_piece('e1', 'd1')

        expected_moves = ['c1', 'c2', 'd2', 'e1', 'e2']
        legal_moves = board.get_legal_moves('d1')
        legal_moves.sort()
        self.assertListEqual(expected_moves, legal_moves, 'Expected moves does not match actual')

        # Check after left rook moves
        board = ChessBoard()
        board['a1'] = Rook(Color.WHITE)
        board['e1'] = King(Color.WHITE)
        board.move_piece('a1', 'b1')

        expected_moves = ['d1', 'd2', 'e2', 'f1', 'f2']
        legal_moves = board.get_legal_moves('e1')
        legal_moves.sort()
        self.assertListEqual(expected_moves, legal_moves, 'Expected moves does not match actual')

        # Check after right rook moves
        board = ChessBoard()
        board['e1'] = King(Color.WHITE)
        board['h1'] = Rook(Color.WHITE)
        board.move_piece('h1', 'h2')

        expected_moves = ['d1', 'd2', 'e2', 'f1', 'f2']
        legal_moves = board.get_legal_moves('e1')
        legal_moves.sort()
        self.assertListEqual(expected_moves, legal_moves, 'Expected moves does not match actual')

        # Check with both rooks after right rook moves
        board = ChessBoard()
        board['a1'] = Rook(Color.WHITE)
        board['e1'] = King(Color.WHITE)
        board['h1'] = Rook(Color.WHITE)
        board.move_piece('h1', 'h2')

        expected_moves = ['c1','d1', 'd2', 'e2', 'f1', 'f2']
        legal_moves = board.get_legal_moves('e1')
        legal_moves.sort()
        self.assertListEqual(expected_moves, legal_moves, 'Expected moves does not match actual')

        # Check with both rooks after right rook moves
        board = ChessBoard()
        board['a1'] = Rook(Color.WHITE)
        board['e1'] = King(Color.WHITE)
        board['h1'] = Rook(Color.WHITE)
        board.move_piece('a1', 'b1')

        expected_moves = ['d1', 'd2', 'e2', 'f1', 'f2', 'g1']
        legal_moves = board.get_legal_moves('e1')
        legal_moves.sort()
        self.assertListEqual(expected_moves, legal_moves, 'Expected moves does not match actual')

        # Confirm cannot castle even if king and rooks back in starting positions
        fen = Fen('r3k2r/8/8/8/8/8/8/8 b - -')
        board = ChessBoard(fen)

        can_castle_left = board.can_castle(Color.BLACK, MoveDirection.LEFT)
        can_castle_right = board.can_castle(Color.BLACK, MoveDirection.RIGHT)
        self.assertFalse(can_castle_left, 'King should not be able to castle left')
        self.assertFalse(can_castle_right, 'King should not be able to castle right')


if __name__ == '__main__':
    unittest.main()
