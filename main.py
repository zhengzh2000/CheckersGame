'''
I was watching Tech with Tim while writing the final checker project, because I really have no idea how to write this assignment. 
The link is https://www.youtube.com/watch?v=vnd3RfeG3NM. 
'''
import pygame
from checkers.abbre import WIDTH, HEIGHT, SQUARE_SIZE, RED
from checkers.game import Game
from checkers.aimove import aimove


p = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers')


def mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col


def main():
    run = True
    game = Game(p)

    while run:

        if game.turn == RED:
            new_board = aimove(game.get_board(), 4, RED, game)
            game.ai_move(new_board)

        if game.winner() != None:
            print(game.winner())
            run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = mouse(pos)
                game.select(row, col)

        game.update()

    pygame.quit()


main()
