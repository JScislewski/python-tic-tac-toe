import random
import time
from os import name, system


def is_field_free(board, position):
    return board[position] == " "


def is_board_full(board):
    for i in range(1, 10):
        if is_field_free(board, i):
            return False
    return True


def is_board_empty(board):
    for i in range(1, 10):
        if board[i] != " ":
            return False
    return True


def no_empty_fields(board):
    empty_fields = 0
    for i in range(1, 10):
        if board[i] == " ":
            empty_fields += 1
    return empty_fields


def clear_screen():
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")


def display_board(board):
    clear_screen()
    print("| " + board[7] + " | " + board[8] + " | " + board[9] + " |")
    print("| " + board[4] + " | " + board[5] + " | " + board[6] + " |")
    print("| " + board[1] + " | " + board[2] + " | " + board[3] + " |")


def random_markers():
    flip = random.randint(0, 1)
    if flip == 0:
        return ("X", "O")
    else:
        return ("O", "X")


def place_marker(board, marker, position):
    board[position] = marker


def has_won(board, marker):
    return (
        (board[1] == marker and board[2] == marker and board[3] == marker)
        or (board[4] == marker and board[5] == marker and board[6] == marker)
        or (board[7] == marker and board[8] == marker and board[9] == marker)
        or (board[1] == marker and board[5] == marker and board[9] == marker)
        or (board[7] == marker and board[5] == marker and board[3] == marker)
        or (board[7] == marker and board[4] == marker and board[1] == marker)
        or (board[8] == marker and board[5] == marker and board[2] == marker)
        or (board[9] == marker and board[6] == marker and board[3] == marker)
    )


def select_position(board):
    position = 0

    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not is_field_free(
        board, position
    ):
        position = int(input("Choose position (1-9): "))
    return position


def replay():
    choice = input("Play again? Enter 'y' or 'n': ")
    return choice == "y"
