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

        # Hold the last move made on this board. Needed to be able to do en passant check.
        self.last_move = {'start': '', 'end': '', 'piece_type': '', 'piece_color': ''}

        # List of all squares with algebraic notation.
        self._board_positions = [file+str(rank+1) for rank in range(0, board_length) for file in "abcdefgh"]

        # Dictionary of all pieces on board keyed by the algebraic notation.
        self._pieces = {file + str(rank + 1): None for rank in range(0, board_length) for file in "abcdefgh"}
        self._king_positions = {Color.white: None, Color.black: None}

        # Dictionary mapping of algebraic notation to index values. The board is a flat list and position a1 is index 0.
        # This mapping allows for quick quick offset computations. Shifting over to the right by the board width will
        # move us up one square.
        self._indexes = {}
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
        Check if a position is occupied with a piece.

        :param position: String
            Algebraic notation position.
        :return:
        """
        try:
            self._indexes[position]
        except IndexError:
            raise Exception(position + " is not a valid position")
        return self._pieces[position] is not None

    def is_check(self, king_color, position=None):
        """
        Test for check against king of the specified color.

        :param king_color: Color
            Color of king to test for check against.
        :param position: String
            If set, look for check from this position instead of the position
            of the king specified by king_color
        :return: bool
            True if king is in check, False otherwise.
        """
        king_position = position if position else self._king_positions[king_color]

        # Check file and rank
        diagonal_pieces = (Type.queen, Type.bishop)
        file_and_rank_pieces = (Type.rook, Type.queen)
        pawn_capture_directions = (MoveDirection.f_right_diag, MoveDirection.f_left_diag)
        opponent_piece_list = {
            MoveDirection.forward: file_and_rank_pieces,
            MoveDirection.f_right_diag: diagonal_pieces,
            MoveDirection.right: file_and_rank_pieces,
            MoveDirection.b_right_diag: diagonal_pieces,
            MoveDirection.backward: file_and_rank_pieces,
            MoveDirection.b_left_diag: diagonal_pieces,
            MoveDirection.left: file_and_rank_pieces,
            MoveDirection.f_left_diag: diagonal_pieces
        }

        for direction, pieces in opponent_piece_list.items():
            nearest_piece = self._get_nearest_piece_in_direction(king_position, direction, king_color, self._king_positions[king_color])
            if nearest_piece and nearest_piece['color'] != king_color:
                offset = nearest_piece['offset']
                piece_type = nearest_piece['type']
                if direction in pawn_capture_directions and offset == 1 and piece_type == Type.pawn:
                    return True
                elif offset == 1 and piece_type == Type.king:
                    return True
                elif piece_type in pieces:
                    return True

        # Color doesnt matter here
        l_shape_positions = self.get_possible_positions(king_position, MoveDirection.l_shape, king_color)
        for position in l_shape_positions:
            if self.is_position_occupied(position):
                piece = self[position]
                if piece.type == Type.knight and piece.color != king_color:
                    return True

        return False

    def is_checkmate(self, king_color):
        """
        Test for checkmate against king of the specified color.

        :param king_color: Color
            Color of king to test for checkmate against.
        :return: bool
            True if king is in checkmate, False otherwise.
        """
        king_position = self._king_positions[king_color]
        check = self.is_check(king_color)
        possible_moves = self.get_possible_moves(king_position)
        return check and not possible_moves

    def is_stalemate(self, king_color):
        """
        Test for stalemate

        :param king_color:
        :return: bool
            True if the game is a stalemate, False otherwise.
        """
        king_position = self._king_positions[king_color]
        return not self.is_check(king_color) and not self.get_possible_moves(king_position)

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
        """
        Get the board width and height

        :return: Dictionary
            width: width of board
            height: height of board
        """
        size = len(self._pieces) / self.get_dimension()
        return dict(width=size, height=size)

    def get_possible_moves(self, position):
        """
        Retrieve a list of all valid moves for the piece currently occupying the supplied position.

        :param position: String
            Algebraic notation for a position.
        :return: List
            List of positions that the piece at the position can move to.
        """
        if not self.is_position_occupied(position):
            return []

        piece_on_start = self[position]
        return piece_on_start.get_possible_moves(self, position)

    def get_board_pieces(self):
        """
        Get a dictionary of board pieces. Every square on the board is returned. They key to each square is the
        algebraic notation of that square and the value is None if there is not piece.
        :return:
        """
        return self._pieces

    def get_dimension(self):
        """
        Retrieve board dimension.

        :return: int
            Board is assumed to be square so only the dimensions for one side is returned.
        """
        return 8

    def load(self, game_transactions):
        """
        Inflate the ChessBoard object based on the provided transactions. Each
        transaction should contain the player who made the move, the piece,
        the start position, and the end position.

        :param game_transactions:
        :return:
        """
        for transaction in game_transactions:
            player, piece, start_pos, end_pos = transaction
            self.move_piece(start_pos, end_pos)

    def get_possible_positions(self, start_position, move_direction, piece_color):
        """
        Get a list of all possible positions in the direction provided as if the board were empty. Positions returned
        are in algebraic notation.

        :param start_position:
        :param move_direction:
        :return:
        """
        possible_positions = []
        x_offset, y_offset = 0, 0

        if move_direction == MoveDirection.l_shape:
            current_x_coord, current_y_coord = self._position_to_coordinates(start_position)
            # Color used in MOVE_OFFSETS doesnt matter for l_shape
            for x_offset, y_offset in Move.MOVE_OFFSETS[piece_color][move_direction]:
                possible_position = self._get_position(start_position, x_offset, y_offset)
                if possible_position is not None:
                    no_y_shift_position = self._get_position(start_position, x_offset, 0)
                    no_y_shift_x, no_y_shift_y = self._position_to_coordinates(no_y_shift_position)
                    if current_y_coord == no_y_shift_y:
                        possible_positions.append(possible_position)
        else:
            num_spaces = self._get_direction_square_count(start_position, move_direction)
            for count in range(0, num_spaces):
                x_offset, y_offset = self._get_increment_values(move_direction, piece_color, x_offset, y_offset)
                possible_positions.append(self._get_position(start_position, x_offset, y_offset))

        return possible_positions

    def _get_increment_values(self, move_direction, piece_color, x_position, y_position):
        increment_values = (0, 0)
        if move_direction != MoveDirection.l_shape:
            x_increment, y_increment = Move.MOVE_OFFSETS[piece_color][move_direction]
            increment_values = (x_position + x_increment, y_position + y_increment)
        return increment_values

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
            position_x = self._index_to_position(possible_x_index)
            column_x, row_x = self._position_to_coordinates(position_x)
            column_current, row_current = self._position_to_coordinates(position)

            if row_x == row_current:
                new_index = y_offset * self.get_dimension() + x_offset + starting_index
                return self._index_to_position(new_index)
        return None

    def _position_to_coordinates(self, position):
        """
        Treat A1 as the origin in x,y coordinate system. Return offset the passed in
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

    def _get_nearest_piece_in_direction(self, start_position, move_direction, piece_color, ignore_position=None):
        """
        Get the nearest piece from the starting position heading in
        the direction specified. Not expecting MoveDirection.l_shape
        as a direction.

        :param start_position: String
            Position to start searching from
        :param move_direction: Direction
            Direction to search in
        :param piece_color: Color
            Color of piece on start_position. Needed to know which
            direction is forward, backward, etc.
        :return Dictionary
            [position]
            [color]
            [offset]
            [type]
        """
        offset = 0
        positions = self.get_possible_positions(start_position, move_direction, piece_color)

        for position in positions:
            offset += 1
            piece_on_destination = self.is_position_occupied(position)

            if piece_on_destination:
                if ignore_position and position == ignore_position:
                    continue
                piece = self[position]
                return {'position': position, 'color': piece.color, 'offset': offset, 'type': piece.type}

        return None

    def _is_valid_index(self, index):
        """

        """
        if index < 0 or index >= len(self._indexes):
            return False
        return True

    def __str__(self):
        """

        """
        board_size = self.get_dimension()
        rank_count = self.get_dimension()
        return_val = ''
        for rank in range(rank_count * 7, -board_size, -board_size):
            return_val += str(rank_count) + " "
            for file in self._board_positions[rank: rank + board_size]:
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

board = ChessBoard(True)
board['d5'] = Rook(Color.black)
print(board.get_possible_positions('d3', MoveDirection.forward, Color.white))
# board['35'] = Pawn(Color.black)
