# PlayerController.py

class PlayerController:
    def __init__(self, board_instance):
        self.board_instance = board_instance

    def move(self, direction):
        # Current player position
        y_pos, x_pos = self.board_instance.player.position
        new_y, new_x = y_pos, x_pos                   
        # Current level
        level = self.board_instance.current_level     
        level = [list(row) for row in level]          
        # Define level bounds
        row_max = self.board_instance.level_height
        col_max = self.board_instance.level_width

        # TODO: Visual feedback for hitting a wall

        # Perform character check in each direction
        N, E, S, W = self.char_check(level, y_pos, x_pos)
        # Check NESW for Transport chars. If so, next_level()
        transport = self.check_transport(N,E,S,W,direction)
        # Update character positoin
        new_y, new_x = self.board_instance.player.position
        if not transport:
            if direction == 'w' and y_pos > 1 and N in self.board_instance.traversable:
                new_y = y_pos - 1
            elif direction == 'a' and x_pos > 1 and W in self.board_instance.traversable:
                new_x = x_pos - 1
            elif direction == 's' and y_pos < row_max - 2 and S in self.board_instance.traversable:
                new_y = y_pos + 1
            elif direction == 'd' and x_pos < col_max - 2 and E in self.board_instance.traversable:
                new_x = x_pos + 1
            
        self.board_instance.player.position = new_y, new_x

    # Get the surrounding chars in NESW directions
    def char_check(self, level, y_pos, x_pos):
        row, col = y_pos, x_pos
        N = level[row - 1][col]
        E = level[row][col + 1]
        S = level[row + 1][col]
        W = level[row][col - 1]

        # Return chars in each direction
        return N, E, S, W

    def check_transport(self, N, E, S, W, direction):
        # Check chars in NESW for door/gate/etc chars; if walking in that dir, next level
        travel_north = (-1,0)
        travel_east = (0,1)
        travel_south = (1,0)
        travel_west = (0,-1)
        transport = False
        if N == '=' and direction == 'w':
            transport = True
            self.board_instance.next_level(travel_north)
        if E == '[' and direction == 'd':
        # Pass the xy to the board for tuple summation
            transport = True
            self.board_instance.next_level(travel_east)
        if S == '=' and direction == 's':
            transport = True
            self.board_instance.next_level(travel_south)
        if W == ']' and direction == 'a':
            transport = True
            self.board_instance.next_level(travel_west)
        return transport