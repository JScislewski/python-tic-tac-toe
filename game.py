from ai import ai_move
from game_utils import (
    clear_screen,
    display_board,
    has_won,
    is_board_full,
    place_marker,
    replay,
    select_position,
)

while True:
    clear_screen()
    game_board = [" "] * 10
    turn = "AI"
    game_on = True
    while game_on:
        if turn == "Player":
            display_board(game_board)
            selected_position = select_position(game_board)
            place_marker(game_board, "O", selected_position)

            if has_won(game_board, "O"):
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
            ai_move(game_board)
            display_board(game_board)
            if has_won(game_board, "X"):
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
