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

    def test_check(self):
        # Pawn

        # Bishop
        board = ChessBoard(empty_board=True)
        bishop = Bishop(Color.black)

        # Knight

        # Queen

        # Rook

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
                actual_possible_squares = board.get_possible_positions(start_position, move_direction)

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
                actual_possible_squares = board.get_possible_positions(start_position, move_direction)

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
                actual_possible_squares = board.get_possible_positions(start_position, move_direction)

                if move_direction == MoveDirection.l_shape:
                    actual_possible_squares.sort()
                message = 'Expected squares do not match actual squares'
                self.assertListEqual(expected_possible_squares, actual_possible_squares, message)