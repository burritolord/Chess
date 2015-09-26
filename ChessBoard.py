__author__ = 'nick.james'
from Pawn import Pawn
from Rook import Rook
from Knight import Knight
from Bishop import Bishop
from King import King
from Queen import Queen
from Color import Color
from Move import Move
from Type import Type


class ChessBoard:

    forward = 8
    backward = -8
    left = -1
    right = 1
    f_left_diag = 7
    f_right_diag = 9
    b_left_diag = -7
    b_right_diag = -9
    l_shape = [-17, -15, -10, -6, 6, 10, 15, 17]

    def __init__(self):
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
        Get the piece at the specified position

        :param position: Starting position to check from
        :return: Piece
        """
        try:
            index = self._indexes[position]
        except IndexError:
            return None
        return self._board_positions[index]

    def is_position_occupied(self, position):
        try:
            index = self._indexes[position]
        except IndexError:
            raise Exception(position + " is not a valid position")
        return self._board_positions[index] is None

    def is_check(self, color):
        check = False
        # oponent_color = Color.black if color == Color.white else Color.black
        king_position = self._king_positions[color]

        # Check file and rank
        file_and_rank_pieces = (Type.queen, Type.rook)
        for direction in [Move.forward, Move.backward, Move.left, Move.right]:
            tmp_index = self._indexes[king_position] + direction
            while self._is_valid_index(tmp_index):
                tmp_position = self._pieces[self._board_positions[tmp_index]]
                if self.is_position_occupied(tmp_position):
                    piece = self.get_piece(tmp_position)
                    if piece.get_color() != color and piece.get_type() in file_and_rank_pieces:
                        check = True
                        break
                tmp_index += direction

        # Check right forward diagonal
        diagonal_pieces = (Type.queen, Type.bishop)
        for direction in [Move.f_left_diag, Move.f_right_diag, Move.b_left_diag, Move.b_right_diag]:
            tmp_index = self._indexes[king_position] + direction
            while self._is_valid_index(tmp_index):
                tmp_position = self._pieces[self._board_positions[tmp_index]]
                if self.is_position_occupied(tmp_position):
                    piece = self.get_piece(tmp_position)
                    if piece.get_color() != color and piece.get_type() in diagonal_pieces:
                        check = True
                        break
                tmp_index += direction

        # Check L shape

        return check

    def is_checkmate(self, color):
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
        piece_on_end_position = self.get_piece(end_position)


    def _place_piece(self, position, piece):
        try:
            index = self._indexes[position]
        except IndexError:
            raise Exception(position + " is not a valid position")
        self._board_positions[index] = piece

    def _remove_piece(self, position):
        try:
            index = self._indexes[position]
        except IndexError:
            raise Exception(position + " is not a valid position")
        self._board_positions[index] = None

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