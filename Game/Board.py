# Python libraries
import os
import sys
import time
# Custom classes
import Items
import Player
import WorldGenerator as wg

'''
Would like to eventually be able to traverse a 10x10 world of 20x20 levels
'''

###################################################
SIZE = 10 # screen size (20x20)
player_start_position = (0,0)
###################################################

# Generates a random level
def generate_level():
    # Example usage
    CHARS = ['M', ' ', 'T']
    PROBABILITIES = [0.4, 0.02, 0]
    
    generated_level = wg.WorldGenerator(SIZE, CHARS, PROBABILITIES)
    generated_level.cluster_mountains()
    generated_level.remove_strays()
    
    board = generated_level.return_self()

    player_start_position = (8,8)

    return board, player_start_position

# A blank field
def Field():
    # original board (player centered among blanks)
    level_layout = [[' ' for _ in range(SIZE)] for _ in range(SIZE)]
    level = [list(row) for row in level_layout]
    player_start_position = (SIZE//2, SIZE//2)
    return level, player_start_position

# Level 1
def Level_1():
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
        "#RRRRRRRRRRRRRRRRRR#",
        "#TTTTTTTTTTTTTTTTTT#",
        "####################",
    ]
    # convert strings to list of chars
    level = [list(row) for row in level_layout]
    SIZE = len(level)
        # define player position
    player_start_position = (SIZE//2, SIZE//2)

    return level, player_start_position

def print_title():
    size = os.get_terminal_size().columns
    print("#" * (size + 4))
    print("#" + " " * (size + 2) + "#")
    print("#" + f"{'Game!':^{size}}#")
    print("#" + " " * (size + 2) + "#")
    print("#" + f"{'Press any key to start':^{size}}#")
    print("#" + " " * (size + 2) + "#")
    print("#" * (size + 4))