import board

# Control player movement
def move(direction, level=board.current_level, current_position=board.current_pos):
    row, col = current_position
    new_row, new_col = row, col
    y_pos = len(board.current_level)
    x_pos = len(board.current_level)

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

# Check for chars in player direction
def char_check(level, current_position, direction):
    row, col = current_position
    N = level[row - 1][col]
    E = level[row][col + 1]
    S = level[row + 1][col]
    W = level[row][col - 1]
    
    # TODO
    if N == '=' and direction == 'w':
        # board.next_level(board_x, board_y-1)
        pass
    if E == '[' and direction == 'd':
        board.increment_col()
        pass
    if S == '=' and direction == 's':
        pass
    if W == ']' and direction == 'a':
        pass

    return N, E, S, W


