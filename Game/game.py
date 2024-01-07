# Python libraries
import os
import sys
import msvcrt
import time
# Custom classes
from Board import Board
from PlayerController import PlayerController

# TODO:
# movement issue: character runs too quickly; time.sleep(); buffered input


def get_key_press():
    return msvcrt.getch().decode('utf-8')


def main_game_loop():
    # Board initialization
    initial_position = (5,18)
    board_instance = Board('Game\\world.txt', 20, 16, initial_position)
    player_controller = PlayerController(board_instance)
    # Print title
    board_instance.print_title(30)
    # Wait for user ENTER
    input()
    # Select first level
    board_instance.select_level()
    # Print to console
    board_instance.print_level()

    # Game loop
    while True:
        if msvcrt.kbhit():
            direction = get_key_press().lower()
            if direction in ['w', 'a', 's', 'd']:
                player_controller.move(direction)
                board_instance.print_level()
                board_instance.print_player_pos()
            time.sleep(0.1)


if __name__ == "__main__":
    main_game_loop()

