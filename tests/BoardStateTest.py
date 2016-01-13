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