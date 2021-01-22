from os import system, name
import time
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


def random_markers():
    flip = random.randint(0, 1)
    if flip == 0:
        return ("X", "O")
    else:
        return ("O", "X")


def display_whos_turn(player, marker):
    print(player + "(" + marker + ")" + " turn")


def place_marker(board, marker, position):
    board[position] = marker


def has_player_won(board, marker):
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


def choose_starting_player(player_marker, ai_marker):
    print("Randomly choosing starting player...")
    time.sleep(1)
    if player_marker == "X":
        return "Player"
    else:
        return "AI"


def is_field_free(board, position):
    return board[position] == " "


def is_board_full(board):
    for i in range(1, 10):
        if is_field_free(board, i):
            return False
    return True


def select_position(board):
    position = 0

    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not is_field_free(
        board, position
    ):
        position = int(input("Choose position (1-9): "))
    return position


def ai_move(board, ai_marker):
    position = ""
    for i in range(1, 10):
        if position == "" and is_field_free(board, i):
            position = i
    place_marker(board, ai_marker, position)


def replay():
    choice = input("Play again? Enter 'yes' or 'no': ")
    return choice == "yes"


while True:
    clear_screen()
    game_board = [" "] * 10
    player_marker, ai_marker = random_markers()
    turn = choose_starting_player(player_marker, ai_marker)
    print("\n" + turn + " will start")

    play_game = input("Are You ready to start the game? 'y' or 'n': ")

    if play_game == "y":
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == "Player":
            display_board(game_board)
            selected_position = select_position(game_board)
            place_marker(game_board, player_marker, selected_position)

            if has_player_won(game_board, player_marker):
                display_board(game_board)
                print("Player has won!")
                game_on = False
            else:
                if is_board_full(game_board):
                    display_board(game_board)
                    print("It's a tie!")
                    game_on = False
                else:
                    turn = "AI"
        else:
            ai_move(game_board, ai_marker)
            display_board(game_board)
            if has_player_won(game_board, ai_marker):
                display_board(game_board)
                print("AI has won!")
                game_on = False
            else:
                if is_board_full(game_board):
                    display_board(game_board)
                    print("It's a tie")
                    game_on = False
                else:
                    turn = "Player"

    if not replay():
        break
