__author__ = 'nick.james'
from Pawn import Pawn
from Rook import Rook
from Knight import Knight
from Bishop import Bishop
from King import King
from Queen import Queen
from Color import Color
from Type import Type
from MoveDirection import MoveDirection


class ChessBoard:

    PIECE_SHIFTING = {
        MoveDirection.forward: 8,
        MoveDirection.backward: -8,
        MoveDirection.left: -1,
        MoveDirection.right: 1,
        MoveDirection.f_left_diag: 7,
        MoveDirection.f_right_diag: 9,
        MoveDirection.b_left_diag: -7,
        MoveDirection.b_right_diag: -9,
        MoveDirection.l_shape: [-17, -15, -10, -6, 6, 10, 15, 17]
    }

    def __init__(self):
        """
        Create a ChessBoard object with all pieces in starting position
        :return:
        """
        self._board_positions = [y+str(x+1) for x in range(0, 8) for y in "abcdefgh"]
        self._pieces = {y+str(x+1): None for x in range(0, 8) for y in "abcdefgh"}
        self._indexes = {}
        for position, index in zip(self._board_positions, range(0, 64)):
            self._indexes[position] = index

        # Set the starting pieces for white
        for index in range(8, 16):
            self._pieces[self._board_positions[index]] = Pawn(Color.white)
        self._pieces['a1'], self._pieces['h1'] = Rook(Color.white), Rook(Color.white)
        self._pieces['b1'], self._pieces['g1'] = Knight(Color.white), Knight(Color.white)
        self._pieces['c1'], self._pieces['f1'] = Bishop(Color.white), Bishop(Color.white)
        self._pieces['d1'] = Queen(Color.white)
        self._pieces['e1'] = King(Color.white)

        # Set the starting pieces for black
        for index in range(48, 56):
            self._pieces[self._board_positions[index]] = Pawn(Color.black)
        self._pieces['a8'], self._pieces['h8'] = Rook(Color.black), Rook(Color.black)
        self._pieces['b8'], self._pieces['g8'] = Knight(Color.black), Knight(Color.black)
        self._pieces['c8'], self._pieces['f8'] = Bishop(Color.black), Bishop(Color.black)
        self._pieces['d8'] = Queen(Color.black)
        self._pieces['e8'] = King(Color.black)

        self._king_positions = {Color.white: 'e1', Color.black: 'e8'}

    def get_piece(self, position):
        """
        Get the piece at the specified position.

        :param position: String Starting position to check from.
        :return: Piece | None
        """
        try:
            self._indexes[position]
        except IndexError:
            return None
        return self._pieces[position]

    def is_position_occupied(self, position):
        """
        Check if the position is occupied with a piece.
        :param position: String
            Position to test.
        :return:
        """
        try:
            self._indexes[position]
        except IndexError:
            raise Exception(position + " is not a valid position")
        return self._pieces[position] is not None

    def is_check(self, color):
        """
        Test for check against king of the specified color.

        :param color: Color
            Color of king to test for check against.
        :return: bool
            True if king is in check, False otherwise.
        """
        check = False
        # opponent_color = Color.black if color == Color.white else Color.black
        king_position = self._king_positions[color]

        # Check file and rank
        file_and_rank_pieces = (Type.queen, Type.rook)
        for direction in [self.PIECE_SHIFTING[MoveDirection.forward], self.PIECE_SHIFTING[MoveDirection.backward],
                          self.PIECE_SHIFTING[MoveDirection.left], self.PIECE_SHIFTING[MoveDirection.right]]:
            tmp_index = self._get_index(king_position) + direction
            while self._is_valid_index(tmp_index):
                tmp_position = self._get_position(tmp_index)
                if self.is_position_occupied(tmp_position):
                    piece = self.get_piece(tmp_position)
                    if piece.get_color() != color and piece.get_type() in file_and_rank_pieces:
                        check = True
                        break
                tmp_index += direction

        # Check right forward diagonal
        diagonal_pieces = (Type.queen, Type.bishop)
        for direction in [self.PIECE_SHIFTING[MoveDirection.f_left_diag], self.PIECE_SHIFTING[MoveDirection.f_right_diag],
                          self.PIECE_SHIFTING[MoveDirection.b_left_diag], self.PIECE_SHIFTING[MoveDirection.b_right_diag]]:
            tmp_index = self._get_index(king_position) + direction
            while self._is_valid_index(tmp_index):
                tmp_position = self._get_position(tmp_index)
                if self.is_position_occupied(tmp_position):
                    piece = self.get_piece(tmp_position)
                    if piece.get_color() != color and piece.get_type() in diagonal_pieces:
                        check = True
                        break
                tmp_index += direction

        # Check L shape

        return check

    def is_checkmate(self, color):
        """
        Test for checkmate against king of the specified color.

        :param color: Color
            Color of king to test for checkmate against.
        :return: bool
            True if king is in checkmate, False otherwise.
        """
        pass

    def move_piece(self, start_position, end_position):
        """
        Move piece from starting position to end position. Does
        not check if end position is valid. Ex. king in check
        or if overtaking square with piece of same color

        :param start_position:
        :param end_position:
        :return:
        """
        piece_on_start_position = self.get_piece(start_position)

        self._remove_piece(start_position)
        self._remove_piece(end_position)
        self._place_piece(end_position, piece_on_start_position)

        if piece_on_start_position.get_type() == Type.king:
            self._king_positions[piece_on_start_position.get_color()] = end_position

    def get_position(self, position, x_offset, y_offset):
        """
        Get the position corresponding to x and y offset.

        :param position: Position to treat as origin
        :param x_offset: x offset from origin
        :param y_offset: y offset from origin
        :return:
        """
        starting_index = self._get_index(position)
        possible_index = y_offset * 8 + x_offset + starting_index
        if self._is_valid_index(possible_index):
            return self._get_position(possible_index)
        return None

    def get_board_dimension(self):
        size = len(self._pieces) / 8
        return dict(width=size, height=size)

    def get_possible_moves(self, position):
        """
        Retrieve a list of all valid moves for the piece currently occupying the square at position.

        :param position: String
            Algebraic notation for a position.
        :return:
        """
        piece_on_start = self.get_piece(position)
        return piece_on_start.get_possible_moves(self, position)

    def _get_index(self, position):
        """
        Retrieve the index for the specified position.

        :param position: String
            Algebraic notation for a position.
        :return:
        """
        return self._indexes[position]

    def _get_position(self, index):
        """
        Retrieve the position for the specified index.

        :param index: int
            Index in _board_positions list
        :return:
        """
        return self._board_positions[index]

    def _place_piece(self, position, piece):
        try:
            index = self._indexes[position]
        except IndexError:
            raise Exception(position + " is not a valid position")
        piece.set_has_moved(True)
        self._pieces[self._board_positions[index]] = piece

    def _remove_piece(self, position):
        try:
            index = self._indexes[position]
        except IndexError:
            raise Exception(position + " is not a valid position")
        self._pieces[self._board_positions[index]] = None

    def __str__(self):
        return_val = ''
        for rank in range(56, -8, -8):
            for file in self._board_positions[rank: rank + 8]:
                if self._pieces[file] is None:
                    return_val += "# "
                else:
                    return_val += str(self._pieces[file]) + " "
            return_val += '\n'
        return return_val

    def _is_valid_index(self, index):
        if index < 0 or index > len(self._indexes):
            return False
        return True

board = ChessBoard()
# board.move_piece('b1', 'c3')
board.get_possible_moves('b1')
