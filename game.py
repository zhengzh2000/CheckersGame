import pygame
from .abbre import RED, BLACK
from checkers.board import Board


class Game:
    def __init__(self, p):
        self.reset()
        self.p = p

    def update(self):
        self.board.draw_all(self.p)
        pygame.display.update()

    def reset(self):
        self.selected = None
        self.board = Board()
        self.turn = BLACK
        self.valid_moves = {}

    def winner(self, username):
        records = loadStrings("record.txt")
        record_dict = {}
        for record in records:
            record = record.strip()
            name, wins = record.split()[0], record.split()[1]
            record_dict[name] = int(wins)
        if record_dict.get(username):
            record_dict[username] += 1
        else:
            record_dict[username] = 1
        record_list = [(key, val)for (key, val) in record_dict.items()]
        record_list = sorted(record, key=lambda item: item[1], reverse=True)
        record_write = []
        for r in record_list:
            record_write.append(r[0]+" "+str(r[1]))
        saveStrings("record.txt", record_write)
        return self.board.winner()

    def select(self, row, col):
        if self.selected:
            result = self.piece_move(row, col)
            if not result:
                self.selected = None
                self.select(row, col)

        piece = self.board.get_piece(row, col)
        if piece != 0 and piece.color == self.turn:
            self.selected = piece
            self.valid_moves = self.board.get_valid_moves(piece)
            return True

        return False

    def change_turn(self):
        self.valid_moves = {}
        if self.turn == BLACK:
            self.turn = RED
        else:
            self.turn = BLACK

    def piece_move(self, row, col):
        piece = self.board.get_piece(row, col)
        if self.selected and piece == 0 and (row, col) in self.valid_moves:
            self.board.move(self.selected, row, col)
            skipped = self.valid_moves[(row, col)]
            if skipped:
                self.board.remove(skipped)
            self.change_turn()
        else:
            return False
        return True

    def get_board(self):
        return self.board

    def ai_move(self, board):
        self.board = board
        self.change_turn()
