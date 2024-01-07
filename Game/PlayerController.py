import board

# Control player movement
def move(direction):
    current_position = board.current_pos
    y_pos, x_pos = current_position
    new_y, new_x = y_pos, x_pos
    # convert strings to list of chars
    level = board.current_level
    level = [list(row) for row in level]
    row_max = len(level)
    col_max = len(level[0])

    # TODO: Visual feedback for hitting a wall

    # Perform character check in each direction
    N, E, S, W = char_check(level, current_position, direction)

    if direction == 'w' and y_pos > 1 and N in board.traversable:
        new_y = y_pos - 1
    elif direction == 'a' and x_pos > 1 and W in board.traversable:
        new_x = x_pos - 1
    elif direction == 's' and y_pos < row_max - 2 and S in board.traversable:
        new_y = y_pos + 1
    elif direction == 'd' and x_pos < col_max - 2 and E in board.traversable:
        new_x = x_pos + 1
    board.current_pos = new_y, new_x

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


