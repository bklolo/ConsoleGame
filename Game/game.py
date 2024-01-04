import os
import msvcrt
import time
import Board
import sys

SIZE = 29   # board size

##-- Globel Varibles --##
player_name = 'X'         ##-- This is for the Funtion char_creation()            --##
player_class_choice = 'X' ##-- This is also for the Funtion char_creation()       --##
player_in_game = 'X'      ##-- Again this is also for the Funtion char_creation() --##
mob = 'X'                 ##-- This varible is to hold the current mob player is fighing --##
gender = 'X'              ##-- This varible sets the pronouns for the story and is set in the function in char_creation() in gender_call() --##
opening = True            ##-- Only True if hasnt seen opening story --##
turn = True               ##-- If True it's the players turn         --##
x = 5                     ##-- Y Coords --##
y = 0                     ##-- X Coords --##
sub_x = 0                 ##-- For Map in side of biome --##
sub_y = 0                 ##--  ^^       ^^       ^^    --##
biome_or_subBiome = False ##-- To see if player is in a biome or not --##

##-- Map sizes --##
small = 100
medium = 500
large = 1000

player_char = '.'

# MSVCRT: Microsoft Visual C Runtime module 
# Read/decode a single keypress without waiting for the user to press Enter
def get_key():
    return msvcrt.getch().decode('utf-8')

# Print the game environment
def print_board(board, player_position, player_char):
    # check for door/mountain/etc here ???
    # example: if player_position == door_pos: level = next_level

    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console
    display = ""
    for y_index, row in enumerate(board):
        for x_index, cell in enumerate(row):
            if (y_index, x_index) == player_position:
                display += player_char + ' '
            else:
                display += cell + ' '
        display += '\n'

    sys.stdout.write(display)
    sys.stdout.flush()  # console print replaces last print (less flickering)



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

# The main game loop
level1 = Board.Level_1()
field = Board.Field()
def update_scene():
    board, position = level1
    print_board(board, position, player_char)

    while True:
        if msvcrt.kbhit():
            direction = get_key().lower()
            if direction in ['w', 'a', 's', 'd']:
                position = move_player(board, position, direction)
                print_board(board, position, player_char)
                
        #time.sleep(0.1)

# Check if the script is being run as the main program
if __name__ == "__main__":
    update_scene()