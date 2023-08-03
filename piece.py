from .abbre import SQUARE_SIZE, WHITE, CROWN
import pygame


class Piece:
    BORDER = 5
    OUTLINE = 10

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False
        self.x = 0
        self.y = 0
        self.position_circle()

    def position_circle(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    def make_king(self):
        self.king = True

    def draw(self, p):
        radius = SQUARE_SIZE//2 - self.OUTLINE
        pygame.draw.circle(p, WHITE, (self.x, self.y), radius + self.BORDER)
        pygame.draw.circle(p, self.color, (self.x, self.y), radius)
        if self.king:
            p.blit(CROWN, (self.x - CROWN.get_width() //
                   2, self.y - CROWN.get_height()//2))

    def move(self, row, col):
        self.row = row
        self.col = col
        self.position_circle()

    def __repr__(self):
        return str(self.color)
