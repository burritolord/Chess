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


class NumbersTest(unittest.TestCase):

    def setUp(self):
        self.board = ChessBoard(empty_board=True)

    def test_move_pawn(self):
        start_position = 'a1'
        end_position = 'a2'

        self.board[start_position] = Pawn(Color.white)
        self.assertFalse(self.board[start_position].has_moved, 'Pawn has never moved')

        self.board.move_piece(start_position, end_position)
        self.assertIsNone(self.board[start_position], 'There should no longer be a Pawn on square ' + start_position)
        self.assertIsInstance(self.board[end_position], Pawn, 'There should be a Pawn on square ' + end_position)
        self.assertTrue(self.board[end_position].has_moved, 'Pawn has moved')

    def test_move_queen(self):
        start_position = 'a1'
        end_position = 'c3'

        self.board[start_position] = Queen(Color.white)
        self.assertFalse(self.board[start_position].has_moved, 'Piece has never moved')
        self.assertIsNone(self.board[end_position], 'There should not be a piece on the destination square')

        self.board.move_piece(start_position, end_position)
        self.assertIsNone(self.board[start_position], 'There should no longer be a piece on square ' + start_position)
        self.assertIsInstance(self.board[end_position], Queen, 'There should be a piece on square ' + end_position)
        self.assertTrue(self.board[end_position].has_moved, 'Pawn has moved')

    def test_pawn_capture(self):
        start_position = 'a2'
        end_position = 'b3'

        self.board[start_position] = Queen(Color.white)
        moves = {Type.pawn: ['']}


        self.board[start_position] = Pawn(Color.white)

if __name__ == '__main__':
    unittest.main()