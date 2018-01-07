import unittest


class MoveResultTest(unittest.TestCase):
    def test_captured_position_in_positions_list(self):
        """
        Capture an opponent piece.
        Expected result is old position is listed as empty and capture position contains piece doing the capture.
        :return:
        """
        pass

    def test_newly_occupied_position_in_positions_list(self):
        """
        Move a piece from one position to another.
        Expected result is old position is listed as empty and newly occupied position list new piece.
        :return:
        """
        pass

    def test_pawn_promotion(self):
        """
        Move a pawn from starting position to the end of the board.
        Expected result is pawn can be promoted to any piece other than a king.
        :return:
        """
        pass
