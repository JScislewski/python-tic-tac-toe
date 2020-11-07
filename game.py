from os import system, name
import random


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


def player_input():
    """
    OUTPUT = (Player 1 marker, Player 2 marker)
    """
    marker = ""
    while not (marker == "X" or marker == "O"):
        marker = input("Player1: Choose X or O: ").upper()
    if marker == "X":
        return ("X", "O")
    else:
        return ("O", "X")


def place_marker(board, marker, position):
    board[position] = marker


def win_check(board, marker):
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


def choose_first():
    flip = random.randint(0, 1)
    if flip == 0:
        return "Player 1"
    else:
        return "Player 2"


clear_screen()
test_board = ["#", "X", "O", "X", "O", "X", "O", "X", "O", "X"]
player1_marker, player2_marker = player_input()
display_board(test_board)
place_marker(test_board, "@", 3)
display_board(test_board)
