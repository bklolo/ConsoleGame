import pygame
import random
# Represents each scene in the World
class Scene:
    def __init__(self):
        self.contents = []

class World:
    """The World class houses all scenes, static and generated"""
    def __init__(self, width, length):
        self.width = width      # width of World grid
        self.length = length    # length of World grid
        self.world = [[Scene() for _ in range(width)] for _ in range(length)]   # Generate [[scene_1],[scene_2],...,[scene_N]]
    
    # Return a list of the world, as it is
    def get_world(self):
        return [[scene.contents for scene in row] for row in self.world]

    def get_scene(self, x, y):
        """Return the contents of a scene, else None"""
        if 0 <= x < self.width and 0 <= y < self.length:
            return self.world[y][x].contents
        else:
            return None

    # Add the contents of a scene to the world
    def add_scene_contents(self, x, y, contents):
        if 0 <= x < self.width and 0 <= y < self.length:
            self.world[y][x].contents.extend(contents)

    def generate_scene(self, x, y):
        generator = SceneGenerator(self.width, self.length)
        new_contents = generator.generate_scene()
        self.add_scene_contents(x, y, new_contents)

class SceneGenerator:
    global CHARS ; global PROBABILITIES
    CHARS = ['M', ' ', 'T']
    PROBABILITIES = [0.06, 0.02, 0.2,3]

    def __init__(self, width, height):
        self.width = width ; self.height = height
        self.scene = self.generate_scene()

    def generate_scene(self):
        return [
            [self.generate_tile() for x in range(self.width)] for y in range(self.height)]

    def generate_tile(self):
        global PROBABILITIES ; global CHARS
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
            count_m = self.surrounding_char_count(i, j, 'M')
            count_t = self.surrounding_char_count(i, j, 'T')
            count_sp = self.surrounding_char_count(i, j, ' ')
            # if M is max
            if count_m > count_t and count_m > count_sp:
                self.cluster_neighbors('M')
            # if T is max
            elif count_t > count_sp:
                self.cluster_neighbors('T')
            # else ' ' is max
            else:
                self.cluster_neighbors(' ')

    def surrounding_char_count(self, i, j, count_char):
        """for each surrounding cell (3x3), if in bounds, add to that chars count"""
        count_x = sum(1 for x in range(i - 1, i + 1) for y in range(j - 1, j + 1)
                        if (0 <= x < self.width) and (0 <= y < self.height) 
                        and (self.scene[x][y] == count_char))
        
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

class TileMapper:
    """Map all chars in generated Scene to output_tiles"""
    
    def __init__(self, tile_folder, num_of_tiles, scene) -> None:
        self.folder = tile_folder           # tile location  
        self.num_of_tiles = num_of_tiles    # number of tiles to collect
        self.scene = scene                  # scene to map to
        self.tile_images = []               # list of tiles
        self.tilemap_data = []              # list of char to tile data
        self.dict = { }              
    
    def return_dict(self):
        return self.dict
    
    def add_char_to_dict(self, char, tile_index):
        """Add (char: tile_number) key-value pairs to dictionary"""
        self.dict[char] = tile_index

    def map_chars_to_tiles(self):        
        """Convert chars to tiles (store each tile index for each char within scene)"""
        self.tilemap_data = [[self.dict[char] for char in row] for row in self.scene]

    def get_tilemap(self):
        """Return the list of tile/image indexes"""
        return self.tilemap_data
    
    def get_tile_images_list(self):
        """Create and return the list of image files"""
        self.tile_images = [pygame.image.load(f"{self.folder}/tile_{i}.png") for i in range(0, self.num_of_tiles + 1)]
        return self.tile_images

    def get_tile_size(self):
        return self.tile_images[0].get_width()

# Test mapper
'''
scene = Scene()
scene.contents = [['M','T',' '],['M',' ',' '],[' ','T',' ']]
mapper = TileMapper("output_tiles", 100, scene)
tile_images = mapper.get_tile_images_list()
tile_size = mapper.get_tile_size()

# Add a new character mapping
mapper.add_char_to_dict(' ', tile_images[80])
mapper.add_char_to_dict('T', tile_images[15])
mapper.add_char_to_dict('M', tile_images[16])

# grab individual tiles
mapper.map_chars_to_tiles()
tilemap_data = mapper.get_tilemap()
'''

# Data for testing mapper
''' 
# Load tiles (total of 100)
tile_images = [pygame.image.load(f"output_tiles/tile_{i}.png") for i in range(0, 101)]
tile_size = tile_images[0].get_width() # not sure that all tiles are same width

player_char = tile_images[5]

# Dictionary to map chars to tiles
char_to_tile = {' ': tile_images.index(tile_images[80]), 
                'T': tile_images.index(tile_images[15]), 
                'M': tile_images.index(tile_images[16])
                }

# Convert chars to tiles
tilemap_data = [[char_to_tile[char] for char in row] for row in scene]

'''


'''
# Example usage:
screen_width = 10
screen_height = 5
grid = 4
world = World(3, 3) # world grid
world.generate_scene(0,0)
world.generate_scene(2,2)

start_level = world.get_scene(0,0)
level1 = world.get_scene(2,2)
# Access contents of a scene
print(level1)
print(world.get_world())
'''