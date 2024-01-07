# Python libraries
import os
import sys
import msvcrt
# Custom classes
import board
import PlayerController as player


player_char = '.'


def get_key_press():
    return msvcrt.getch().decode('utf-8')


def main_game_loop():
    # Board initialization
    board.print_title(30)
    input()
    level, player_start_pos = board.Level_1()
    board.print_level(level, player_start_pos, player_char)
    player_pos = player_start_pos
    # Character initialization

    # Game loop
    while True:
        if msvcrt.kbhit():
            direction = get_key_press().lower()
            if direction in ['w', 'a', 's', 'd']:
                player_pos = player.move(level, player_pos, direction)
                board.print_level(level, player_pos, player_char)


if __name__ == "__main__":
    main_game_loop()

