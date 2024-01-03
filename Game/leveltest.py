# Define the level layout with walls, mountains, trees, and rivers
level_layout = [
    "####################",
    "#MMMMMMMMMMMMMMMMMM#",
    "#MMMMMMMMMMMMMMMMMM#",
    "#MMMMMMMMMMMMMMMMMM#",
    "#MMMMMMMMMMMMMMMMMM#",
    "#MMMMMMMMMMMMMMMMMM#",
    "#MMMMMMMMMMMMMMMMMM#",
    "#MMMMMMMMMMMMMMMMMM#",
    "#MMMMMMMMMMMMMMMMMM#",
    "#MMMMMMMMMMMMMMMMMM#",
    "#MMMMMMMMMMMMMMMMMM#",
    "#MMMMMMMMMMMMMMMMMM#",
    "#MMMMMMMMMMMMMMMMMM#",
    "#RRRRRRRRRRRRRRRRRRR#",
    "#TTTTTTTTTTTTTTTTTTT#",
    "####################",
]

# Convert the level layout to a list of lists of characters
board = [list(row) for row in level_layout]

# Print the initial level
for row in board:
    print(''.join(row))