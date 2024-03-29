# Python libraries
import os   
import sys
import time
import random
# Custom classes
import Items
from Classes import *
import tools.WorldGenerator as wg


class Board:
    def __init__(self, level_path, level_width, level_height, player, enemy):
        #self.player_char = player.symbol
        self.level_path = level_path
        self.level_width = level_width
        self.level_height = level_height
        self.current_level = []
        self.current_level_index = (0, 0)
        self.traversable = [' ']
        self.ports = ['[', ']', '=']
        # Player
        self.player = player
        # Enemy
        self.enemy = enemy
        self.enemy_last_move_time = 0

        self.select_level()
############################################################################### Enemy START
    def update_enemy(self):
            enemy_y, enemy_x = self.enemy.position
            player_y, player_x = self.player.position

            # Determine the direction of movement
            y_direction = (enemy_y < player_y) - (enemy_y > player_y)
            x_direction = (enemy_x < player_x) - (enemy_x > player_x)

            # Check if the cooldown period has passed
            current_time = time.time()
            if current_time - self.enemy_last_move_time >= self.enemy.cooldown:
                # Update the enemy's position
                enemy_y += y_direction
                enemy_x += x_direction
                self.enemy.position = (enemy_y, enemy_x)

                # Update the last move time
                self.enemy_last_move_time = current_time

                # Check if the enemy is adjacent to the player
                if abs(enemy_y - player_y) + abs(enemy_x - player_x) == 1:
                    self.encounter()
    
    def encounter(self):
        pass
################################################################################# Enemy END
    def select_level(self):
        # Read levels.txt
        with open(self.level_path, 'r') as file:
            lines = file.readlines()
        # Get x,y of level
        section_row, section_col = self.current_level_index
        # Level row select
        start_row = section_row * self.level_height
        end_row = start_row + self.level_height
        # Level col select
        start_col = section_col * self.level_width
        end_col = start_col + self.level_width

        # Load new level data
        level_data = []
        for i in range(start_row, end_row):
            if start_col < len(lines[i]):
                row_data = lines[i][start_col:end_col].strip()
                level_data.append(row_data)

        self.current_level = level_data         # convert level to list of lists of chars here?

    def next_level(self, next_level_index):

        # Tuple addition 
        new_level_index = (self.current_level_index[0] + next_level_index[0], self.current_level_index[1] + next_level_index[1])

        self.current_level_index = new_level_index
        wall_thk = 3
        index_offset = 1
        # NESW
        if next_level_index == (-1, 0):
            self.player.position = (abs(self.player.position[0] + self.level_height) - wall_thk, self.player.position[1])
        elif next_level_index == (0, 1):
            self.player.position = (self.player.position[0], abs(self.player.position[1] - self.level_width) - index_offset)
        elif next_level_index == (1,0):
            self.player.position = (abs(self.player.position[0] - self.level_height) - index_offset, self.player.position[1])
        elif next_level_index == (0,-1):
            self.player.position = (self.player.position[0], abs(self.player.position[0] - self.level_width) + wall_thk)

        self.select_level()

    def print_level(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        for y_index, row in enumerate(self.current_level):
            for x_index, cell in enumerate(row):
                if (y_index, x_index) == self.player.position:
                    print(self.player.symbol, end=' ')
                elif (y_index, x_index) == self.enemy.position:
                    print(self.enemy.symbol, end=' ')
                else:
                    print(cell, end=' ')
            print()

    def print_title(self, title_width):
        # ^{size} centers the text within a field of a specified width, where size is the width
        
        print("#" * title_width)
        print("#" + " " * (title_width-2) + "#")
        print("#" + f"{'Game!':^{title_width-2}}#")
        print("#" + " " * (title_width-2) + "#")
        print("#" + f"{'Press ENTER to start':^{title_width-2}}#")
        print("#" + " " * (title_width-2) + "#")
        print("#" * (title_width))
    
    
    def print_player_pos(self):
        print(f"Player position: {self.player.position}")


    ####################################
    ############# Generate #############
    ####################################

    # Generates a random level
    def generate_level():
        SIZE = 20
        # Example usage
        CHARS = ['M', ' ', 'T']
        PROBABILITIES = [0.4, 0.02, 0]
        
        generated_level = wg.WorldGenerator(SIZE, CHARS, PROBABILITIES)
        generated_level.cluster_mountains()
        generated_level.remove_strays()
        
        board = generated_level.return_self()

        player_start_position = (8,8)

        return board, player_start_position
