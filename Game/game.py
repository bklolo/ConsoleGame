# Python libraries
import os
import sys
import msvcrt
import time
# Custom classes
from Board import Board
from PlayerController import PlayerController
from Classes import *

# TODO:
# movement issue: character runs too quickly; time.sleep(); buffered input


def get_key_press():
    return msvcrt.getch().decode('utf-8')


def main_game_loop():
    # Board
    board_width = 20
    board_height = 20
    game_path = 'C:\\Users\\bkl\\Desktop\\Projects\\_FunProjects\\ConsoleGame\\Game\\world.txt'
    generated_path = 'C:\\Users\\bkl\\Desktop\\Projects\\_FunProjects\\ConsoleGame\\generated_world.txt'
    paths = [game_path, generated_path]
    # health, stamina, symbol, position, aggro
    player = Player(100,50,'.',(5,5))
    enemy = Enemy(50,25,';', (7,10), 1)
    board_instance = Board(paths[0], board_width, board_height, player, enemy)
    
    # Player
    player_controller = PlayerController(board_instance)
    
    # Print title
    board_instance.print_title(60)
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
        else:
            board_instance.print_level()
            board_instance.update_enemy()
            time.sleep(0.2)

if __name__ == "__main__":
    main_game_loop()

