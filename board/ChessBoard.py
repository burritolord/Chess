__author__ = 'nick.james'
from piece.Pawn import Pawn
from piece.Rook import Rook
from piece.Knight import Knight
from piece.Bishop import Bishop
from piece.King import King
from piece.Queen import Queen
from piece.Color import Color
from piece.Type import Type
from piece.Move import Move
from piece.MoveDirection import MoveDirection
from ChessHelper import ChessHelper


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

    def __init__(self, empty_board=False):
        """
        Create a ChessBoard object with all pieces in starting position
        :return:
        """
        board_length = self.get_dimension()
        self.last_move = {'start': '', 'end': '', 'piece_type': '', 'piece_color': ''}
        self._board_positions = [y+str(x+1) for x in range(0, board_length) for y in "abcdefgh"]
        self._pieces = {y+str(x+1): None for x in range(0, board_length) for y in "abcdefgh"}
        self._indexes = {}
        self._king_positions = {Color.white: None, Color.black: None}
        for position, index in zip(self._board_positions, range(0, board_length**2)):
            self._indexes[position] = index

        if not empty_board:
            # Set the starting pieces for white
            for index in range(board_length, board_length*2):
                self._pieces[self._board_positions[index]] = Pawn(Color.white)
            self._pieces['a1'], self._pieces['h1'] = Rook(Color.white), Rook(Color.white)
            self._pieces['b1'], self._pieces['g1'] = Knight(Color.white), Knight(Color.white)
            self._pieces['c1'], self._pieces['f1'] = Bishop(Color.white), Bishop(Color.white)
            self._pieces['d1'] = Queen(Color.white)
            self._pieces['e1'] = King(Color.white)

            # Set the starting pieces for black
            for index in range(board_length*6, board_length*7):
                self._pieces[self._board_positions[index]] = Pawn(Color.black)
            self._pieces['a8'], self._pieces['h8'] = Rook(Color.black), Rook(Color.black)
            self._pieces['b8'], self._pieces['g8'] = Knight(Color.black), Knight(Color.black)
            self._pieces['c8'], self._pieces['f8'] = Bishop(Color.black), Bishop(Color.black)
            self._pieces['d8'] = Queen(Color.black)
            self._pieces['e8'] = King(Color.black)

            self._king_positions[Color.white] = 'e1'
            self._king_positions[Color.black] = 'e8'

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
        # Check file and rank
        oponent_piece_list = {MoveDirection.forward: [Type.rook, Type.queen],
                              MoveDirection.f_right_diag: [Type.queen, Type.bishop]}

        self._get_nearest_piece_in_direction(king_position, MoveDirection.forward)
        file_and_rank_pieces = (Type.queen, Type.rook)
        for direction in [self.PIECE_SHIFTING[MoveDirection.forward], self.PIECE_SHIFTING[MoveDirection.backward],
                          self.PIECE_SHIFTING[MoveDirection.left], self.PIECE_SHIFTING[MoveDirection.right]]:
            tmp_index = self._position_to_index(king_position) + direction
            while self._is_valid_index(tmp_index):
                tmp_position = self._index_to_position(tmp_index)
                if self.is_position_occupied(tmp_position):
                    piece = self[tmp_position]
                    if piece.color != color and piece.type in file_and_rank_pieces:
                        check = True
                        break
                    else:
                        break
                tmp_index += direction

        # Check diagonal
        diagonal_pieces = (Type.queen, Type.bishop)
        for direction in [self.PIECE_SHIFTING[MoveDirection.f_left_diag], self.PIECE_SHIFTING[MoveDirection.f_right_diag],
                          self.PIECE_SHIFTING[MoveDirection.b_left_diag], self.PIECE_SHIFTING[MoveDirection.b_right_diag]]:
            tmp_index = self._position_to_index(king_position) + direction
            while self._is_valid_index(tmp_index):
                tmp_position = self._index_to_position(tmp_index)
                if self.is_position_occupied(tmp_position):
                    piece = self[tmp_position]
                    if piece.color != color and piece.type in diagonal_pieces:
                        check = True
                        break
                    else:
                        break
                tmp_index += direction

        # Check L shape
        for offset in self.PIECE_SHIFTING[MoveDirection.l_shape]:
            tmp_index = self._position_to_index(king_position) + offset
            if self._is_valid_index(tmp_index):
                tmp_position = self._index_to_position(tmp_index)
                if self.is_position_occupied(tmp_position):
                    if piece.color != color and piece.type in diagonal_pieces:
                        check = True
                        break

        return check

    def is_checkmate(self, color):
        """
        Test for checkmate against king of the specified color.

        :param color: Color
            Color of king to test for checkmate against.
        :return: bool
            True if king is in checkmate, False otherwise.
        """
        king = self[self._king_positions[color]]
        return self.is_check(color) and not king.get_possible_moves()

    def move_piece(self, start_position, end_position):
        """
        Move piece from starting position to end position. Does
        not check if end position is valid. Ex. king in check
        or if overtaking square with piece of same color

        :param start_position:
        :param end_position:
        :return:
        """
        piece_on_start_position = self[start_position]
        piece_on_start_position.has_moved = True

        self._remove_piece(start_position)
        self._remove_piece(end_position)
        self[end_position] = piece_on_start_position

        if piece_on_start_position.type == Type.king:
            self._king_positions[piece_on_start_position.color] = end_position

        self.last_move['start'] = start_position
        self.last_move['end'] = end_position
        self.last_move['piece_type'] = self._pieces[end_position].type
        self.last_move['piece_color'] = self._pieces[end_position].color

    def get_board_dimension(self):
        size = len(self._pieces) / self.get_dimension()
        return dict(width=size, height=size)

    def get_possible_moves(self, position):
        """
        Retrieve a list of all valid moves for the piece currently occupying the square at position.

        :param position: String
            Algebraic notation for a position.
        :return:
        """
        if not self.is_position_occupied(position):
            return []

        piece_on_start = self[position]
        return piece_on_start.get_possible_moves(self, position)

    def get_board_pieces(self):
        return self._pieces

    def get_dimension(self):
        return 8

    def load(self, game_transactions):
        """

        :param game_transactions:
        :return:
        """
        for transaction in game_transactions:
            player, piece, start_pos, end_pos = transaction
            self.move_piece(start_pos, end_pos)

    def get_possible_positions(self, start_position, move_direction):
        """

        """
        possible_positions = []
        x_offset, y_offset = 0, 0

        if move_direction == MoveDirection.l_shape:
            current_x_coord, current_y_coord = self._position_to_coordinates(start_position)
            for x_offset, y_offset in Move.MOVE_OFFSETS[move_direction]:
                possible_position = self._get_position(start_position, x_offset, y_offset)
                if possible_position is not None:
                    no_y_shift_position = self._get_position(start_position, x_offset, 0)
                    no_y_shift_x, no_y_shift_y = self._position_to_coordinates(no_y_shift_position)
                    if current_y_coord == no_y_shift_y:
                        possible_positions.append(possible_position)
        else:
            num_spaces = self._get_direction_square_count(start_position, move_direction)
            move = Move()

            for count in range(0, num_spaces):
                x_offset, y_offset = move.get_increment_values(move_direction, x_offset, y_offset)
                possible_positions.append(self._get_position(start_position, x_offset, y_offset))

        return possible_positions

    def _get_position(self, position, x_offset, y_offset):
        """
        Get the position corresponding to x and y offset.

        :param position: Position to treat as origin
        :param x_offset: x offset from origin
        :param y_offset: y offset from origin
        :return:
        """
        starting_index = self._position_to_index(position)
        possible_y_index = y_offset * self.get_dimension() + starting_index
        possible_x_index = x_offset + starting_index

        if self._is_valid_index(possible_y_index) and self._is_valid_index(possible_x_index):
            new_index = y_offset * self.get_dimension() + x_offset + starting_index
            return self._index_to_position(new_index)
        return None

    def _position_to_coordinates(self, position):
        """
        Treat a1 as the origin in x,y coordinate system. Return offset the passed in
        position is from the origin.

        :param position: String
            Algebraic notation for chess position
        :return: Tuple
            The coordinates for the position
        """
        position = ChessHelper.to_string(position)
        columns = {letter: index for index, letter in enumerate("abcdefgh")}
        column = columns[position[0]]
        row = int(position[1]) - 1

        return column, row


    def _get_direction_square_count(self, start_position, move_direction):
        """

        :param start_position:
        :param move_direction:
        :return:
        """
        board_length = self.get_dimension()
        max_movement = board_length - 1
        num_spaces = max_movement
        current_x_coord, current_y_coord = self._position_to_coordinates(start_position)

        if move_direction == MoveDirection.forward:
            max_movement = board_length - current_y_coord - 1
        elif move_direction == MoveDirection.f_right_diag:
            from_right = board_length - current_x_coord - 1
            from_top = board_length - current_y_coord - 1
            max_movement = min(from_top, from_right)
        elif move_direction == MoveDirection.right:
            max_movement = board_length - current_x_coord - 1
        elif move_direction == MoveDirection.b_right_diag:
            from_right = board_length - current_x_coord - 1
            max_movement = min(current_y_coord, from_right)
        elif move_direction == MoveDirection.backward:
            max_movement = current_y_coord
        elif move_direction == MoveDirection.b_left_diag:
            max_movement = min(current_y_coord, current_x_coord)
        elif move_direction == MoveDirection.left:
            max_movement = current_x_coord
        elif move_direction == MoveDirection.f_left_diag:
            from_top = board_length - current_y_coord - 1
            max_movement = min(from_top, current_x_coord)

        return min(num_spaces, max_movement)

    def _position_to_index(self, position):
        """
        Retrieve the index for the specified position.

        :param position: String
            Algebraic notation for a position.
        :return:
        """
        return self._indexes[position]

    def _index_to_position(self, index):
        """
        Retrieve the position for the specified index.

        :param index: int
            Index in _board_positions list
        :return:
        """
        return self._board_positions[index]

    def _remove_piece(self, position):
        """
        Remove a piece from the board
        :param position: String
            Algebraic notation for a position.
        :return:
        """
        try:
            index = self._indexes[position]
        except IndexError:
            raise Exception(position + " is not a valid position")
        self._pieces[self._board_positions[index]] = None

    def _get_nearest_piece_in_direction(self, start_position, move_direction):
        """

        """
        x_offset, y_offset = 0, 0
        num_spaces = self._get_direction_square_count(start_position, move_direction)
        move = Move()

        for count in range(0, num_spaces):
            x_offset, y_offset = move.get_increment_values(move_direction, x_offset, y_offset)
            possible_position = self._get_position(start_position, x_offset, y_offset)
            piece_on_destination = self.is_position_occupied(possible_position)

            if piece_on_destination:
                return possible_position

        return None

    def _is_valid_index(self, index):
        if index < 0 or index >= len(self._indexes):
            return False
        return True

    def __str__(self):
        rank_count = self.get_dimension()
        return_val = ''
        for rank in range(rank_count * 7, -rank_count, -rank_count):
            return_val += str(rank_count) + " "
            for file in self._board_positions[rank: rank + rank_count]:
                if self._pieces[file] is None:
                    return_val += "# "
                else:
                    return_val += str(self._pieces[file]) + " "
            return_val += '\n'
            rank_count -= 1

        return_val += "  "
        for file_letter in "abcdefgh":
            return_val += file_letter + " "

        return return_val

    def __getitem__(self, position):
        """
        Get the piece at the specified position.
        """
        return self._pieces[position]

    def __setitem__(self, position, piece):
        self._pieces[position] = piece
        if piece.type == Type.king:
            self._king_positions[piece.color] = position

# board = ChessBoard(True)
# board['a2'] = Queen(Color.white)
# Queen.has_moved = True
# # print(board)
# print(board.get_possible_moves('a2'))
# board.move_piece('e1','e7')
# print(board.is_check(Color.white))
