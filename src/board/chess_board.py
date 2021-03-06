import copy
from src.board.fen import Fen
from src.piece.rook import Rook
from src.piece.knight import Knight
from src.piece.bishop import Bishop
from src.piece.queen import Queen
from src.piece.color import Color
from src.piece.type import Type
from src.piece.move_direction import MoveDirection
from src.utils.chess_helper import ChessHelper
from src.board.exception import PieceTypeError
from src.board.exception import EmptyPositionError
from src.board.exception import InvalidPositionError
from src.board.exception import InvalidIndexError


class ChessBoard:

    """
    Offsets to shift over from current position to move forward, backward, etc.
    """
    PIECE_SHIFTING = {
        MoveDirection.FORWARD: 8,
        MoveDirection.BACKWARD: -8,
        MoveDirection.LEFT: -1,
        MoveDirection.RIGHT: 1,
        MoveDirection.F_LEFT_DIAG: 7,
        MoveDirection.F_RIGHT_DIAG: 9,
        MoveDirection.B_LEFT_DIAG: -9,
        MoveDirection.B_RIGHT_DIAG: -7,
        MoveDirection.L_SHAPE: [-17, -15, -10, -6, 6, 10, 15, 17]
    }

    def __init__(self, fen=None):
        """
        Create a ChessBoard object.

        :param fen: Fen
            Object containing initial board configuration
        :return:
        """
        board_length = self.get_dimension()

        # Hold en passant target square. Needed to be able to do en passant check.
        self._en_passant_info = {'target_position': None, 'pawn_position': None}

        # List of all squares with algebraic notation.
        self._board_positions = [file+str(rank+1) for rank in range(0, board_length) for file in "abcdefgh"]

        # Dictionary of all pieces on board keyed by the algebraic notation.
        self._pieces = {file + str(rank + 1): None for rank in range(0, board_length) for file in "abcdefgh"}
        self._king_positions = {Color.WHITE: None, Color.BLACK: None}

        # Dictionary mapping of algebraic notation to index values. The board is a flat list and position a1 is index 0.
        # This mapping allows for quick offset computations. Shifting over to the right by the board width will move us
        # up one square.
        self._indexes = {Color.WHITE: {}, Color.BLACK: {}}
        for position, index in zip(self._board_positions, range(0, board_length**2)):
            self._indexes[Color.WHITE][position] = index
        for position, index in zip(reversed(self._board_positions), range(0, board_length**2)):
            self._indexes[Color.BLACK][position] = index

        if fen and fen.board:
            # Set en passant position if there is one
            if fen.en_passant_position:
                self._en_passant_info['target_position'] = fen.en_passant_position
                push_pawn = self._get_position_shifted_by_offset(fen.en_passant_position, MoveDirection.BACKWARD, 1,
                                                                 fen.current_player)
                self._en_passant_info['pawn_position'] = push_pawn

            for position, piece in fen.board.items():
                self._pieces[position] = copy.deepcopy(piece)

                # Set king positions
                if piece.type == Type.KING:
                    self._king_positions[piece.color] = position

            # Update king move directions
            for direction in [MoveDirection.LEFT, MoveDirection.RIGHT]:
                if self._king_positions[Color.WHITE]:
                    king = self[self._king_positions[Color.WHITE]]
                    if direction not in fen.white_castle:
                        king.move_directions[direction] = 1

            for direction in [MoveDirection.LEFT, MoveDirection.RIGHT]:
                if self[self._king_positions[Color.BLACK]]:
                    king = self[self._king_positions[Color.BLACK]]
                    if direction not in fen.black_castle:
                        king.move_directions[direction] = 1

    def is_position_occupied(self, position):
        """
        Check if a position is occupied with a piece.

        :param position: string
            Algebraic notation position.
        :return: bool
            True if piece on position, False otherwise
        """
        ChessHelper.validate_position(position)

        return self._pieces[position] is not None

    def is_check(self, king_color, position=None, ghost_pieces=None):
        """
        Test for check against king of the specified color.

        :param king_color: Color
            Color of king to test for check against.
        :param position: string
            If set, look for check from this position instead of the position of the king specified by king_color.
        :param ghost_pieces: dict
            Positions to ignore or contain ghost pieces.
        :return: bool
            True if king is in check, False otherwise.
        """
        if position:
            ChessHelper.validate_position(position)

        king_position = position if position else self._king_positions[king_color]
        if not self._king_positions[king_color]:
            return False

        # Check file and rank
        diagonal_pieces = (Type.QUEEN, Type.BISHOP)
        file_and_rank_pieces = (Type.ROOK, Type.QUEEN)
        pawn_capture_directions = (MoveDirection.F_RIGHT_DIAG, MoveDirection.F_LEFT_DIAG)
        opponent_piece_list = {
            MoveDirection.FORWARD: file_and_rank_pieces,
            MoveDirection.F_RIGHT_DIAG: diagonal_pieces,
            MoveDirection.RIGHT: file_and_rank_pieces,
            MoveDirection.B_RIGHT_DIAG: diagonal_pieces,
            MoveDirection.BACKWARD: file_and_rank_pieces,
            MoveDirection.B_LEFT_DIAG: diagonal_pieces,
            MoveDirection.LEFT: file_and_rank_pieces,
            MoveDirection.F_LEFT_DIAG: diagonal_pieces
        }

        for direction, pieces in opponent_piece_list.items():
            ghost_pieces = {} if not ghost_pieces else ghost_pieces
            nearest_piece = self._get_nearest_piece_in_direction(king_position, direction, king_color, ghost_pieces)
            if nearest_piece and nearest_piece['color'] != king_color:
                offset = nearest_piece['offset']
                piece_type = nearest_piece['type']
                if direction in pawn_capture_directions and offset == 1 and piece_type == Type.PAWN:
                    return True
                elif offset == 1 and piece_type == Type.KING:
                    return True
                elif piece_type in pieces:
                    return True

        # Color doesnt matter here
        l_shape_positions = self._get_possible_positions(king_position, MoveDirection.L_SHAPE, king_color)
        for position in l_shape_positions:
            if self.is_position_occupied(position):
                piece = self[position]
                if piece.type == Type.KNIGHT and piece.color != king_color:
                    return True

        return False

    def get_enpassant_position(self):
        """
        Retrieve the en passant target position.
        :return:
        """
        return self._en_passant_info['target_position']

    def is_checkmate(self, king_color):
        """
        Test for checkmate against king of the specified color.

        :param king_color: Color
            Color of king to test for checkmate against.
        :return: bool
            True if king is in checkmate, False otherwise.
        """
        # TODO confirm no piece can block the piece putting king in check. If there is a piece,
        # need to be sure piece is not pinned
        king_position = self._king_positions[king_color]
        # is_check needs to return piece, piece position, and attack squares for piece putting king in check
        # Can piece putting king in check be captured
        # Can a non pinned piece block
        # Iterate over list of pieces.
        # Check if a piece possible moves includes capturing the piece putting king in check. Ghost piece trying to move
        # and piece putting king in check
        # Check if a piece possible moves includes attack squares Ghost piece trying to move
        # Maybe just create method to return dict of all non pinned pieces
        check = self.is_check(king_color)
        possible_moves = self.get_legal_moves(king_position)
        return check and not possible_moves

    def is_stalemate(self, color):
        """
        Test for stalemate.

        :param color: Color
            Color of player to test for stalemate.
        :return: bool
            True if the game is a stalemate, False otherwise.
        """
        # TODO add check for insufficient material to checkmate opponent
        legal_moves_available = False
        for position, piece in self._pieces.items():
            if piece and piece.color == color:
                legal_moves = self.get_legal_moves(position)
                if legal_moves:
                    legal_moves_available = True

        king_in_check = self.is_check(color)

        return not king_in_check and not legal_moves_available

    def move_piece(self, start_position, end_position):
        """
        Move piece from starting position to end position. Does not check if end position is valid. Ex. king in check
        or if overtaking square with piece of same color. Also does not check if moving piece has passed through other
        pieces.

        :param start_position: string
            Algebraic notation position.
        :param end_position: string
            Algebraic notation position.
        :return: dict
            [position]: Piece. Use None if position is now empty
        """
        ChessHelper.validate_position(start_position)
        ChessHelper.validate_position(end_position)

        start_position_piece = self[start_position]
        if not start_position_piece:
            raise EmptyPositionError(start_position)

        updated_positions = {}
        move_info = self._direction_and_position_offset(start_position, end_position, start_position_piece.color)
        direction = move_info['direction']
        column_offset, row_offset = move_info['offset']

        # Copy of en_passant info
        en_passant_info = copy.copy(self._en_passant_info)

        # Have to clone the piece before moving it. Otherwise, it makes it really hard to compare
        # expected move result to actual move result since the piece here could have a modified
        # move_directions . Plus, we don't really care about any values other than piece type and color
        updated_positions[start_position] = None
        updated_positions[end_position] = copy.deepcopy(start_position_piece)

        if start_position_piece.type == Type.PAWN and row_offset == 2:
            tartget_position = self._get_position_shifted_by_offset(start_position, MoveDirection.FORWARD, 1,
                                                                    start_position_piece.color)
            en_passant_info['pawn_position'] = end_position
            en_passant_info['target_position'] = tartget_position
        else:
            en_passant_info['pawn_position'] = None
            en_passant_info['target_position'] = None

        # Check pawn special movements
        if start_position_piece.type == Type.PAWN:
            # Update move_directions after pawn moves forward twice
            if start_position_piece.move_directions[MoveDirection.FORWARD] > 1:
                start_position_piece.move_directions[MoveDirection.FORWARD] = 1
            # Check for en passant
            if self.can_en_passant(start_position, direction):
                self._remove_piece(self._en_passant_info['pawn_position'])
                updated_positions[self._en_passant_info['pawn_position']] = None
        # Check for castling
        elif start_position_piece.type == Type.KING:
            if abs(column_offset) == 2 and self.can_castle(start_position_piece.color, direction):
                rook_positions = {
                    Color.WHITE: {MoveDirection.LEFT: 'a1', MoveDirection.RIGHT: 'h1'},
                    Color.BLACK: {MoveDirection.LEFT: 'h8', MoveDirection.RIGHT: 'a8'}
                }
                new_rook_position = self._get_position_shifted_by_offset(start_position, direction, 1,
                                                                     start_position_piece.color)
                self[new_rook_position] = self[rook_positions[start_position_piece.color][direction]]
                self._remove_piece(rook_positions[start_position_piece.color][direction])
                updated_positions[new_rook_position] = copy.deepcopy(self[new_rook_position])
                updated_positions[rook_positions[start_position_piece.color][direction]] = None

                # Update King left and right move_directions
                start_position_piece.move_directions[MoveDirection.LEFT] = 1
                start_position_piece.move_directions[MoveDirection.RIGHT] = 1

            start_position_piece.move_directions[MoveDirection.LEFT] = 1
            start_position_piece.move_directions[MoveDirection.RIGHT] = 1
        elif start_position_piece.type == Type.ROOK:
            king_position = self._king_positions[start_position_piece.color]
            column, row = self.position_to_row_and_column(start_position, start_position_piece.color)
            rook_direction = None
            if column == 0:
                rook_direction = MoveDirection.LEFT
            elif column == self.get_dimension() - 1:
                rook_direction = MoveDirection.RIGHT
            # Check needed because might be dealing with a board without a king
            if king_position and rook_direction:
                king = self[king_position]
                if king.move_directions[rook_direction] > 1:
                    king.move_directions[rook_direction] = 1

        self._en_passant_info = en_passant_info
        self._remove_piece(start_position)
        self._remove_piece(end_position)
        self[end_position] = start_position_piece

        return updated_positions

    def can_castle(self, king_color, direction):
        """
        Check if a king can castle or not.

        :param king_color: Color
            Color of king to check if can castle.
        :param direction: int
            Expecting either MoveDirection.left or MoveDirection.right
        :return: bool
            True if king can castle, False otherwise.
        """
        if direction != MoveDirection.LEFT and direction != MoveDirection.RIGHT:
            return False

        king_position = self._king_positions[king_color]
        nearest_piece_info = self._get_nearest_piece_in_direction(king_position, direction, king_color)

        if nearest_piece_info and nearest_piece_info['type'] == Type.ROOK:
            king = self[king_position]
            is_check = self.is_check(king_color, king_position)
            if king_color == Color.WHITE:
                expected_rook_offset = 3 if direction == MoveDirection.RIGHT else 4
            else:
                expected_rook_offset = 4 if direction == MoveDirection.RIGHT else 3
            is_expected_offset = expected_rook_offset == nearest_piece_info['offset']

            if king.move_directions[direction] == 2 and not is_check and is_expected_offset:
                king_index = self._position_to_index(king_position, king.color)
                index_one = king_index + self.PIECE_SHIFTING[direction]
                index_two = index_one + self.PIECE_SHIFTING[direction]
                position_one_is_check = self.is_check(king_color, self._index_to_position(index_one, king_color))
                position_two_is_check = self.is_check(king_color, self._index_to_position(index_two, king_color))
                if not position_one_is_check and not position_two_is_check:
                    return True

        return False

    def can_en_passant(self, position, direction):
        """
        Check if a pawn can perform en passant move.
        :param position: string
            Algebraic notation position.
        :param direction: int
            Direction to look in. Ex MoveDirection.f_right_diag
        :return:
        """
        if direction != MoveDirection.F_RIGHT_DIAG and direction != MoveDirection.F_LEFT_DIAG:
            return False

        pawn = self[position]
        if not pawn:
            return False
        if pawn.type != Type.PAWN:
            return False

        # Check if en_passant target_position is equal to the position passed in
        new_position = self._get_position_shifted_by_offset(position, direction, 1, pawn.color)
        if new_position == self._en_passant_info['target_position']:
            return True

        return False

    def get_legal_moves(self, position):
        """
        Retrieve a list of all legal moves for the piece currently occupying the supplied position.

        :param position: string
            Algebraic notation for a position.
        :return: List
            List of positions that the piece at the position can move to.
        """
        if not self.is_position_occupied(position):
            return []

        possible_moves = []
        piece_on_position = self[position]
        piece_move_directions = piece_on_position.move_directions
        piece_king_position = self._king_positions[piece_on_position.color]

        # TODO Refactor. Code is hard to follow
        for move_direction, num_spaces in piece_move_directions.items():
            possible_positions = self._get_possible_positions(position, move_direction, piece_on_position.color)

            # Handle special case for Knight
            if move_direction == MoveDirection.L_SHAPE:
                for possible_position in possible_positions:
                    ghost_pieces = {
                        position: None,
                        possible_position: {
                            'color': piece_on_position.color,
                            'type': piece_on_position.type
                        }
                    }

                    if not self.is_check(piece_on_position.color, piece_king_position, ghost_pieces):
                        piece_on_destination = self.is_position_occupied(possible_position)
                        if not piece_on_destination:
                            possible_moves.append(possible_position)
                        elif self[possible_position].color != piece_on_position.color:
                            possible_moves.append(possible_position)

            # Every other piece
            else:
                piece_num_spaces = piece_on_position.move_directions[move_direction]
                num_spaces = len(possible_positions) if piece_num_spaces == -1 else num_spaces
                num_spaces = min(len(possible_positions), num_spaces)

                for position_num, possible_position in enumerate(possible_positions[0:num_spaces]):
                    destination_occupied = self.is_position_occupied(possible_position)
                    # Ignore the current position when performing a test for check. Also place piece on possible
                    # position as a ghost piece. Needed to know if when moved to possible position, the king is still
                    # not in check
                    ghost_pieces = {
                        position: None,
                        possible_position: {
                            'color': piece_on_position.color,
                            'type': piece_on_position.type
                        }
                    }

                    if piece_on_position.type == Type.KING:
                        if not self.is_check(piece_on_position.color, possible_position, ghost_pieces):
                            try:
                                can_castle = self.can_castle(piece_on_position.color, move_direction)
                            except ValueError:
                                can_castle = False
                            finally:
                                king_index = self._position_to_index(position, piece_on_position.color)
                                possible_index = self._position_to_index(possible_position, piece_on_position.color)
                                distance = abs(king_index - possible_index)

                            # Only add position two squares away if castling is possible
                            if can_castle and distance == 2:
                                possible_moves.append(possible_position)
                            elif not destination_occupied and distance != 2:
                                possible_moves.append(possible_position)
                            elif destination_occupied and self[possible_position].color != piece_on_position.color and\
                                    distance != 2:
                                possible_moves.append(possible_position)
                                break
                        else:  # Piece is same color as one we are working with
                            break
                    elif piece_on_position.type == Type.PAWN and not self.is_check(piece_on_position.color, piece_king_position, ghost_pieces):
                        if (not destination_occupied and move_direction != MoveDirection.F_LEFT_DIAG
                                and move_direction != MoveDirection.F_RIGHT_DIAG):
                            possible_moves.append(possible_position)
                        elif (self[possible_position] and self[possible_position].color != piece_on_position.color and
                              (move_direction == MoveDirection.F_LEFT_DIAG or
                               move_direction == MoveDirection.F_RIGHT_DIAG) and
                              position_num == 0):
                            possible_moves.append(possible_position)
                            break
                        elif (move_direction == MoveDirection.F_LEFT_DIAG or
                              move_direction == MoveDirection.F_RIGHT_DIAG) and\
                                self.can_en_passant(position, move_direction):
                            possible_moves.append(possible_position)
                        else:  # Piece is same color as one we are working with
                            break
                    elif not self.is_check(piece_on_position.color, piece_king_position, ghost_pieces):
                        if not destination_occupied:
                            possible_moves.append(possible_position)
                        elif self[possible_position].color != piece_on_position.color:
                            possible_moves.append(possible_position)
                            break
                        else:  # Piece is same color as one we are working with
                            break

        return possible_moves

    def get_board_pieces(self):
        """
        Get a dictionary of board pieces.

        :return: dict
            Every square on the board is returned. They key to each square is the algebraic notation of that square and
            the value is None if there is not a piece.
        """
        return copy.deepcopy(self._pieces)

    def get_dimension(self):
        """
        Retrieve board dimension.

        :return: int
            Board is assumed to be square so only the dimensions for one side is returned.
        """
        return 8

    def position_to_row_and_column(self, position, piece_color):
        """
        Treat position at bottom left corner as the origin in x,y coordinate system. Return offset the passed in
        position is from the origin.

        :param position: string
            Algebraic notation for chess position
        :param piece_color: Color
            Color of player who's perspective should be used.
        :return: tuple
            The coordinates for the position.
            Ex (1,1) from white perspective is B2 but G7 from black perspective.
        """
        ChessHelper.validate_position(position)

        if piece_color == Color.WHITE:
            column = 'abcdefgh'.index(position[0])
            row = int(position[1]) - 1
        else:
            column = 'hgfedcba'.index(position[0])
            dimension = self.get_dimension()
            row = dimension - int(position[1])

        return column, row

    def _get_possible_positions(self, start_position, move_direction, piece_color):
        """
        Get a list of all possible positions in the direction provided as if the board were empty. Positions returned
        are in algebraic notation.

        :param start_position: string
            Algebraic notation position.
        :param move_direction: int
            Direction to move. Ex MoveDirection.forward
        :param piece_color: Color
            Color of player who's perspective should be used.
        :return: list
            List of positions in algebraic notation. Positions in the list are sorted by the offset from the start
            position. Index 0 is the nearest position in the specified direction.
        """
        ChessHelper.validate_position(start_position)

        possible_positions = []
        current_index = next_index = self._position_to_index(start_position, piece_color)
        current_column, current_row = self.position_to_row_and_column(
            self._index_to_position(current_index, piece_color),
            piece_color)
        if move_direction == MoveDirection.L_SHAPE:
            for shift in self.PIECE_SHIFTING[MoveDirection.L_SHAPE]:
                try:
                    next_index = current_index + shift
                    self._index_to_position(next_index, piece_color)
                except InvalidIndexError:
                    continue
                else:
                    next_column, next_row = self.position_to_row_and_column(
                        self._index_to_position(next_index, piece_color),
                        piece_color)
                    column_diff = abs(next_column - current_column)
                    if current_row != next_row and column_diff <= 2:
                        possible_positions.append(self._index_to_position(next_index, piece_color))
        else:
            num_spaces = self._get_direction_square_count(start_position, move_direction, piece_color)
            for count in range(0, num_spaces):
                next_index += self.PIECE_SHIFTING[move_direction]
                possible_positions.append(self._index_to_position(next_index, piece_color))

        return possible_positions

    def _get_direction_square_count(self, start_position, move_direction, piece_color):
        """
        Retrieve the number of squares from the starting position to the edge of the board in the direction specified.

        :param start_position: string
            Algebraic notation position.
        :param move_direction: int
            Direction to work in. Ex MoveDirection.forward
        :param piece_color: Color
            Color of player who's perspective should be used.
        :return: int
            Number of squares till the edge of the board.
        """
        ChessHelper.validate_position(start_position)

        board_length = self.get_dimension()
        max_movement = board_length - 1
        num_spaces = max_movement
        current_x_coord, current_y_coord = self.position_to_row_and_column(start_position, piece_color)

        if move_direction == MoveDirection.FORWARD:
            max_movement = board_length - current_y_coord - 1
        elif move_direction == MoveDirection.F_RIGHT_DIAG:
            from_right = board_length - current_x_coord - 1
            from_top = board_length - current_y_coord - 1
            max_movement = min(from_top, from_right)
        elif move_direction == MoveDirection.RIGHT:
            max_movement = board_length - current_x_coord - 1
        elif move_direction == MoveDirection.B_RIGHT_DIAG:
            from_right = board_length - current_x_coord - 1
            max_movement = min(current_y_coord, from_right)
        elif move_direction == MoveDirection.BACKWARD:
            max_movement = current_y_coord
        elif move_direction == MoveDirection.B_LEFT_DIAG:
            max_movement = min(current_y_coord, current_x_coord)
        elif move_direction == MoveDirection.LEFT:
            max_movement = current_x_coord
        elif move_direction == MoveDirection.F_LEFT_DIAG:
            from_top = board_length - current_y_coord - 1
            max_movement = min(from_top, current_x_coord)

        return min(num_spaces, max_movement)

    def _get_position_shifted_by_offset(self, position, direction, offset, piece_color):
        """
        Retrieve position after shifting over by offset in the direction specified. Ex position=a1,
        direction=MoveDirection.right, offset=1, piece_color=Color.white. Return value is a2

        :param position: string
            Algebraic notation position.
        :param offset: int
            Number of times to shift over in direction
        :param piece_color: int
            Color.white or Colore.black
        :return: string
            Algebraic notation position.
        """
        ChessHelper.validate_position(position)

        index = self._position_to_index(position, piece_color)
        shifted_index = index + self.PIECE_SHIFTING[direction] * offset
        return self._index_to_position(shifted_index, piece_color)

    def _position_to_index(self, position, piece_color):
        """
        Convert an algebraic notation position to an index.

        :param position: string
            Algebraic notation for a position.
        :param piece_color: Color
            Color of player who's perspective should be used.
        :return: int
            Index for that position.
        """
        ChessHelper.validate_position(position)

        return self._indexes[piece_color][position]

    def _index_to_position(self, index, piece_color):
        """
        Convert an index to an algebraic notation position.

        :param index: int
            Index in _board_positions list.
        :param piece_color: Color
            Color of player who's perspective should be used.
        :return:
        """
        if not self._is_valid_index(index):
            raise InvalidIndexError(index)

        if piece_color == Color.WHITE:
            position = self._board_positions[index]
        else:
            position = self._board_positions[len(self._indexes[piece_color]) - index - 1]

        return position

    def _remove_piece(self, position):
        """
        Remove a piece from the board.

        :param position: string
            Algebraic notation for a position.
        :return:
        :raises: InvalidPositionError
            If position is not valid, exception will be raised.
        """
        ChessHelper.validate_position(position)

        # Color does not matter since both indexes point to the same board
        index = self._indexes[Color.WHITE][position]
        self._pieces[self._board_positions[index]] = None

    def _get_nearest_piece_in_direction(self, start_position, move_direction, piece_color, ghost_pieces=None):
        """
        Get the nearest piece from the starting position heading in the direction specified. Not expecting
        MoveDirection.l_shape as a direction.

        :param start_position: string
            Position to start searching from
        :param move_direction: int
            Direction to search in. Ex MoveDirection.forward
        :param piece_color: Color
            Color of player who's perspective should be used.
        :param ghost_pieces: dict
            Positions to either ignore or contain ghost pieces.
        :return: dict
            [position]
            [color]
            [offset]
            [type]
        """
        ChessHelper.validate_position(start_position)

        offset = 0
        positions = self._get_possible_positions(start_position, move_direction, piece_color)

        for position in positions:
            offset += 1
            piece_on_destination = self.is_position_occupied(position)

            ghost_pieces = {} if not ghost_pieces else ghost_pieces
            if position in ghost_pieces and not ghost_pieces[position]:
                continue
            elif position in ghost_pieces:
                return {
                    'position': position,
                    'color': ghost_pieces[position]['color'],
                    'offset': offset,
                    'type': ghost_pieces[position]['type']
                }
            elif piece_on_destination:
                piece = self[position]
                return {
                    'position': position,
                    'color': piece.color,
                    'offset': offset,
                    'type': piece.type
                }

        return None

    def _is_valid_index(self, index):
        """
        Check if an index is in valid range

        :param index: int
            Index value
        """
        if index < 0 or index >= self.get_dimension() ** 2:
            return False
        return True

    def _on_same_row(self, position_one, position_two):
        """
        Determine if both positions are on the same row.

        :param position_one: string
            Position in algebraic notation.
        :param position_two: string
            Position in algebraic notation.
        :return:
        """
        # Color does not matter when checking if on same row
        column_one, row_one = self.position_to_row_and_column(position_one, Color.WHITE)
        column_two, row_two = self.position_to_row_and_column(position_two, Color.WHITE)

        return row_one == row_two

    def _direction_and_position_offset(self, start_position, end_position, color):
        """
        Determine the direction and number of positions away end_position is relative to start_position.

        :param start_position: string
            Position in algebraic notation.
        :param end_position: string
            Position in algebraic notation.
        :param color: int
            Dictionary where MoveDirection is the key and value is a tuple containing the number of rows and columns
            end_position is away. Treats start_position as 0,0 on x,y coordinate system. Ex a2 would be (1,1) from a1
        :return: MoveDirection value
        """
        ChessHelper.validate_position(start_position)
        ChessHelper.validate_position(end_position)

        start_column, start_row = self.position_to_row_and_column(start_position, color)
        end_column, end_row = self.position_to_row_and_column(end_position, color)
        row_diff = end_row - start_row
        column_diff = end_column - start_column

        # Compute offsets
        is_forward = row_diff > 0
        is_back = row_diff < 0
        is_right = column_diff > 0
        is_left = column_diff < 0

        # Determine direction
        if is_forward and is_right:
            positions_away = {'direction': MoveDirection.F_RIGHT_DIAG, 'offset': (column_diff, row_diff)}
        elif is_forward and is_left:
            positions_away = {'direction': MoveDirection.F_LEFT_DIAG, 'offset':  (column_diff, row_diff)}
        elif is_back and is_right:
            positions_away = {'direction': MoveDirection.B_RIGHT_DIAG, 'offset':  (column_diff, row_diff)}
        elif is_back and is_left:
            positions_away = {'direction': MoveDirection.B_LEFT_DIAG, 'offset':  (column_diff, row_diff)}
        elif is_forward:
            positions_away = {'direction': MoveDirection.FORWARD, 'offset':  (column_diff, row_diff)}
        elif is_back:
            positions_away = {'direction': MoveDirection.BACKWARD, 'offset':  (column_diff, row_diff)}
        elif is_right:
            positions_away = {'direction': MoveDirection.RIGHT, 'offset':  (column_diff, row_diff)}
        elif is_left:
            positions_away = {'direction': MoveDirection.LEFT, 'offset': (column_diff, row_diff)}
        else:
            positions_away = {'direction': None, 'offset': (0, 0)}

        return positions_away

    def __str__(self):
        """
        Return a string representation of the chess board.

        :return: string
            Board from white players perspective. All white pieces are a capital letter and black pieces are lowercase.
            Hashes represent a blank square.
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
        Retrieve the piece at the specified position.

        :param position: string
            Algebraic notation for a position.
        :return: Piece
            Return a piece object if a piece exist at the supplied position. Return None if there is no piece.
        """
        return self._pieces[position]

    def __setitem__(self, position, piece):
        """
        Put a piece on the board at the specified position.

        :param position: string
            Algebraic notation for a position.
        :param piece: Piece
            Piece object.
        :return:
        """
        ChessHelper.validate_position(position)

        self._pieces[position] = copy.deepcopy(piece)
        if piece.type == Type.KING:
            self._king_positions[piece.color] = position


if __name__ == '__main__':
    fen = Fen()
    board = ChessBoard(fen)
    print(board)
