import unittest
from board.ChessBoard import ChessBoard
from piece.King import King
from piece.Pawn import Pawn
from piece.Queen import Queen
from piece.Bishop import Bishop
from piece.Knight import Knight
from piece.Rook import Rook
from piece.Color import Color


class PieceLegalMovesTest(unittest.TestCase):

    def test_pawn_legal_moves(self):
        """
        Move a pawn to each corner and one middle square.
        Expected result is that all the possible moves match the expected list.
        :return:
        """
        start_positions = {
            Color.white: {
                'a1': ['a2', 'a3'],
                'a8': [],
                'h1': ['h2', 'h3'],
                'h8': [],
                'd4': ['d5', 'd6']
            },
            Color.black: {
                'a1': [],
                'a8': ['a6', 'a7'],
                'h1': [],
                'h8': ['h6', 'h7'],
                'd4': ['d2', 'd3']
            }
        }
        for color, positions in start_positions.items():
            for start_position, expected_moves in positions.items():
                with self.subTest(color=color, start_position=start_position, expected_moves=expected_moves):
                    board = ChessBoard(empty_board=True)
                    board[start_position] = Pawn(color)
                    possible_moves = board.get_legal_moves(start_position)
                    possible_moves.sort()

                    message = 'Expected move list does not match actual move list'
                    self.assertListEqual(expected_moves, possible_moves, message)

        # Confirm pawn can only move one square after it is moved
        board = ChessBoard(empty_board=True)
        board['a1'] = Pawn(Color.white)
        board.move_piece('a1', 'a3')
        possible_moves = board.get_legal_moves('a3')
        expected_possible_moves = ['a4']

        self.assertListEqual(expected_possible_moves, possible_moves, 'Pawn should not be able to ')

    def test_pawn_en_passant_legal_move(self):
        """
        Place pawn on 4th or 5th rank and move pawn of opposite color immediately to left or right of first pawn.
        Expected result is en passant move is present in legal move list for first pawn.
        :return:
        """
        piece_movements = {
            Color.white: [
                [('h2', 'h5'), ('g7', 'g5')],
                [('a2', 'a5'), ('b7', 'b5')]
            ],
            Color.black: [
                [('a7', 'a4'), ('b2', 'b4')],
                [('h7', 'h4'), ('g2', 'g4')]
            ]
        }
        expected_moves = {
            Color.white: {
                'h5': ['g6', 'h6'],
                'a5': ['a6', 'b6']
            },
            Color.black: {
                'a4': ['a3', 'b3'],
                'h4': ['g3', 'h3']
            }
        }
        for (c1, moves_for_color), (c2, expected_for_color) in zip(piece_movements.items(), expected_moves.items()):
            for piece_moves, (check_position, expected_list) in zip(moves_for_color, expected_for_color.items()):
                with self.subTest(piece_moves=piece_moves, check_position=check_position, expected_list=expected_list):
                    board = ChessBoard()
                    for movements in piece_moves:
                        start, end = movements
                        board.move_piece(start, end)

                    legal_moves = board.get_legal_moves(check_position)
                    legal_moves.sort()
                    self.assertListEqual(expected_list, legal_moves, 'En passant move should be in legal moves list')

    def test_pawn_legal_moves_piece_blocking(self):
        """
        Place a pawn on a square and another piece 2 positions in front of it.
        Expected result is there are is one legal move for the pawn that is blocked.
        :return:
        """
        opposing_colors = [[Color.black, Color.white], [Color.white, Color.black]]
        for opposing_color in opposing_colors:
            start_positions = ['b2', 'g7']
            blocking_positions = ['b4', 'g5']
            expected_moves = [['b3'], ['g6']]
            pawn_colors = [Color.white, Color.black]
            for start, blocking, expected, pawn_color, opposing in zip(start_positions, blocking_positions, expected_moves, pawn_colors, opposing_color):
                with self.subTest(start=start, blocking=blocking, expected=expected, pawn_color=pawn_color, opposing=opposing):
                    board = ChessBoard(empty_board=True)
                    board[start] = Pawn(pawn_color)
                    board[blocking] = Pawn(opposing)

                    legal_moves = board.get_legal_moves(start)
                    legal_moves.sort()

                    message = 'Pawn should only have one legal move'
                    self.assertListEqual(expected, legal_moves, message)

    def test_rook_legal_moves(self):
        """
        Move a rook to each corner and one middle square.
        Expected result is that all the possible moves match the expected list.
        :return:
        """
        start_positions = {
            Color.white: {
                'a1': ['a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h1'],
                'a8': ['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'b8', 'c8', 'd8', 'e8', 'f8', 'g8', 'h8'],
                'h1': ['a1', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'h8'],
                'h8': ['a8', 'b8', 'c8', 'd8', 'e8', 'f8', 'g8', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7'],
                'd4': ['a4', 'b4', 'c4', 'd1', 'd2', 'd3', 'd5', 'd6', 'd7', 'd8', 'e4', 'f4', 'g4', 'h4']
            },
            Color.black: {
                'a1': ['a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h1'],
                'a8': ['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'b8', 'c8', 'd8', 'e8', 'f8', 'g8', 'h8'],
                'h1': ['a1', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'h8'],
                'h8': ['a8', 'b8', 'c8', 'd8', 'e8', 'f8', 'g8', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7'],
                'd4': ['a4', 'b4', 'c4', 'd1', 'd2', 'd3', 'd5', 'd6', 'd7', 'd8', 'e4', 'f4', 'g4', 'h4']
            }
        }
        for color, positions in start_positions.items():
            for start_position, expected_moves in positions.items():
                with self.subTest(color=color, start_position=start_position, expected_moves=expected_moves):
                    board = ChessBoard(empty_board=True)
                    board[start_position] = Rook(color)
                    possible_moves = board.get_legal_moves(start_position)
                    possible_moves.sort()

                    message = 'Expected move list does not match actual move list'
                    self.assertListEqual(expected_moves, possible_moves, message)

    def test_knight_legal_moves(self):
        """
        Move a knight to each corner and one middle square.
        Expected result is that all the possible moves match the expected list.
        :return:
        """
        start_positions = {
            Color.white: {
                'a1': ['b3', 'c2'],
                'a8': ['b6', 'c7'],
                'h1': ['f2', 'g3'],
                'h8': ['f7', 'g6'],
                'd4': ['b3', 'b5', 'c2', 'c6', 'e2', 'e6', 'f3', 'f5'],
                'g7': ['e6', 'e8', 'f5', 'h5']
            },
            Color.black: {
                'a1': ['b3', 'c2'],
                'a8': ['b6', 'c7'],
                'h1': ['f2', 'g3'],
                'h8': ['f7', 'g6'],
                'd4': ['b3', 'b5', 'c2', 'c6', 'e2', 'e6', 'f3', 'f5'],
                'g7': ['e6', 'e8', 'f5', 'h5']
            }
        }
        for color, positions in start_positions.items():
            for start_position, expected_moves in positions.items():
                with self.subTest(color=color, start_position=start_position, expected_moves=expected_moves):
                    board = ChessBoard(empty_board=True)
                    board[start_position] = Knight(color)
                    possible_moves = board.get_legal_moves(start_position)
                    possible_moves.sort()

                    message = 'Expected move list does not match actual move list'
                    self.assertListEqual(expected_moves, possible_moves, message)

    def test_bishop_legal_moves(self):
        """
        Move a bishop to each corner and one middle square.
        Expected result is that all the possible moves match the expected list.
        :return:
        """
        start_positions = {
            Color.white: {
                'a1': ['b2', 'c3', 'd4', 'e5', 'f6', 'g7', 'h8'],
                'a8': ['b7', 'c6', 'd5', 'e4', 'f3', 'g2', 'h1'],
                'h1': ['a8', 'b7', 'c6', 'd5', 'e4', 'f3', 'g2'],
                'h8': ['a1', 'b2', 'c3', 'd4', 'e5', 'f6', 'g7'],
                'd4': ['a1', 'a7', 'b2', 'b6', 'c3', 'c5', 'e3', 'e5', 'f2', 'f6', 'g1', 'g7', 'h8']
            },
            Color.black: {
                'a1': ['b2', 'c3', 'd4', 'e5', 'f6', 'g7', 'h8'],
                'a8': ['b7', 'c6', 'd5', 'e4', 'f3', 'g2', 'h1'],
                'h1': ['a8', 'b7', 'c6', 'd5', 'e4', 'f3', 'g2'],
                'h8': ['a1', 'b2', 'c3', 'd4', 'e5', 'f6', 'g7'],
                'd4': ['a1', 'a7', 'b2', 'b6', 'c3', 'c5', 'e3', 'e5', 'f2', 'f6', 'g1', 'g7', 'h8']
            }
        }
        for color, positions in start_positions.items():
            for start_position, expected_moves in positions.items():
                with self.subTest(color=color, start_position=start_position, expected_moves=expected_moves):
                    board = ChessBoard(empty_board=True)
                    board[start_position] = Bishop(color)
                    possible_moves = board.get_legal_moves(start_position)
                    possible_moves.sort()

                    message = 'Expected move list does not match actual move list'
                    self.assertListEqual(expected_moves, possible_moves, message)

    def test_queen_legal_moves(self):
        """
        Move a queen to each corner and one middle square.
        Expected result is that all the possible moves match the expected list.
        :return:
        """
        start_positions = {
            Color.white: {
                'a1': ['a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8',
                       'b1', 'b2', 'c1', 'c3', 'd1', 'd4', 'e1',
                       'e5', 'f1', 'f6', 'g1', 'g7', 'h1', 'h8'],
                'a8': ['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7',
                       'b7', 'b8', 'c6', 'c8', 'd5', 'd8', 'e4',
                       'e8', 'f3', 'f8', 'g2', 'g8', 'h1', 'h8'],
                'h1': ['a1', 'a8', 'b1', 'b7', 'c1', 'c6', 'd1',
                       'd5', 'e1', 'e4', 'f1', 'f3', 'g1', 'g2',
                       'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'h8'],
                'h8': ['a1', 'a8', 'b2', 'b8', 'c3', 'c8', 'd4',
                       'd8', 'e5', 'e8', 'f6', 'f8', 'g7', 'g8',
                       'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7'],
                'd4': ['a1', 'a4', 'a7', 'b2', 'b4', 'b6', 'c3',
                       'c4', 'c5', 'd1', 'd2', 'd3', 'd5', 'd6',
                       'd7', 'd8', 'e3', 'e4', 'e5', 'f2', 'f4',
                       'f6', 'g1', 'g4', 'g7', 'h4', 'h8']
            },
            Color.black: {
                'a1': ['a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8',
                       'b1', 'b2', 'c1', 'c3', 'd1', 'd4', 'e1',
                       'e5', 'f1', 'f6', 'g1', 'g7', 'h1', 'h8'],
                'a8': ['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7',
                       'b7', 'b8', 'c6', 'c8', 'd5', 'd8', 'e4',
                       'e8', 'f3', 'f8', 'g2', 'g8', 'h1', 'h8'],
                'h1': ['a1', 'a8', 'b1', 'b7', 'c1', 'c6', 'd1',
                       'd5', 'e1', 'e4', 'f1', 'f3', 'g1', 'g2',
                       'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'h8'],
                'h8': ['a1', 'a8', 'b2', 'b8', 'c3', 'c8', 'd4',
                       'd8', 'e5', 'e8', 'f6', 'f8', 'g7', 'g8',
                       'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7'],
                'd4': ['a1', 'a4', 'a7', 'b2', 'b4', 'b6', 'c3',
                       'c4', 'c5', 'd1', 'd2', 'd3', 'd5', 'd6',
                       'd7', 'd8', 'e3', 'e4', 'e5', 'f2', 'f4',
                       'f6', 'g1', 'g4', 'g7', 'h4', 'h8']
            }
        }
        for color, positions in start_positions.items():
            for start_position, expected_moves in positions.items():
                with self.subTest(color=color, start_position=start_position, expected_moves=expected_moves):
                    board = ChessBoard(empty_board=True)
                    board[start_position] = Queen(color)
                    possible_moves = board.get_legal_moves(start_position)
                    possible_moves.sort()

                    message = 'Expected move list does not match actual move list'
                    self.assertListEqual(expected_moves, possible_moves, message)

    def test_king_legal_moves(self):
        """
        Move a king to each corner and one middle square.
        Expected result is that all the possible moves match the expected list.
        :return:
        """
        start_positions = {
            Color.white: {
                'a1': ['a2', 'b1', 'b2'],
                'a8': ['a7', 'b7', 'b8'],
                'h1': ['g1', 'g2', 'h2'],
                'h8': ['g7', 'g8', 'h7'],
                'd4': ['c3', 'c4', 'c5', 'd3', 'd5', 'e3', 'e4', 'e5']
            },
            Color.black: {
                'a1': ['a2', 'b1', 'b2'],
                'a8': ['a7', 'b7', 'b8'],
                'h1': ['g1', 'g2', 'h2'],
                'h8': ['g7', 'g8', 'h7'],
                'd4': ['c3', 'c4', 'c5', 'd3', 'd5', 'e3', 'e4', 'e5']
            }
        }
        for color, positions in start_positions.items():
            for start_position, expected_moves in positions.items():
                with self.subTest(color=color, start_position=start_position, expected_moves=expected_moves):
                    board = ChessBoard(empty_board=True)
                    board[start_position] = King(color)
                    possible_moves = board.get_legal_moves(start_position)
                    possible_moves.sort()

                    message = 'Expected move list does not match actual move list'
                    self.assertListEqual(expected_moves, possible_moves, message)

    def test_king_castle_legal_move(self):
        """
        Place king on starting square and rooks of the same color on their starting squares.
        Expected result is that queen side and king side castling is listed in legal moves list.
        :return:
        """
        board = ChessBoard(empty_board=True)
        board['a1'] = Rook(Color.white)
        board['e1'] = King(Color.white)
        board['a8'] = Rook(Color.black)
        board['e8'] = King(Color.black)

        # Try with just one rook.
        expected_legal_moves = {
            'e1': ['c1', 'd1', 'd2', 'e2', 'f1', 'f2'],
            'e8': ['c8', 'd7', 'd8', 'e7', 'f7', 'f8'],
        }
        for position, expected_moves in expected_legal_moves.items():
            with self.subTest(position=position, expected_moves=expected_moves):
                legal_moves = board.get_legal_moves(position)
                legal_moves.sort()
                self.assertListEqual(expected_moves, legal_moves, 'Castle move should be in legal move list')

        # Try with both rooks.
        board['h1'] = Rook(Color.white)
        board['h8'] = Rook(Color.black)
        expected_legal_moves = {
            'e1': ['c1', 'd1', 'd2', 'e2', 'f1', 'f2', 'g1'],
            'e8': ['c8', 'd7', 'd8', 'e7', 'f7', 'f8', 'g8'],
        }
        for position, expected_moves in expected_legal_moves.items():
            with self.subTest(position=position, expected_moves=expected_moves):
                legal_moves = board.get_legal_moves(position)
                legal_moves.sort()
                self.assertListEqual(expected_moves, legal_moves, 'Castle move should be in legal move list')

    def test_king_cant_put_self_in_check(self):
        """
        Place king in middle square. Place rook of opposing color on an immediate front right diagonal square.
        Expected result is the space directly to the right and in front of king is not in legal moves list.
        :return:
        """
        color_group = [(Color.white, Color.black), (Color.black, Color.white)]
        for group in color_group:
            with self.subTest(group=group):
                board = ChessBoard(empty_board=True)
                king_color, rook_color = group
                board['d4'] = King(king_color)
                board['e5'] = Rook(rook_color)

                expected_moves = ['c3', 'c4', 'd3', 'e5']
                legal_moves = board.get_legal_moves('d4')
                legal_moves.sort()
                self.assertListEqual(expected_moves, legal_moves, 'King should not be able to put self in check')

    def test_piece_pinned(self):
        """
        Test moving a piece of every type that is the same color as king but pinned by opponents piece.
        Expected result is legal move list for piece should be empty.
        :return:
        """
        # Pawn pined
        board = ChessBoard(empty_board=True)
        board['c3'] = King(Color.white)
        board['d4'] = Pawn(Color.white)
        board['f6'] = Bishop(Color.black)

        legal_moves = board.get_legal_moves('d4')
        self.assertListEqual([], legal_moves, 'Piece should not have any legal moves.')

        # Rook pined
        board = ChessBoard(empty_board=True)
        board['c3'] = King(Color.white)
        board['d4'] = Rook(Color.white)
        board['f6'] = Bishop(Color.black)

        legal_moves = board.get_legal_moves('d4')
        self.assertListEqual([], legal_moves, 'Piece should not have any legal moves.')

        # Knight pined
        board = ChessBoard(empty_board=True)
        board['c3'] = King(Color.white)
        board['d4'] = Knight(Color.white)
        board['f6'] = Bishop(Color.black)

        legal_moves = board.get_legal_moves('d4')
        self.assertListEqual([], legal_moves, 'Piece should not have any legal moves.')

        # Bishop pined
        board = ChessBoard(empty_board=True)
        board['c3'] = King(Color.white)
        board['c5'] = Bishop(Color.white)
        board['c6'] = Rook(Color.black)

        legal_moves = board.get_legal_moves('c5')
        self.assertListEqual([], legal_moves, 'Piece should not have any legal moves.')

        # Queen kinda pined
        board = ChessBoard(empty_board=True)
        board['c3'] = King(Color.white)
        board['c4'] = Queen(Color.white)
        board['c6'] = Rook(Color.black)

        legal_moves = board.get_legal_moves('c4')
        self.assertListEqual(['c5', 'c6'], legal_moves, 'Legal moves dont match expected moves.')


if __name__ == '__main__':
    unittest.main()
