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
screen_width = 360
screen_height = 240
screen = pygame.display.set_mode((screen_width, screen_height),pygame.SCALED)
pygame.display.set_caption("Pygame")

################### Level Manager ###################
# Generate world
world_width = 1080
world_height = 720
world = World(world_width, world_height)
world.generate_scene(0,0)
scene = world.get_scene(0,0)
mapper = TileMapper("output_tiles", 100, scene)
tile_images = mapper.get_tile_images_list()
tile_size = mapper.get_tile_size()
mapper.add_char_to_dict(' ', 80)
mapper.add_char_to_dict('T', 15)
mapper.add_char_to_dict('M', 16)
mapper.map_chars_to_tiles()
tilemap_data = mapper.get_tilemap()

field = pygame.Surface((world_width, world_height)) 

#Draw tiles on a surface based on tilemap_data
for row_index, row in enumerate(tilemap_data):
    for col_index, tile_index in enumerate(row):
        # Get the tile image corresponding to the tile index
        tile = tile_images[tile_index]
        # Calculate where to draw the tile
        x = col_index * tile_size
        y = row_index * tile_size
        # Blit(draw) the tile onto the surface
        field.blit(tile, (x, y))
################ End Level Manager ##################

#Setup character 
player_images =[pygame.image.load(f"character-slices/tile_{i}.png") for i in range(0,8)]
player = Controller(player_images,(0,0), 1, world_width, world_height)

# Game loop vars
clock = pygame.time.Clock()
playing = True
white = (255,255,255)
black = (0,0,0)

################ Game Loop ##################
while playing:
    #populating delta time
    currentFrameTicks = pygame.time.get_ticks()
    deltaTime = currentFrameTicks - previousFrameTicks
    previousFrameTicks = currentFrameTicks 
    
    ##############UPDATE##############################
    player.update()
    ##################################################

    ##############DRAW################################
    # Clear the screen
    screen.fill(black)
    
    #create a temp map to draw the character on so the map isnt ruined
    temp = pygame.Surface((world_width, world_height))
    temp.blit(field,(0,0)) 
    player.draw(temp, deltaTime)

    # Calculate the Viewport positon "Camera" That follows the player around
    xoffset = screen_width/2 
    yoffset = screen_height/2 
    x,y = player.world_position
    
    if x < xoffset:
        x = 0
    elif x > world_width - xoffset:
        x = world_width - screen_width
    else:
        x -= xoffset

    if y < yoffset:
        y = 0
    elif y > world_height - yoffset:
        y = world_height -screen_height
    else:
        y -= yoffset
   
    screen.blit(temp,(-x ,-y))

    # Update the surface/display (OpenGL support?)
    pygame.display.flip()
    ##################################################
    
    # Define framerate
    clock.tick(60)

# Quit Pygame (don't need sys.exit()?)
pygame.quit()