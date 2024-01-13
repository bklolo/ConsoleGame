import pygame
from pygame.locals import QUIT, KEYDOWN, K_ESCAPE
import tools.WorldGenerator as wg

# Pygame init
pygame.init()

# Screen init
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pygame")

# Generate world
SIZE = 16 * 4 # multiple of tile width
CHARS = ['M', ' ', 'T']
PROBABILITIES = [0.06, 0.02, 0.2,3]
world_generator = wg.WorldGenerator(SIZE, CHARS, PROBABILITIES)
world_generator.cluster_characters('M') # cluster three times (can use other funcs for more customization)
world_generator.cluster_characters('T')
world_generator.cluster_characters(' ')
# Remove strays
world_generator.remove_strays()
# Cluster the neighboring cells around desired point
world_generator.cluster_plants(SIZE//2,SIZE//2)
# The generated world list, as it is
world = world_generator.world

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
tilemap_data = [
    [char_to_tile[char] for char in row] for row in world
]

# Get the number of tiles in each row and column
num_cols = len(tilemap_data[0])  # width
num_rows = len(tilemap_data)     # height

# Frame rate
clock = pygame.time.Clock()

white = (255,255,255)
black = (0,0,0)

# Game loop
playing = True
while playing:
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            playing = False

    # Update game logic here

    # Clear the screen
    screen.fill(black)

    # Draw tiles on the screen based on tilemap_data
    for row_index, row in enumerate(tilemap_data):
        for col_index, tile_index in enumerate(row):
            # Get the tile image corresponding to the tile index
            tile = tile_images[tile_index]
            # Calculate where to draw the tile
            x = col_index * tile_size
            y = row_index * tile_size
            # Blit(draw) the tile onto the screen
            screen.blit(tile, (x, y))

    # Update the surface/display (OpenGL support?)
    pygame.display.flip()

    # Define framerate
    clock.tick(60)

# Quit Pygame (don't need sys.exit()?)
pygame.quit()
