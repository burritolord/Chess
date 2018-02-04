import unittest
from src.piece.king import King
from src.piece.pawn import Pawn
from src.piece.queen import Queen
from src.piece.bishop import Bishop
from src.piece.knight import Knight
from src.piece.rook import Rook
from src.piece.move_direction import MoveDirection
from src.piece.color import Color
from src.piece.type import Type


class PieceTest(unittest.TestCase):
    """
    Test piece attributes
    """

    def setUp(self):
        self.types = {
            Type.PAWN: Pawn,
            Type.BISHOP: Bishop,
            Type.KING: King,
            Type.KNIGHT: Knight,
            Type.QUEEN: Queen,
            Type.ROOK: Rook
        }

    def test_create(self):
        """
        Test the creation of pieces and the states
        :return:
        """
        for t, piece_class in self.types.items():
            with self.subTest(t):
                piece = piece_class(Color.WHITE)
                self.assertEqual(Color.WHITE, piece.color, 'Color was not set correctly')
                self.assertEqual(t, piece.type, 'Piece type does not match')

    def test_capture(self):
        """
        Test capture property
        :return:
        """
        for t, piece_class in self.types.items():
            with self.subTest(t):
                piece = piece_class(Color.WHITE)
                self.assertFalse(piece.capture, 'Piece should not be captured')

                piece.capture = True
                self.assertTrue(piece.capture, 'Piece should not be captured')

    def test_move_directions(self):
        """
        Test move directions per piece
        :return:
        """
        piece_directions = {
            Type.PAWN: {MoveDirection.FORWARD: 2,
                        MoveDirection.F_RIGHT_DIAG: 1,
                        MoveDirection.F_LEFT_DIAG: 1},
            Type.BISHOP: {MoveDirection.F_LEFT_DIAG: -1,
                          MoveDirection.F_RIGHT_DIAG: -1,
                          MoveDirection.B_RIGHT_DIAG: -1,
                          MoveDirection.B_LEFT_DIAG: -1},
            Type.KING: {MoveDirection.FORWARD: 1,
                        MoveDirection.F_RIGHT_DIAG: 1,
                        MoveDirection.RIGHT: 2,
                        MoveDirection.B_RIGHT_DIAG: 1,
                        MoveDirection.BACKWARD: 1,
                        MoveDirection.B_LEFT_DIAG: 1,
                        MoveDirection.LEFT: 2,
                        MoveDirection.F_LEFT_DIAG: 1},
            Type.KNIGHT: {MoveDirection.L_SHAPE: True},
            Type.QUEEN: {MoveDirection.FORWARD: -1,
                         MoveDirection.F_RIGHT_DIAG: -1,
                         MoveDirection.RIGHT: -1,
                         MoveDirection.B_RIGHT_DIAG: -1,
                         MoveDirection.BACKWARD: -1,
                         MoveDirection.B_LEFT_DIAG: -1,
                         MoveDirection.LEFT: -1,
                         MoveDirection.F_LEFT_DIAG: -1},
            Type.ROOK: {MoveDirection.FORWARD: -1,
                        MoveDirection.RIGHT: -1,
                        MoveDirection.BACKWARD: -1,
                        MoveDirection.LEFT: -1}
        }
        for t, piece_class in self.types.items():
            with self.subTest(t):
                piece = piece_class(Color.WHITE)
                directions = piece.move_directions
                self.assertDictEqual(piece_directions[t], directions, 'Directions do not match expected')


if __name__ == '__main__':
    unittest.main()
