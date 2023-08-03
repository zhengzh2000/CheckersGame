import pygame

WIDTH = 800
HEIGHT = 800
ROWS = 8
COLS = 8
SQUARE_SIZE = WIDTH//COLS

# rgb
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (128, 128, 128)
BROWN = (160, 82, 45)
TAN = (210, 180, 140)

CROWN = pygame.transform.scale(pygame.image.load('crown.png'), (50, 80))
