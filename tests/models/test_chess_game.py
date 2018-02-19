import unittest
from src.models.chess_game import ChessGame, MoveResult
from src.piece.color import Color
from src.models.player import Player
from src.piece.pawn import Pawn
from src.piece.rook import Rook
from src.piece.knight import Knight
from src.piece.queen import Queen
from src.piece.type import Type
from src.board.exception import *


class ChessGameTest(unittest.TestCase):

    def setUp(self):
        self.p1 = Player()
        self.p2 = Player()

    def test_current_player(self):
        """
        Move a piece as one player.
        Expected result is opposite colored player is the current player.
        :return:
        """
        p1 = Player()
        p2 = Player()
        game = ChessGame(white_player=p1, black_player=p2)
        current_player = game.current_player
        self.assertEqual(Color.WHITE, current_player.color)

        game.move_piece('d2', 'd4')
        current_player = game.current_player
        self.assertEqual(Color.BLACK, current_player.color)

        game.move_piece('d7', 'd5')
        current_player = game.current_player
        self.assertEqual(Color.WHITE, current_player.color)

    def test_move_result_updated_positions(self):
        """
        Move a piece as a player.
        Expected result is start position is empty and end position contains the moved piece.
        :return:
        """
        p1 = Player()
        p2 = Player()
        game = ChessGame(white_player=p1, black_player=p2)
        result = game.move_piece('d2', 'd4')

        expected_move_result = MoveResult()
        expected_move_result.update_positions = {'d2': None, 'd4': Pawn(Color.WHITE)}
        self.assertEqual(expected_move_result, result)

    def test_move_result_capture(self):
        """
        Perform piece capture.
        Expected result is move result states captured piece no longer on board, piece that moved is in new location,
        and previous location for piece that moved is empty.
        :return:
        """
        p1 = Player()
        p2 = Player()
        fen = 'rnbqkb1r/pppppppp/5n2/8/4P3/3P4/PPP2PPP/RNBQKBNR b KQkq -'
        game = ChessGame(fen=fen, white_player=p1, black_player=p2)
        result = game.move_piece('f6', 'e4')

        expected_move_result = MoveResult()
        expected_move_result.update_positions = {'f6': None, 'e4': Knight(Color.BLACK)}
        self.assertEqual(expected_move_result, result)

        result = game.move_piece('d3', 'e4')
        expected_move_result.update_positions = {'d3': None, 'e4': Pawn(Color.WHITE)}
        self.assertEqual(result, expected_move_result)

    def test_move_result_checkmate(self):
        """
        Move a piece to place the king in checkmate.
        Expected result is the king is placed in checkmate an the is_over flag is set to True.
        :return:
        """
        # Confirm checkmate and game_over flag set to True
        p1 = Player()
        p2 = Player()
        p1.color = Color.WHITE
        p2.color = Color.BLACK

        # Minimal
        fen = '8/8/8/8/6q1/3k4/8/4K3 b - -'
        game = ChessGame(fen=fen, white_player=p1, black_player=p2)
        self.assertFalse(game.is_over)

        result = game.move_piece('g4', 'e2')
        expected_move_result = MoveResult()
        expected_move_result.update_positions = {'g4': None, 'e2': Queen(Color.BLACK)}
        expected_move_result.king_in_checkmate = p1
        expected_move_result.king_in_check = p1
        self.assertEqual(expected_move_result, result)
        self.assertTrue(game.is_over)

        # Medium
        fen = '8/1r6/8/4k3/1q6/8/8/K7 b KQkq -'
        game = ChessGame(fen=fen, white_player=p1, black_player=p2)
        self.assertFalse(game.is_over)

        result = game.move_piece('b7', 'a7')
        expected_move_result = MoveResult()
        expected_move_result.update_positions = {'b7': None, 'a7': Rook(Color.BLACK)}
        expected_move_result.king_in_checkmate = p1
        expected_move_result.king_in_check = p1
        self.assertEqual(expected_move_result, result)
        self.assertTrue(game.is_over)

        # Complex
        fen = '8/3n4/4b3/2q1k3/K7/2P5/3RB1p1/8 b - -'
        game = ChessGame(fen=fen, white_player=p1, black_player=p2)
        self.assertFalse(game.is_over)

        result = game.move_piece('d7', 'b6')
        expected_move_result = MoveResult()
        expected_move_result.update_positions = {'d7': None, 'b6': Knight(Color.BLACK)}
        expected_move_result.king_in_checkmate = p1
        expected_move_result.king_in_check = p1
        self.assertEqual(expected_move_result, result)
        self.assertTrue(game.is_over)

    def test_move_result_pawn_promotion(self):
        p1 = Player()
        p2 = Player()
        p1.color = Color.WHITE
        p2.color = Color.BLACK

        fen = '8/P2n4/4b3/2q1k3/K7/8/3RB1p1/8 b - -'
        game = ChessGame(fen=fen, white_player=p1, black_player=p2)

        # Move black pawn
        result = game.move_piece('g2', 'g1')
        expected_move_result = MoveResult()
        expected_move_result.pawn_promote_info = {
            'player': p2,
            'promote_types': game.get_pawn_promote_types()
        }

        self.assertEqual(expected_move_result, result)

        result = game.promote_pawn('g2', 'g1', Type.QUEEN)
        expected_move_result = MoveResult()
        expected_move_result.update_positions = {'g2': None, 'g1': Queen(Color.BLACK)}
        self.assertEqual(expected_move_result, result)

        # Move white pawn
        result = game.move_piece('a7', 'a8')
        expected_move_result = MoveResult()
        expected_move_result.pawn_promote_info = {
            'player': p1,
            'promote_types': game.get_pawn_promote_types()
        }

        self.assertEqual(expected_move_result, result)

        result = game.promote_pawn('a7', 'a8', Type.KNIGHT)
        expected_promote_result = MoveResult()
        expected_promote_result.update_positions = {'a7': None, 'a8': Knight(Color.WHITE)}
        self.assertEqual(expected_promote_result, result)

    def test_pawn_capture_promotion(self):
        """
        Perform piece capture with a pawn that will place the pawn on the last row.
        Expected result is the pawn can be promoted.
        :return:
        """
        p1 = Player()
        p2 = Player()
        p1.color = Color.WHITE
        p2.color = Color.BLACK

        fen = '2b1k2r/5pP1/2n1p3/1P5p/3B1P2/2P3N1/7P/3RK3 w - -'
        game = ChessGame(fen=fen, white_player=p1, black_player=p2)

        # Capture the black pawn
        result = game.move_piece('g7', 'h8')

        expected_move_result = MoveResult()
        expected_move_result.pawn_promote_info = {
            'player': p1,
            'promote_types': game.get_pawn_promote_types()
        }
        self.assertEqual(expected_move_result, result)

        # Promote the piece and confirm move result
        result = game.promote_pawn('g7', 'h8', Type.QUEEN)
        expected_promote_result = MoveResult()
        expected_promote_result.update_positions = {'g7': None, 'h8': Queen(Color.WHITE)}
        expected_promote_result.king_in_check = p2
        self.assertEqual(expected_promote_result, result)

    def test_cannot_promote_pawn(self):
        """
        Move a pawn forward but not on last row.
        Expected result is pawn will not be promoted.
        :return:
        """
        p1 = Player()
        p2 = Player()
        p1.color = Color.WHITE
        p2.color = Color.BLACK

        fen = '8/1k6/8/8/8/6P1/3K4/8 w - -'
        game = ChessGame(fen=fen, white_player=p1, black_player=p2)
        result = game.move_piece('g3', 'g4')
        self.assertIsNone(result.pawn_promote_info)

        # Test boundary by moving pawn to second to last row
        fen = '8/1k6/6P1/8/8/8/3K4/8 w - -'
        game = ChessGame(fen=fen, white_player=p1, black_player=p2)
        result = game.move_piece('g6', 'g7')
        self.assertIsNone(result.pawn_promote_info)

    def test_move_result_king_in_check(self):
        """
        Put a king in check.
        Game should return the game state indicating which king is in check but game over flag is not set.
        :return:
        """
        p1 = Player()
        p2 = Player()
        p1.color = Color.WHITE
        p2.color = Color.BLACK

        fen = 'rnbqkbnr/ppp2ppp/4p3/3p4/8/2P5/PP1PPPPP/RNBQKBNR w KQkq -'
        game = ChessGame(fen=fen, white_player=p1, black_player=p2)
        self.assertFalse(game.is_over)

        result = game.move_piece('d1', 'a4')
        expected_promote_result = MoveResult()
        expected_promote_result.update_positions = {'d1': None, 'a4': Queen(Color.WHITE)}
        expected_promote_result.king_in_check = p2
        self.assertEqual(expected_promote_result, result)
        self.assertFalse(game.is_over)

    def test_move_result_draw(self):
        p1 = Player()
        p2 = Player()
        p1.color = Color.WHITE
        p2.color = Color.BLACK

        fen = 'k7/4K3/2N5/8/3R4/8/8/8 w - -'
        game = ChessGame(fen=fen, white_player=p1, black_player=p2)
        result = game.move_piece('d4', 'b4')
        expected_promote_result = MoveResult()
        expected_promote_result.update_positions = {'d4': None, 'b4': Rook(Color.WHITE)}
        expected_promote_result.draw = True

        self.assertEqual(expected_promote_result, result)
        self.assertTrue(game.is_over)

    def test_castle_info_stays_empty(self):
        """
        Use fen that states king cannot castle in one direction and both directions.
        Expected result is king cannot castle even if a rook and the king are put back in the positions where castling
        would be legal if they had not moved.
        :return:
        """
        p1 = Player()
        p2 = Player()
        p1.color = Color.WHITE
        p2.color = Color.BLACK

        # Both directions
        fen = 'r3k2r/3b2p1/2n1p1P1/1P5p/3B1P2/2P3N1/7P/3RK3 b - -'
        game = ChessGame(fen=fen, white_player=p1, black_player=p2)
        game.move_piece('h5', 'h4')
        expected_fen = 'r3k2r/3b2p1/2n1p1P1/1P6/3B1P1p/2P3N1/7P/3RK3 w - -'
        self.assertEqual(expected_fen, game.fen)

        # Left direction
        fen = 'r3k2r/3b2p1/2n1p1P1/1P5p/3B1P2/2P3N1/7P/3RK3 b k -'
        game = ChessGame(fen=fen, white_player=p1, black_player=p2)
        game.move_piece('h5', 'h4')
        expected_fen = 'r3k2r/3b2p1/2n1p1P1/1P6/3B1P1p/2P3N1/7P/3RK3 w k -'
        self.assertEqual(expected_fen, game.fen)

        # Right direction
        fen = 'r3k2r/3b2p1/2n1p1P1/1P5p/3B1P2/2P3N1/7P/3RK3 b q -'
        game = ChessGame(fen=fen, white_player=p1, black_player=p2)
        game.move_piece('h5', 'h4')
        expected_fen = 'r3k2r/3b2p1/2n1p1P1/1P6/3B1P1p/2P3N1/7P/3RK3 w q -'
        self.assertEqual(expected_fen, game.fen)

    def test_castle_info_updated(self):
        """
        Move the king, and not move the king but one or two rooks.
        Expected result is castle info in fen is updated appropriately.
        :return:
        """
        # Move king

        # Move right rook

        # Move left rook
        pass


    def test_invalid_algebraic_positions(self):
        """
        Test providing invalid algebraic notation for every method that expects it.
        Expected result is exception is thrown.
        :return:
        """
        pass


if __name__ == "__main__":
    unittest.main()
