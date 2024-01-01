import os
import time
import math
import msvcrt
import shutil
import random

SLEEP_DURATION = 0.01

def get_console_size():
    try:
        columns, rows = shutil.get_terminal_size()
        return columns, rows
    except shutil.Error:
        return 80, 25  # Default values if unable to get console size

def move_char_back(my_list, char):
    if char in my_list:
        char_index = my_list.index(char)
        if char_index > 0:
            my_list[char_index], my_list[char_index - 1] = my_list[char_index - 1], my_list[char_index]

def move_char_forward(my_list, char):
    if char in my_list:
        char_index = my_list.index(char)
        if char_index < len(my_list) - 1:
            my_list[char_index], my_list[char_index + 1] = my_list[char_index + 1], my_list[char_index]

def print_track(track):
    print(*track, sep='')

def main():
    console_width, console_height = get_console_size()
    length = console_width - 1
    space = '0'
    track = [space] * length
    toon = '-'
    track.insert(0, toon)

    try:
        while True:
            # Move char to the left
            for x in range(length):
                move_char_forward(track, toon)
                print_track(track)
                time.sleep(SLEEP_DURATION)

            # Move char to the right
            for x in range(length):
                move_char_back(track, toon)
                print_track(track)
                time.sleep(SLEEP_DURATION)

    except KeyboardInterrupt:
        print("\nProgram terminated.")

def fill_board(rows, cols):
    symbols = ['*', '#', '@', '$', '%', '&']  # Add more symbols as needed
    my_dict = {}

    for row in range(1, rows + 1):
        for col in range(1, cols + 1):
            my_dict[f'{row}{col}'] = random.choice(symbols)

    return my_dict

def print_board(board):
    print(board[{0,0}])
    

length = width = 5
play = True
# Game initialization
while play:
    # print ze board
    board = fill_board(length,width)
    print_board(board)
    play = False
        # set player in bottom-middle
    # Functinoality
        # move with arrow keys


if __name__ == "__main__":
    main()
