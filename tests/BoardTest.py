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
        pass

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

    # def test_queen_checkmate(self):
    #     """
    #     Test that a queen will put a king of the opposite color in checkmate
    #     :return:
    #     """
    #     board = ChessBoard(empty_board=True)
    #     board['d6'] = King(Color.black)
    #     board['c5'] = Pawn(Color.black)
    #     board['e5'] = Pawn(Color.black)
    #     board['a5'] = Bishop(Color.white)
    #     board['d5'] = Queen(Color.white)
    #     board['d2'] = Rook(Color.white)
    #     board['g6'] = Knight(Color.white)
    #     self.assertTrue(board.is_checkmate(Color.black), 'King should be in checkmate')


    def test_stalemate(self):
        pass

    def test_en_passant(self):
        pass

    def test_possible_squares(self):
        # Bottom left corner
        board = ChessBoard(empty_board=True)
        start_position = 'a1'
        directions = {MoveDirection.forward: ['a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8'],
                      MoveDirection.f_right_diag: ['b2', 'c3', 'd4', 'e5', 'f6', 'g7', 'h8'],
                      MoveDirection.right: ['b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h1'],
                      MoveDirection.b_right_diag: [],
                      MoveDirection.backward: [],
                      MoveDirection.b_left_diag: [],
                      MoveDirection.left: [],
                      MoveDirection.f_left_diag: [],
                      MoveDirection.l_shape: ['b3', 'c2']
                      }
        for move_direction, expected_possible_squares in directions.items():
            with self.subTest(move_direction=move_direction, expected_possible_squares=expected_possible_squares):
                actual_possible_squares = board.get_possible_positions(start_position, move_direction, Color.white)

                if move_direction == MoveDirection.l_shape:
                    actual_possible_squares.sort()
                message = 'Expected squares do not match actual squares'
                self.assertListEqual(expected_possible_squares, actual_possible_squares, message)

        # Top right corner
        board = ChessBoard(empty_board=True)
        start_position = 'h8'
        directions = {MoveDirection.forward: [],
                      MoveDirection.f_right_diag: [],
                      MoveDirection.right: [],
                      MoveDirection.b_right_diag: [],
                      MoveDirection.backward: ['h7', 'h6', 'h5', 'h4', 'h3', 'h2', 'h1'],
                      MoveDirection.b_left_diag: ['g7', 'f6', 'e5', 'd4', 'c3', 'b2', 'a1'],
                      MoveDirection.left: ['g8', 'f8', 'e8', 'd8', 'c8', 'b8', 'a8'],
                      MoveDirection.f_left_diag: [],
                      MoveDirection.l_shape: ['f7', 'g6']
                      }
        for move_direction, expected_possible_squares in directions.items():
            with self.subTest(move_direction=move_direction, expected_possible_squares=expected_possible_squares):
                actual_possible_squares = board.get_possible_positions(start_position, move_direction, Color.white)

                if move_direction == MoveDirection.l_shape:
                    actual_possible_squares.sort()
                message = 'Expected squares do not match actual squares'
                self.assertListEqual(expected_possible_squares, actual_possible_squares, message)

        # Middle square
        board = ChessBoard(empty_board=True)
        start_position = 'd4'
        directions = {MoveDirection.forward: ['d5', 'd6', 'd7', 'd8'],
                      MoveDirection.f_right_diag: ['e5', 'f6', 'g7', 'h8'],
                      MoveDirection.right: ['e4', 'f4', 'g4', 'h4'],
                      MoveDirection.b_right_diag: ['e3', 'f2', 'g1'],
                      MoveDirection.backward: ['d3', 'd2', 'd1'],
                      MoveDirection.b_left_diag: ['c3', 'b2', 'a1'],
                      MoveDirection.left: ['c4', 'b4', 'a4'],
                      MoveDirection.f_left_diag: ['c5', 'b6', 'a7'],
                      MoveDirection.l_shape: ['b3', 'b5', 'c2', 'c6', 'e2', 'e6', 'f3', 'f5']
                      }
        for move_direction, expected_possible_squares in directions.items():
            with self.subTest(move_direction=move_direction, expected_possible_squares=expected_possible_squares):
                actual_possible_squares = board.get_possible_positions(start_position, move_direction, Color.white)

                if move_direction == MoveDirection.l_shape:
                    actual_possible_squares.sort()
                message = 'Expected squares do not match actual squares'
                self.assertListEqual(expected_possible_squares, actual_possible_squares, message)