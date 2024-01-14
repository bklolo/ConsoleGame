import random

'''Can test script at bottom of script'''


class SceneGenerator:
    global CHARS
    global PROBABILITIES
    CHARS = ['M', ' ', 'T']
    PROBABILITIES = [0.06, 0.02, 0.2,3]

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.scene = self.generate_scene()

    def generate_scene(self):
        return [
            [self.generate_tile() for x in range(self.width)] for y in range(self.height)]


    def generate_tile(self):
        global PROBABILITIES
        global CHARS
        return random.choice(CHARS) if random.random() < random.choice(PROBABILITIES) else ' '


    # Clustering algo
    def cluster_characters(self, thing):
        for i in range(self.height):
            for j in range(self.width):
                if self.scene[i][j] == thing and random.random() < 0.1:  # Adjust the probability as needed
                    self.cluster_neighbors(i, j, thing)


    # Check 3x3 around cell for M
    def cluster_neighbors(self, i, j, thing):
        for x in range(i-1, i+1):
            for y in range(j-1, j+1):
                if 0 <= x < self.width and 0 <= y < self.height and self.scene[x][y] == ' ':
                    self.scene[x][y] = thing


    # Removes most stray characters in each row
    def remove_strays(self):
        for y, row in enumerate(self.scene):
            for x, char in enumerate(row):
                if x - 1 >= 0 and x + 1 < self.width:
                    if row[x - 1] == ' ' and row[x + 1] == ' ':
                        row[x] = ' '


    # Return the list
    def return_self(self):
        return self.scene


    # Clustering algorithm that makes chars extra scarce (maybe good for flora/fauna spawning)
    def cluster_plants(self, i, j):
            count_m = self.cull(i, j, 'M')
            count_t = self.cull(i, j, 'T')
            count_sp = self.cull(i, j, ' ')

            if count_m > count_t and count_m > count_sp:
                self.cluster_neighbors('M')
            elif count_t > count_sp:
                self.cluster_neighbors('T')
            else:
                self.cluster_neighbors(' ')

    def cull(self, i, j, count_char):
        count_x = sum(1 for x in range(i - 1, i + 1) for y in range(j - 1, j + 1)
                        if (0 <= x < self.width) and (0 <= y < self.height) and (self.scene[x][y] == count_char))
        
        return count_x
    
    def print_world(self, str):
        print(f"{str}\n")
        for row in self.scene:
            print(' '.join(row))


    def save_world_to_file(self, filename='generated_world.txt'):
        with open(filename, 'w') as file:
            for i, row in enumerate(self.scene):
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
width = 60
height = 30

world_generator = SceneGenerator(width, height)
world_generator.cluster_characters('M') # cluster three times (can use other funcs for more customization)
world_generator.cluster_characters('T')
world_generator.cluster_characters(' ')
## First print
world_generator.print_world("First print")

# Cluster mountains
world_generator.cluster_characters('M')
world_generator.cluster_characters('M')
world_generator.print_world("Cluster mountains")

# Cluster mountains
world_generator.cluster_characters('T')
world_generator.print_world("Cluster trees")

# Remove non-cluster characters
world_generator.remove_strays()
world_generator.print_world("Remove strays")

# Cluster plants
#world_generator.cluster_plants(4,6)
world_generator.print_world("Cluster plants")
#world_generator.print_world()
#world_generator.save_world_to_file()
'''