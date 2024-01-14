import pygame
from pygame.locals import QUIT, KEYDOWN, K_ESCAPE
import tools.SceneGenerator as SG
from pygame_PlayerController import pygame_PlayerController
import tools.SceneGenerator as SG
import sys
from LevelManager import World

# Pygame init
pygame.init()

# Screen init
screen_width = 1080
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pygame")

# Generate world
###############################################################################################################
SIZE = 16 * 5 # multiple of tile width

#scene_generator = SG.SceneGenerator(screen_width, screen_height, CHARS, PROBABILITIES)
#scene_generator.cluster_characters('M') # cluster three times (can use other funcs for more customization)
#scene_generator.cluster_characters('T')
#scene_generator.cluster_characters(' ')
## Remove strays
#scene_generator.remove_strays()
# Cluster the neighboring cells around desired point
#scene_generator.cluster_plants(SIZE//2,SIZE//2)
###############################################################################################################
# The generated world list, as it isddd

world = World(screen_width, screen_height)
world.generate_scene(0,0)
scene = world.get_scene(0,0)
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
print(world.get_world())
'''

#Setup character 
player_images =[pygame.image.load(f"character-slices/tile_{i}.png") for i in range(0,7)]
p = pygame_PlayerController(player_images,(0,0), 5)

# Load tiles (total of 100)
tile_images = [pygame.image.load(f"output_tiles/tile_{i}.png") for i in range(0, 101)]
tile_size = tile_images[0].get_width() # not sure that all tiles are same width

# Grab desired images from output_tiles/
tree = tile_images[15]
hill = tile_images[16]
field = tile_images[80]

player_char = tile_images[5]

# Dictionary to map chars to tiles
char_to_tile = {' ': tile_images.index(field), 
                'T': tile_images.index(tree), 
                'M': tile_images.index(hill)
                }

# Convert chats to tiles
tilemap_data = [[char_to_tile[char] 
                 for char in row] 
                 for row in scene]

# Get the number of tiles in each row and column
num_cols = len(tilemap_data[0])  # width
num_rows = len(tilemap_data)     # height

# Frame rated
clock = pygame.time.Clock()

white = (255,255,255)
black = (0,0,0)

# Game loop
playing = True
while playing:
    # Update game logic here

    # Clear the screen
    screen.fill(black)

    #Draw tiles on the screen based on tilemap_data
    for row_index, row in enumerate(tilemap_data):
        for col_index, tile_index in enumerate(row):
            # Get the tile image corresponding to the tile index
            tile = tile_images[tile_index]
            # Calculate where to draw the tile
            x = col_index * tile_size
            y = row_index * tile_size
            # Blit(draw) the tile onto the screen
            screen.blit(tile, (x, y))
 
    p.update()
    p.draw(screen)

    # Update the surface/display (OpenGL support?)
    pygame.display.flip()

    # Define framerate
    clock.tick(60)

# Quit Pygame (don't need sys.exit()?)
pygame.quit()
