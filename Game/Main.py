import os
import pygame
from pygame.locals import QUIT, KEYDOWN, K_ESCAPE
from Player import Controller
from LevelManager import *
from Debug import Debug

# TODO
# Player 
#   - animation tied to speed
#   - might not be taking player size into consideration in some places for the offsets
# World
#   - open world, but generate scene based on position?

os.environ['SDL_VIDEO_WINDOW_POS'] = "900,100"  # where window is located
# Pygame init
pygame.init()

# Screen init
screen_width = screen_height = 300
pygame.display.set_mode((screen_width, screen_height),pygame.SCALED)
pygame.display.set_caption("Pygame")
screen = pygame.display.get_surface()
################### Level Manager ###################
# Generate world
world_width = 600   # width of: rows in a scene, scenelists in a world
world_height = 600  # number of: rows in a scene, scenelists in a world
tile_count = 100
tile_folder = "output_tiles"
world = World(world_width, world_height)
world.generate_scene(0,0)
scene = world.get_scene(0,0)
mapper = TileMapper(tile_folder, tile_count, scene)
tile_images = mapper.get_tile_images_list()
tile_size = mapper.get_tile_size()
mapper.add_char_to_dict(' ', 80)
mapper.add_char_to_dict('T', 15)
mapper.add_char_to_dict('M', 16)
mapper.map_chars_to_tiles()

tilemap_data = mapper.get_tilemap()

field = pygame.Surface((world_width, world_height))

mapper.draw_tiles(tilemap_data, tile_size, tile_images, field)

################ End Level Manager ##################

#Setup character 
player_start_pos = (world_width/2,world_height/2) ; player_speed = 1
player_images =[pygame.image.load(f"character-slices/tile_{i}.png") for i in range(0,8)]
player = Controller(player_images, player_start_pos, player_speed, world_width, world_height)
# Game loop vars
clock = pygame.time.Clock()
playing = True
white = (255,255,255)
black = (0,0,0)


previousFrameTicks = 0
currentFrameTicks = 0
deltaTime = 0
half_screen_width = screen_width/2
half_screen_height = screen_height/2
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
    #screen.fill(black)
    
    #create a temp map to draw the character on so the map isnt ruined
    temp = pygame.Surface((world_width, world_height))
    temp.blit(field,(0,0)) 
    player.draw(temp, deltaTime)

    x,y = player.world_position

    ################ DEBUG STUFF #################
    Debug.print(temp, player.world_position, y-10, x)
    Debug.debug_playerRect(x,y,tile_size, temp)
    Debug.debug_screenRect(half_screen_width, half_screen_height, screen_width, screen_height, temp)
    ################################################

    # Calculate the Viewport positon "Camera" That follows the player around
    xoffset = half_screen_width
    yoffset = half_screen_height
    
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
