# Python libraries
import os   
import sys
import time
# Custom classes
import Items
import Player
import WorldGenerator as wg


class Board:
    def __init__(self, level_path, level_width, level_height, initial_position):
        self.player_char = '.'
        self.level_path = level_path
        self.level_width = level_width
        self.level_height = level_height
        self.current_level = []
        self.current_pos = initial_position
        self.current_level_index = (0, 0)
        self.traversable = [' ', '[']
        self.ports = ['[', ']', '=']

        self.select_level()

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

        self.current_level = level_data

        # Your existing select_level logic here

    def next_level(self, next_level_index):

        # Tuple addition using unpacking
        current_level_index = (self.current_level_index[0] + next_level_index[0], self.current_level_index[1] + next_level_index[1])

        # TODO: set player position
        if current_level_index == (0, 0):
            pass
        elif current_level_index == (0, 1):
            self.current_pos = (self.current_pos[0], abs(self.current_pos[1] - self.level_width))

        self.select_level()
        # Your existing next_level logic here

    def print_level(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        for y_index, row in enumerate(self.current_level):
            for x_index, cell in enumerate(row):
                if (y_index, x_index) == self.current_pos:
                    print(self.player_char, end=' ')
                else:
                    print(cell, end=' ')
            print()        # Your existing print_level logic here

    def print_title(self, titlesize):
        # ^{size} centers the text within a field of a specified width, where size is the width
        
        print("#" * titlesize)
        print("#" + " " * (titlesize-2) + "#")
        print("#" + f"{'Game!':^{titlesize-2}}#")
        print("#" + " " * (titlesize-2) + "#")
        print("#" + f"{'Press ENTER to start':^{titlesize-2}}#")
        print("#" + " " * (titlesize-2) + "#")
        print("#" * (titlesize))
    
    
    def print_player_pos(self):
        # Your existing print_player_pos logic heredef print_player_pos():
        print(f"Player position: {self.current_pos}")


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
