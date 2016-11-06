#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week 11 Synthesizing Task"""

import time


class ChessPiece(object):
    """A board game piece class.
    Stores the starting position for a piece on a chess board.
    Args:
        position (string): position of piece as algebraic notiation, starting
        with a letter, and followed by a number.
    Attributes:
        position (string): position of piece as algebraic notiation, starting
        with a letter, and followed by a number.
    """

    prefix = ''

    def __init__(self, position):
        """Constructor for ChessPiece() class.
        Args:
            position(string): position of piece as algebraic notiation, starting
            with a letter, and followed by a number.
        Attributes:
            ChessPiece (class): Calls the ChessPiece() class.
            position (string): determines starting position on board for piece.
        Retruns:
            ValueError if start position is not legal.
        """
        self.position = position
        self.moves = []
        if not self.algebraic_to_numeric(position):
            excep = '`{}` is not a legal start position'
            raise ValueError(excep.format(position))

    def algebraic_to_numeric(self, tile):
        """Returns the position of chess piece as a tuple.
        Args:
            tile (string): The next position for the game piece as algebraic
            notation.
        Returns:
            position (tuple): The algebraic notation converted into a tuple
            containing a zero-based x- and y-value.
        Examples:
            >>> piece = ChessPiece('a1')
            >>> piece.algebraic_to_numeric('a2')
            >>> (0, 1)
        """
        x_coord = {0: ['a', 1],
                   1: ['b', 2],
                   2: ['c', 3],
                   3: ['d', 4],
                   4: ['e', 5],
                   5: ['f', 6],
                   6: ['g', 7],
                   7: ['h', 8]}

        y_coord = int(tile[1:])
        self.tileconvert = []
        for xkey, xval in x_coord.iteritems():
            if tile[0] in xval:
                self.tileconvert.append(xkey)
                for xkey, xval in x_coord.iteritems():
                    if y_coord in xval:
                        self.tileconvert.append(xkey)
        if len(self.tileconvert) is 2:
            return tuple(self.tileconvert)
        else:
            return None

    def is_legal_move(self, position):
        """Returns whether or not move is legal.
        Args:
            position (string): The next position for the game piece as algebraic
            notation.
        Returns:
            boolean: Returns ``True`` if the next position is a legal move on
            the chess board or ``False`` if it is not.
        Examples:
            >>> piece.is_legal_move('a5')
            >>> True
            >>> piece.is_legal_move('j9')
            >>> False
        """
        if self.algebraic_to_numeric(position):
            return True
        else:
            return False

    def move(self, position):
        """Returns the new position of the piece and a timestamp.
        Args:
            position (string): The next position for the game piece as algebraic
            notation.
        Returns:
            tuple: Previous position, new position and the timestamp inside of
            a tuple.
        Examples:
            >>> piece.move('a3')
            ('a1', 'a3', 1413252815.610075)
        """
        if self.is_legal_move(position):
            newmove = (self.prefix + self.position, self.prefix + position,
                       time.time())
            self.moves.append(newmove)
            self.position = position
            return newmove
        else:
            return False


class Rook(ChessPiece):
    """A Rook Chess Piece.
    Modifies the ChessPiece() class.
    Args:
        position (string): position of piece as algebraic notiation, starting
        with a letter, and followed by a number.
    Attributes:
        ChessPiece (class): calls the ChessPiece() class.
        position (string): position of piece as algebraic notiation, starting
        with a letter, and followed by a number.
    """

    def __init__(self, position):
        """Constructor for the Rook() class.
        Args:
            position (string): position of piece as algebraic notiation,
            starting with a letter, and followed by a number.
        Attribues:
            ChessPiece (class): Calls the ChessPiece() class.
        """
        self.prefix = 'R'
        self.position = position
        ChessPiece.__init__(self, position)

    def is_legal_move(self, position):
        """Returns whether or not move is legal for Rook Piece.
        Args:
            position (string): The next position for the game piece as algebraic
            notation.
        Returns:
            Boolean: Returns ``True`` if the next position is a legal move for a
            rook on the chess board or ``False`` if it is not.
        Examples:
            >>> piece.is_legal_move('a5')
            >>> True
            >>> piece.is_legal_move('b3')
            >>> False
        """
        curpos = self.algebraic_to_numeric(self.position)
        newpos = self.algebraic_to_numeric(position)
        if newpos[0] == curpos[0] and 0 <= curpos[1] <= 7:
            return True
        elif newpos[1] == curpos[1] and 0 <= curpos[0] <= 7:
            return True
        else:
            return False


class Bishop(ChessPiece):
    """A Bishop Chess Piece.
    Modifies the ChessPiece() class.
    Args:
        position (string): position of piece as algebraic notiation, starting
        with a letter, and followed by a number.
    Attributes:
        ChessPiece (class): calls the ChessPiece() class.
        position (string): position of piece as algebraic notiation, starting
        with a letter, and followed by a number.
    """

    def __init__(self, position):
        """Constructor for the Bishop() class.
        Args:
            position (string): position of piece as algebraic notiation,
            starting with a letter, and followed by a number.
        Attribues:
            ChessPiece (class): Calls the ChessPiece() class.
        """
        self.prefix = 'B'
        self.position = position
        ChessPiece.__init__(self, position)

    def is_legal_move(self, position):
        """Returns whether or not move is legal for the Bishop piece.
        Args:
            position (string): The next position for the game piece as algebraic
            notation.
        Returns:
            Boolean: Returns ``True`` if the next position is a legal move for a
            bishop on the chess board or ``False`` if it is not.
        Examples:
            >>> piece.is_legal_move('b2')
            >>> True
            >>> piece.is_legal_move('a7')
            >>> False
        """
        curpos = self.algebraic_to_numeric(self.position)
        newpos = self.algebraic_to_numeric(position)
        if abs(newpos[0] - curpos[0]) == abs(newpos[1] - curpos[1]):
            if 0 <= newpos[0] <= 7 and 0 <= newpos[1] <= 7:
                return True
            else:
                return False
        else:
            return False


