import random

'''See example usage at bottom of script'''

class WorldGenerator:
    def __init__(self, size, chars, probabilities):
        self.size = size
        self.chars = chars
        self.probabilities = probabilities
        self.world = self.generate_world()


    def generate_world(self):
        return [[self.generate_tile() for _ in range(self.size)] for _ in range(self.size)]


    def generate_tile(self):
        return random.choice(self.chars) if random.random() < random.choice(self.probabilities) else ' '


    # Clustering algo
    def cluster_characters(self, thing):
        for i in range(self.size):
            for j in range(self.size):
                if self.world[i][j] == thing and random.random() < 0.1:  # Adjust the probability as needed
                    self.cluster_neighbors(i, j, thing)


    # Check 3x3 around cell for M
    def cluster_neighbors(self, i, j, thing):
        for x in range(i-1, i+2):
            for y in range(j-1, j+2):
                if 0 <= x < self.size and 0 <= y < self.size and self.world[x][y] == ' ':
                    self.world[x][y] = thing


    # Removes most stray characters in each row
    def remove_strays(self):
        for y, row in enumerate(self.world):
            for x, char in enumerate(row):
                if x - 1 >= 0 and x + 1 < self.size:
                    if row[x - 1] == ' ' and row[x + 1] == ' ':
                        row[x] = ' '


    # Return the list
    def return_self(self):
        return self.world


    # Clustering algorithm that makes chars extra scarce (maybe good for flora/fauna spawning)
    def cluster_plants(self, i, j):
            count_m = sum(1 for x in range(i - 1, i + 2) for y in range(j - 1, j + 2)
                        if (0 <= x < self.size) and (0 <= y < self.size) and (self.world[x][y] == 'M'))

            count_t = sum(1 for x in range(i - 1, i + 2) for y in range(j - 1, j + 2)
                        if (0 <= x < self.size) and (0 <= y < self.size) and (self.world[x][y] == 'T'))

            count_sp = sum(1 for x in range(i - 1, i + 2) for y in range(j - 1, j + 2)
                        if (0 <= x < self.size) and (0 <= y < self.size) and (self.world[x][y] == ' '))

            if count_m > count_t and count_m > count_sp:
                self.world[i][j] = 'M'
            elif count_t > count_sp:
                self.world[i][j] = 'T'
            else:
                self.world[i][j] = ' '


    # Print for debugging
    def print_world(self):
        for row in self.world:
            print(''.join(row))

'''
### Example usage ###
# Prints level after each algorithm
SIZE = 100
CHARS = ['M', ' ', 'T']
PROBABILITIES = [0.6, 0.02, 0]

world_generator = WorldGenerator(SIZE, CHARS, PROBABILITIES)
world_generator.print_world()

# Cluster mountains
world_generator.cluster_characters('M')
print("\nWorld with Clustered M:")
world_generator.print_world()

# Cluster mountains
#world_generator.cluster_characters('T')
#print("\nWorld with Clustered T:")
#world_generator.print_world()

# Remove non-cluster characters
#world_generator.remove_strays()
#print("\nWorld with remove_strays:")
#world_generator.print_world()
'''