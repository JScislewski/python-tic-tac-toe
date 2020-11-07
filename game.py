from os import system, name


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


test_board = ["#", "X", "O", "X", "O", "X", "O", "X", "O", "X"]

player1_marker, player2_marker = player_input()
display_board(test_board)

print(player1_marker, player2_marker)
