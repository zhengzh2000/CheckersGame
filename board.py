import pygame
from .abbre import BLACK, ROWS, RED, SQUARE_SIZE, COLS, BROWN, TAN
from .piece import Piece


class Board:
    def __init__(self):
        self.board = []
        self.black_left = self.red_left = 12
        self.black_king = self.red_king = 0
        self.create_board()

    def draw_squares(self, p):
        p.fill(BROWN)
        for row in range(ROWS):
            for col in range(row % 2, COLS, 2):
                pygame.draw.rect(p, TAN, (row*SQUARE_SIZE,
                                 col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def get_all_pieces(self, color):
        pieces = []
        for row in self.board:
            for piece in row:
                if piece != 0 and piece.color == color:
                    pieces.append(piece)
        return pieces

    def move(self, piece, row, col):
        a = self.board[piece.row][piece.col]
        b = self.board[row][col]
        a, b = b, a
        piece.move(row, col)

        if row == ROWS - 1 or row == 0:
            piece.make_king()
            if piece.color == RED:
                self.red_king += 1
            else:
                self.black_king += 1

    def get_piece(self, row, col):
        return self.board[row][col]

    def create_board(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                if col % 2 == ((row + 1) % 2):
                    if row < 3:
                        self.board[row].append(Piece(row, col, RED))
                    elif row > 4:
                        self.board[row].append(Piece(row, col, BLACK))
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)

    def draw_all(self, p):
        self.draw_squares(p)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(p)

    def remove(self, pieces):
        for piece in pieces:
            self.board[piece.row][piece.col] = 0
            if piece != 0:
                if piece.color == BLACK:
                    self.black_left -= 1
                else:
                    self.red_left -= 1

    def winner(self):
        if self.black_left <= 0:
            return RED
        elif self.red_left <= 0:
            return BLACK
        return None

    def get_valid_moves(self, piece):
        moves = {}
        left = piece.col - 1
        right = piece.col + 1
        row = piece.row

        if piece.color == BLACK or piece.king:
            moves.update(self.left(
                row - 1, max(row-3, -1), -1, piece.color, left))
            moves.update(self.right(
                row - 1, max(row-3, -1), -1, piece.color, right))
        if piece.color == RED or piece.king:
            moves.update(self.left(
                row + 1, min(row+3, ROWS), 1, piece.color, left))
            moves.update(self.right(
                row + 1, min(row+3, ROWS), 1, piece.color, right))

        return moves

    def left(self, start, stop, step, color, left, skipped=[]):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if left < 0:
                break

            current = self.board[r][left]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, left)] = last + skipped
                else:
                    moves[(r, left)] = last

                if last:
                    if step == -1:
                        row = max(r-3, 0)
                    else:
                        row = min(r+3, ROWS)
                    moves.update(self.left(
                        r+step, row, step, color, left-1, skipped=last))
                    moves.update(self.right(
                        r+step, row, step, color, left+1, skipped=last))
                break
            elif current.color == color:
                break
            else:
                last = [current]

            left -= 1

        return moves

    def right(self, start, stop, step, color, right, skipped=[]):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if right >= COLS:
                break

            current = self.board[r][right]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, right)] = last + skipped
                else:
                    moves[(r, right)] = last

                if last:
                    if step == -1:
                        row = max(r-3, 0)
                    else:
                        row = min(r+3, ROWS)
                    moves.update(self.left(
                        r+step, row, step, color, right-1, skipped=last))
                    moves.update(self.right(
                        r+step, row, step, color, right+1, skipped=last))
                break
            elif current.color == color:
                break
            else:
                last = [current]

            right += 1

        return moves

    def evaluate(self):
        return self.red_left - self.black_left + (self.red_king * 0.5 - self.black_king * 0.5)
