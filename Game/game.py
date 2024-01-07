# Python libraries
import os
import sys
import msvcrt
import time
# Custom classes
import board
import PlayerController as player

# TODO:
# movement issue: character runs too quickly; time.sleep(); buffered input


def get_key_press():
    return msvcrt.getch().decode('utf-8')


def main_game_loop():
    # Board initialization
    board.print_title(30)
    input()
    #level, player_start_pos = board.Level_1()
    board.select_level()
    board.print_level()
    #player_pos = player_start_pos
    # Character initialization

    # Game loop
    while True:
        if msvcrt.kbhit():
            direction = get_key_press().lower()
            if direction in ['w', 'a', 's', 'd']:
                player.move(direction)
                board.print_level()
            time.sleep(0.1)


if __name__ == "__main__":
    main_game_loop()

