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
            count_m = self.cull(i, j, 'M')

            count_t = self.cull(i, j, 'T')

            count_sp = self.cull(i, j, ' ')

            if count_m > count_t and count_m > count_sp:
                self.world[i][j] = 'M'
            elif count_t > count_sp:
                self.world[i][j] = 'T'
            else:
                self.world[i][j] = ' '

    def cull(self, i, j, count_char):
        count_x = sum(1 for x in range(i - 1, i + 2) for y in range(j - 1, j + 2)
                        if (0 <= x < self.size) and (0 <= y < self.size) and (self.world[x][y] == count_char))
        return count_x
    
    def print_world(self):
        for i, row in enumerate(self.world):
            if i % 20 == 0:
                print("#" * (self.size + 6))
                if i != 0:
                    print("#" * (self.size + 6))
            print("#" + ''.join(row)[:20] + "##" + ''.join(row)[20:40] + "##" + ''.join(row)[40:60] + "#")
        if (self.size % 20 == 0):
            print("#" * (self.size + 6))
        else:
            print("#" * (20 + 6))

    def save_world_to_file(self, filename='generated_world.txt'):
        with open(filename, 'w') as file:
            for i, row in enumerate(self.world):
                if i % 20 == 0:
                    file.write("#" * (self.size + 6)+ '\n')
                    if i != 0:
                        file.write("#" * (self.size + 6) + '\n')
                file.write("#" + ''.join(row)[:20] + "##" + ''.join(row)[20:40] + "##" + ''.join(row)[40:60] + "#" + '\n')
            if (self.size % 20 == 0):
                file.write("#" * (self.size + 6) + '\n')
            else:
                file.write("#" * (20 + 6) + '\n')
'''
### Example usage ###
# Prints level after each algorithm
SIZE = 60
CHARS = ['M', ' ', 'T']
PROBABILITIES = [0.6, 0.02, 0]

world_generator = WorldGenerator(SIZE, CHARS, PROBABILITIES)

# First print
#world_generator.print_world()

# Cluster mountains
world_generator.cluster_characters('M')
world_generator.cluster_characters('M')
world_generator.cluster_characters('M')
#print("\n\nWorld with Clustered M:\n\n")
#world_generator.print_world()

# Cluster mountains
world_generator.cluster_characters('T')
#print("\nWorld with Clustered T:")
#world_generator.print_world()

# Remove non-cluster characters
world_generator.remove_strays()
#print("\n\nWorld with remove_strays:\n\n")
#world_generator.print_world()
#world_generator.print_world()
world_generator.save_world_to_file()
'''