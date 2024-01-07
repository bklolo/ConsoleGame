import board

def move(level, current_position, direction):
    row, col = current_position
    new_row, new_col = row, col
    y_pos = len(level)
    x_pos = len(level[0])

    # TODO: visual feedback so player knows when a wall is hit

    # perform character check in each direction?
    N, E, S, W = char_check(level, current_position, direction)

    if direction == 'w':
        if row > 1 and N in board.traversable:
            new_row -= 1
        else:
            pass
    elif direction == 'a' and W in board.traversable:
        if col > 1:
            new_col -= 1
        else:
            pass
    elif direction == 's' and S in board.traversable:
        if row < y_pos - 2:
            new_row += 1
        else:
            pass
    elif direction == 'd' and E in board.traversable:
        if col < x_pos - 2:
            new_col += 1
        else:
            pass

    return new_row, new_col


def char_check(level, current_position, direction):
    row, col = current_position
    N = level[row - 1][col]
    E = level[row][col + 1]
    S = level[row + 1][col]
    W = level[row][col - 1]
    
    # TODO
    # if NESW == '[' and direction == WASD:
    #   load_scene()
    #if E == '[' and direction == 'd':
        # board.nextLevel()

    return N, E, S, W


