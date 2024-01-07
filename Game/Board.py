# Python libraries
import os
import sys
import time
# Custom classes
import Items
import Player
import WorldGenerator as wg

''' TODO:
- Would like to eventually be able to traverse a 10x10 world of 20x20 levels
'''

###################################################
SIZE = 20 # screen size (20x20)
player_start_position = (0,0)
global traversable
traversable = [' ', '[']

bordered_level = [
        "#"*SIZE,
        "#"+ f"{' ':^{SIZE-2}}" + "#",
        "#"+ f"{' ':^{SIZE-2}}" + "#",
        "#"+ f"{' ':^{SIZE-2}}" + "#",
        "#"+ f"{' ':^{SIZE-2}}" + "#",
        "#"+ f"{' ':^{SIZE-2}}" + "#",
        "#"+ f"{' ':^{SIZE-2}}" + "#",
        "#"+ f"{' ':^{SIZE-2}}" + "#",
        "#"+ f"{' ':^{SIZE-2}}" + "#",
        "#"+ f"{' ':^{SIZE-2}}" + "#",
        "#"+ f"{' ':^{SIZE-2}}" + "#",
        "#"+ f"{' ':^{SIZE-2}}" + "#",
        "#"+ f"{' ':^{SIZE-2}}" + "#",
        "#"+ f"{' ':^{SIZE-2}}" + "#",
        "#"+ f"{' ':^{SIZE-2}}" + "#",
        "#"+ f"{' ':^{SIZE-2}}" + "#",
        "#"+ f"{' ':^{SIZE-2}}" + "#",
        "#"+ f"{' ':^{SIZE-2}}" + "#",
        "#"+ f"{' ':^{SIZE-2}}" + "#",
        "#"+ f"{' ':^{SIZE-2}}" + "#",
        "#"*SIZE
]
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


def print_level(level, player_player_pos=None, player_char='.'):
    os.system('cls' if os.name == 'nt' else 'clear')
    for y_index, row in enumerate(level):
        for x_index, cell in enumerate(row):
            if (y_index, x_index) == player_player_pos:
                print(player_char, end=' ')
            else:
                print(cell, end=' ')
        print()


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
        "#MMMM              [",
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
    player_start_position = (7,10)

    return level, player_start_position

def print_title(titlesize):
    # ^{size} centers the text within a field of a specified width, where size is the width
    
    #size = os.get_terminal_size().columns
    
    print("#" * titlesize)
    print("#" + " " * (titlesize-2) + "#")
    print("#" + f"{'Game!':^{titlesize-2}}#")
    print("#" + " " * (titlesize-2) + "#")
    print("#" + f"{'Press any key to start':^{titlesize-2}}#")
    print("#" + " " * (titlesize-2) + "#")
    print("#" * (titlesize))