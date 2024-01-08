# PlayerController.py

from Board import Board

class PlayerController:
    def __init__(self, board_instance):
        self.board_instance = board_instance

    def move(self, direction):
        # Current player position
        y_pos, x_pos = self.board_instance.current_pos
        new_y, new_x = y_pos, x_pos                   
        # Current level
        level = self.board_instance.current_level     
        level = [list(row) for row in level]          
        # Define level bounds
        row_max = self.board_instance.level_height
        col_max = self.board_instance.level_width

        # TODO: Visual feedback for hitting a wall

        # Perform character check in each direction
        N, E, S, W = self.char_check(level, y_pos, x_pos, direction)
        # Check NESW for Transport chars. If so, next_level()
        transport = self.check_transport(N,E,S,W,direction)
        # Update character positoin
        new_y, new_x = self.board_instance.current_pos
        if not transport:
            if direction == 'w' and y_pos > 1 and N in self.board_instance.traversable:
                new_y = y_pos - 1
            elif direction == 'a' and x_pos > 1 and W in self.board_instance.traversable:
                new_x = x_pos - 1
            elif direction == 's' and y_pos < row_max - 2 and S in self.board_instance.traversable:
                new_y = y_pos + 1
            elif direction == 'd' and x_pos < col_max - 2 and E in self.board_instance.traversable:
                new_x = x_pos + 1
            
        self.board_instance.current_pos = new_y, new_x

    # Get the surrounding chars in NESW directions
    def char_check(self, level, y_pos, x_pos, direction):
        row, col = y_pos, x_pos
        N = level[row - 1][col]
        E = level[row][col + 1]
        S = level[row + 1][col]
        W = level[row][col - 1]

        # Return chars in each direction
        return N, E, S, W

    def check_transport(self, N, E, S, W, direction):
        # Check chars in NESW for door/gate/etc chars; if walking in that dir, next level
        transport = False
        if N == '=' and direction == 'w':
            pass
        if E == '[' and direction == 'd':
        # Pass the xy to the board for tuple summation
            transport = True
            self.board_instance.next_level((0, 1))
        if S == '=' and direction == 's':
            pass
        if W == ']' and direction == 'a':
            pass
        return transport