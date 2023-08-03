from copy import deepcopy
import pygame
from .abbre import BLACK, RED


def aimove(position, depth, player, game):
    if depth == 0 or position.winner() != None:
        return position.evaluate(), position

    if player:
        maxEval = float('-inf')
        play_move = None
        for i in get_all_moves(position, RED, game):
            eva = aimove(i, depth - 1, False, game)[0]
            maxEval = max(maxEval, eva)
            if maxEval == eva:
                play_move = i

        return maxEval, play_move
    else:
        minEval = float('inf')
        play_move = None
        for i in get_all_moves(position, BLACK, game):
            eva = aimove(i, depth-1, True, game)[0]
            minEval = min(minEval, eva)
            if minEval == eva:
                play_move = i

        return minEval, play_move


def get_all_moves(board, color, game):
    moves = []

    for piece in board.get_all_pieces(color):
        valid_moves = board.get_valid_moves(piece)
        for move, skip in valid_moves.items():
            temp_board = deepcopy(board)
            temp_piece = temp_board.get_piece(piece.row, piece.col)
            new_board = move_less(temp_piece, move, temp_board, game, skip)
            moves.append(new_board)

    return moves


def move_less(piece, move, board, skip):
    board.move(piece, move[0], move[1])
    if skip:
        board.remove(skip)

    return board
