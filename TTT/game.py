# listen over hvad jeg skal have med

# add board
# add display board
# play game
# handle turn
# check win
    # check rows
    # check columns
    # check diagonals
# check tie
# flip playser

board = ["-","-","-",
         "-","-","-",
         "-","-","-" ]

def display_board():
    print(board[0] + "  |  " + board[1] + "  |  " + board[2])
    print(board[3] + "  |  " + board[4] + "  |  " + board[5])
    print(board[6] + "  |  " + board[7] + "  |  " + board[8])

def play_game():
    display_board()

    while game_still_going:

        handle_turn(current_player)
        Check_if_game_over()
def handle_turn():
    position = input("Vælg en position fra 1-9:")
    position = int(position) - 1

    board[position] = "X"
    display_board()

play_game()