from os import system, name


def clear_screen():
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")


def display_board(board):
    print("| " + board[7] + " | " + board[8] + " | " + board[9] + " |")
    print("| " + board[4] + " | " + board[5] + " | " + board[6] + " |")
    print("| " + board[1] + " | " + board[2] + " | " + board[3] + " |")
    clear_screen()
    print("| " + board[7] + " | " + board[8] + " | " + board[9] + " |")
    print("| " + board[4] + " | " + board[5] + " | " + board[6] + " |")
    print("| " + board[1] + " | " + board[2] + " | " + board[3] + " |")


test_board = ["#", "X", "O", "X", "O", "X", "O", "X", "O", "X"]
display_board(test_board)
