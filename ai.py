import math
import random

from game_utils import (
    has_won,
    is_board_empty,
    is_board_full,
    is_field_free,
    no_empty_fields,
    place_marker,
)


def minimax(board, depth, isMaximizing):
    if has_won(board, "X"):
        return 1
    if has_won(board, "O"):
        return -1
    if is_board_full(board):
        return 0
    if isMaximizing:
        best_score = -math.inf
        for i in range(1, 10):
            score = -math.inf
            if is_field_free(board, i):
                place_marker(board, "X", i)
                score = minimax(board, depth + 1, False)
                board[i] = " "
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(1, 10):
            score = math.inf
            if is_field_free(board, i):
                place_marker(board, "O", i)
                score = minimax(board, depth + 1, True)
                board[i] = " "
            best_score = min(score, best_score)
        return best_score


def ai_move(board):
    best_move = 0
    if is_board_empty(board):
        best_move = random.randint(1, 9)
    else:
        best_score = -math.inf
        for i in range(1, 10):
            score = -math.inf
            if is_field_free(board, i):
                place_marker(board, "X", i)
                score = minimax(board, 0, False)
                board[i] = " "
            if score > best_score:
                best_score = score
                best_move = i
    place_marker(board, "X", best_move)
