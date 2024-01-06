# Python libraries
import os
import sys
import msvcrt
# Custom classes
import board


player_char = '$'


def get_key_press():
    return msvcrt.getch().decode('utf-8')

    
def print_level(level, player_player_pos=None, player_char=None):
    os.system('cls' if os.name == 'nt' else 'clear')
    for y_index, row in enumerate(level):
        for x_index, cell in enumerate(row):
            if (y_index, x_index) == player_player_pos:
                print(player_char, end=' ')
            else:
                print(cell, end=' ')
        print()

    
def move_player(level, player_pos, direction):
    row, col = player_pos
    new_row, new_col = row, col

    if direction == 'w' and row > 0:
        new_row -= 1
    elif direction == 's' and row < len(level) - 1:
        new_row += 1
    elif direction == 'a' and col > 0:
        new_col -= 1
    elif direction == 'd' and col < len(level[0]) - 1:
        new_col += 1

    return new_row, new_col


def main_game_loop():
    board.print_title()
    input()
    level, player_pos = board.generate_level()
    print_level(level, player_pos, player_char)

    while True:
        if msvcrt.kbhit():
            direction = get_key_press().lower()
            if direction in ['w', 'a', 's', 'd']:
                player_pos = move_player(level, player_pos, direction)
                print_level(level, player_pos, player_char)


if __name__ == "__main__":
    main_game_loop()