class King(ChessPiece):
    """A King Chess Piece.
    Modifies the ChessPiece() class.
    Args:
        position (string): position of piece as algebraic notiation, starting
        with a letter, and followed by a number.
    Attributes:
        ChessPiece (class): calls the ChessPiece() class.
        position (string): position of piece as algebraic notiation, starting
        with a letter, and followed by a number.
    """
    def __init__(self, position):
        """Constructor for the King() class.
        Args:
            position (string): position of piece as algebraic notiation,
            starting with a letter, and followed by a number.
        Attribues:
            ChessPiece (class): Calls the ChessPiece() class.
        """
        self.prefix = 'K'
        self.position = position
        ChessPiece.__init__(self, position)

    def is_legal_move(self, position):
        """Returns whether or not move is legal for the King piece.
        Args:
            position (string): The next position for the game piece as algebraic
            notation.
        Returns:
            Boolean: Returns ``True`` if the next position is a legal move for a
            king on the chess board or ``False`` if it is not.
        Examples:
            >>> piece.is_legal_move('b2')
            >>> True
            >>> piece.is_legal_move('e6')
            >>> False
        """
        curpos = self.algebraic_to_numeric(self.position)
        newpos = self.algebraic_to_numeric(position)
        if 0 <= newpos[0] <= 7 and 0 <= newpos[1] <= 7:
            if curpos[0] + 1 == newpos[0] and curpos[1] == newpos[1]:
                return True
            elif curpos[0] + 1 == newpos[0] and curpos[1] + 1 == newpos[1]:
                return True
            elif curpos[0] + 1 == newpos[0] and curpos[1] - 1 == newpos[1]:
                return True
            elif curpos[0] == newpos[0] and curpos[1] - 1 == newpos[1]:
                return True
            elif curpos[0] - 1 == newpos[0] and curpos[1] - 1 == newpos[1]:
                return True
            elif curpos[0] - 1 == newpos[0] and curpos[1] == newpos[1]:
                return True
            elif curpos[0] - 1 == newpos[0] and curpos[1] + 1 == newpos[1]:
                return True
            elif curpos[0] == newpos[0] and curpos[1] + 1 == newpos[1]:
                return True
        else:
            return False


class ChessMatch(object):
    """A board game class.
    Stores the pieces and their positions on the game board.
    Args:
        pieces (dict): position of piece as full algebraic notiation, starting
        with a capital letter, then a lower-case letter and followed by a
        number for the key, the instance of the piece's class as the value.
    Attributes:
        pieces (dict): position of piece as full algebraic notiation, starting
        with a capital letter, then a lower-case letter and followed by a
        number for the key, the instance of the piece's class as the value.
    """

    def __init__(self, pieces=None):
        """Constructor for the ChessMatch() class.
        Args:
            pieces (dict): position of piece as full algebraic notiation,
            followed by the instance of the piece's class as the value.
            Defaults to None.
        Attributes:
            pieces (dict): position of piece as full algebraic notiation,
            followed by the instance of the piece's class as the value.
            Defaults to None.
        """
        self.pieces = pieces
        if self.pieces is None:
            self.reset()
        else:
            self.pieces = pieces
            self.log = []

    def reset(self):
        """Resets the positions of the pieces on the game board.
        Returns:
            pieces (dict): position of piece as full algebraic notiation,
            followed by the instance of the piece's class as the value. Default
            starting values for each piece are insterted.
        """
        self.pieces = {'Ra1': Rook('a1'),
                       'Rh1': Rook('h1'),
                       'Ra8': Rook('a8'),
                       'Rh8': Rook('h8'),
                       'Bc1': Bishop('c1'),
                       'Bf1': Bishop('f1'),
                       'Bc8': Bishop('c8'),
                       'Bf8': Bishop('f8'),
                       'Ke1': King('e1'),
                       'Ke8': King('e8')}
        self.log = []

    def move(self, full_name, position):
        """Calls the specified piece's move() method to move it to new position.
        Args:
            full_name (string): The full notation of the piece's position.
            position (string): The algebraic notation of the piece's next
            postion on the board.
        Examples:
            >>> match = ChessMatch()
            >>> match.move('Ra1', 'a3')
            >>> match.log
            [('Ra1', 'Ra3', 1429532533.977381)]
            >>> match.pieces
            {'Ra3': <__main__.Rook object at 0xb609452c>}
        """
        if full_name[0] is 'R':
            if Rook(full_name[1:]):
                rmove = Rook(full_name[1:]).move(position)
                self.log.append(rmove)
                self.pieces.pop(full_name)
                self.pieces['R' + position] = Rook(position)
            else:
                return False
        elif full_name[0] is 'B':
            if Bishop(full_name[1:]):
                rmove = Bishop(full_name[1:]).move(position)
                self.log.append(rmove)
                self.pieces.pop(full_name)
                self.pieces['B' + position] = Bishop(position)
            else:
                return False
        elif full_name[0] is 'K':
            if King(full_name[1:]):
                rmove = King(full_name[1:]).move(position)
                self.log.append(rmove)
                self.pieces.pop(full_name)
                self.pieces['K' + position] = King(position)
        else:
            return False

    def __len__(self):
        """Magic method for len() function.
        Allows ClassMatch class to be called inside of len() function.
        """
        return len(self.log)
