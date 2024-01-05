import os
import msvcrt
import time

SIZE = 29   # board size

# Print the game environment
def print_board(board, player_position):
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console
    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if (i, j) == player_position:
                print('.', end=' ')
            else:
                print(cell, end=' ')
        print()

# Move the player across rows/columns
def move_player(board, player_position, direction):
    row, col = player_position
    new_row, new_col = row, col
    # Need to check for collisions here
    if direction == 'w' and row > 0:
        new_row -= 1
    elif direction == 's' and row < len(board) - 1:
        new_row += 1
    elif direction == 'a' and col > 0:
        new_col -= 1
    elif direction == 'd' and col < len(board[0]) - 1:
        new_col += 1

    return new_row, new_col

# MSVCRT: Microsoft Visual C Runtime module 
# Read/decode a single keypress without waiting for the user to press Enter
def get_key():
    return msvcrt.getch().decode('utf-8')

# The main game loop
def update_scene():

    ##################
    # INITIALIZATION #
    ##################
    
    # original board (player centered among blanks)
    #board = [['.' for _ in range(SIZE)] for _ in range(SIZE)]

    # static level (string format for ease of editing)
    level_layout = [
        "####################",
        "#MMMMMMMMM         #",
        "#MMMMMMMMM         #",
        "#MMMM              #",
        "#MMMM              #",
        "#MMMM              #",
        "#                  #",
        "#MMMM      T  T    #",
        "#MMMM     T TT     #",
        "#MMMM              #",
        "#MMMM              #",
        "#                  #",
        "#MMMMMMMMMMMMMMMMMM#",
        "#RRRRRRRRRRRRRRRRRRR#",
        "#TTTTTTTTTTTTTTTTTTT#",
        "####################",
    ]
    # convert strings to list of chars
    board = [list(row) for row in level_layout]
    # define player position
    player_position = (SIZE//2, SIZE//2)

    # board, player_position = Board.Level_1()

    print_board(board, player_position)
    
    while True:
        if msvcrt.kbhit():
            direction = get_key().lower()

            if direction in ['w', 'a', 's', 'd']:
                player_position = move_player(board, player_position, direction)
                print_board(board, player_position)

        #time.sleep(0.1)

if __name__ == "__main__":
    # initialiazation

    # update scene
    update_scene()