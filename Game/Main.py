import pygame
from pygame.locals import QUIT, KEYDOWN, K_ESCAPE
from Player import Controller
from LevelManager import *

previousFrameTicks = 0
currentFrameTicks = 0
deltaTime = 0

# Pygame init
pygame.init()

# Screen init
screen_width = 720
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height),pygame.RESIZABLE)
pygame.display.set_caption("Pygame")

# Generate world
world = World(screen_width, screen_height)
world.generate_scene(0,0)
scene = world.get_scene(0,0)

# Tilemapper
#######################################################
mapper = TileMapper("output_tiles", 100, scene)
tile_images = mapper.get_tile_images_list()
tile_size = mapper.get_tile_size()

# Add a new character mapping
mapper.add_char_to_dict(' ', 80)
mapper.add_char_to_dict('T', 15)
mapper.add_char_to_dict('M', 16)

# grab individual tiles
mapper.map_chars_to_tiles()
tilemap_data = mapper.get_tilemap()
########################################################

#Setup character 
player_images =[pygame.image.load(f"character-slices/tile_{i}.png") for i in range(0,8)]
player = Controller(player_images,(0,0), 10)

# Frame rated
clock = pygame.time.Clock()

white = (255,255,255)
black = (0,0,0)

# Game loop
playing = True
while playing:
    #populating delta time
    currentFrameTicks = pygame.time.get_ticks()
    deltaTime = currentFrameTicks - previousFrameTicks
    previousFrameTicks = currentFrameTicks 
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
 
    player.update()
    player.draw(screen, deltaTime)

    # Update the surface/display (OpenGL support?)
    pygame.display.flip()

    # Define framerate
    clock.tick(60)

# Quit Pygame (don't need sys.exit()?)
pygame.quit()
