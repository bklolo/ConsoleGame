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
global current_pos
current_pos= (7,10)

# Level vars
level_path = 'Game\\world.txt'
level_width = 20
level_height = 16
current_level = []
current_level_index = (0,0)

# Tile types
global traversable
traversable = [' ', '[']
ports = ['[', ']', '=']

####################################
############## Load ################
####################################

def select_level(current_level_index=(0,0)):
    global current_level
    # Read levels.txt
    with open(level_path, 'r') as file:
        lines = file.readlines()
    # Get x,y of level
    section_row, section_col = current_level_index
    # Level row select
    start_row = section_row * level_height
    end_row = start_row + level_height
    # Level col select
    start_col = section_col * level_width
    end_col = start_col + level_width

    # Load new level data
    level_data = []
    for i in range(start_row, end_row):
        if start_col < len(lines[i]):
            row_data = lines[i][start_col:end_col].strip()
            level_data.append(row_data)

    current_level = level_data


def nextLevel(current_level, next_level):
    # tuple addition
    select_level(current_level + next_level)


####################################
############# Print ################
####################################

def print_level(player_char='.'):
    os.system('cls' if os.name == 'nt' else 'clear')
    for y_index, row in enumerate(current_level):
        for x_index, cell in enumerate(row):
            if (y_index, x_index) == current_pos:
                print(player_char, end=' ')
            else:
                print(cell, end=' ')
        print()


def print_title(titlesize):
    # ^{size} centers the text within a field of a specified width, where size is the width
    
    #size = os.get_terminal_size().columns
    
    print("#" * titlesize)
    print("#" + " " * (titlesize-2) + "#")
    print("#" + f"{'Game!':^{titlesize-2}}#")
    print("#" + " " * (titlesize-2) + "#")
    print("#" + f"{'Press ENTER to start':^{titlesize-2}}#")
    print("#" + " " * (titlesize-2) + "#")
    print("#" * (titlesize))


####################################
############# Generate #############
####################################

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


####################################
############### Misc ###############
####################################

# A blank screen w/ player centered
def Field():
    # original board (player centered among blanks)
    level_layout = [[' ' for _ in range(SIZE)] for _ in range(SIZE)]
    level = [list(row) for row in level_layout]
    player_start_position = (SIZE//2, SIZE//2)
    return level, player_start_position


# Level 1 test
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
        "#MMMMMM        MMMM#",
        "#MMMM            MM#",
        "#TTTT T T T       T#",
        "####################"
    ]


    # convert strings to list of chars
    level = [list(row) for row in level_layout]
    SIZE = len(level)
        # define player position
    player_start_position = (7,10)

    return level, player_start_position


# Level 2 test
def Level_2():
    # static level (string format for ease of editing)
    level_layout = [
        "####################",
        "# T T T T T T T T T T T T T T T T T T #",
        "# T T T T T T T T T T T T T T T T T T #",
        "#                                     #",
        "# T                                   #",
        "]                                     #",
        "# T                                   #",
        "#                                     #",
        "#                                     #",
        "#                                     #",
        "#                                     #",
        "#                                     #",
        "# M M M M M                           #",
        "# M M M M M M    M                    #",
        "# M M M M M M M M M M M M             #",
        "# # # # # # # # # # # # # # # # # # # #",
    ]

    # convert strings to list of chars
    level = [list(row) for row in level_layout]
    SIZE = len(level)
        # define player position
    player_start_position = (5,1)

    return level, player_start_position
    
