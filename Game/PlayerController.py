# PlayerController.py

from Board import Board

class PlayerController:
    def __init__(self, board_instance):
        self.board_instance = board_instance

    def move(self, direction):
        # current position on the board
        current_position = self.board_instance.current_pos
        # grab xy of current position
        y_pos, x_pos = current_position
        # placeholders for new position
        new_y, new_x = y_pos, x_pos
        level = self.board_instance.current_level
        level = [list(row) for row in level]
        # define level params
        row_max = self.board_instance.level_height
        col_max = self.board_instance.level_width

        # TODO: Visual feedback for hitting a wall

        # Perform character check in each direction
        N, E, S, W = self.char_check(level, self.board_instance.current_pos, direction)

        if direction == 'w' and y_pos > 1 and N in self.board_instance.traversable:
            new_y = y_pos - 1
        elif direction == 'a' and x_pos > 1 and W in self.board_instance.traversable:
            new_x = x_pos - 1
        elif direction == 's' and y_pos < row_max - 2 and S in self.board_instance.traversable:
            new_y = y_pos + 1
        elif direction == 'd' and x_pos < col_max - 2 and E in self.board_instance.traversable:
            new_x = x_pos + 1
        self.board_instance.current_pos = new_y, new_x

    def char_check(self, level, current_position, direction):
        row, col = current_position
        N = level[row - 1][col]
        E = level[row][col + 1]
        S = level[row + 1][col]
        W = level[row][col - 1]

        # TODO
        if N == '=' and direction == 'w':
            # self.board_instance.next_level(board_x, board_y-1)
            pass
        if E == '[' and direction == 'd':
            self.board_instance.next_level((0, 1))
            pass
        if S == '=' and direction == 's':
            pass
        if W == ']' and direction == 'a':
            pass

        return N, E, S, W
