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

os.environ['SDL_VIDEO_WINDOW_POS'] = "700,30"  # where window is located
# Pygame init
pygame.init()

################### Screen init #####################
player_size = 16 # 
display_width = player_size * 25
display_height = display_width * 0.75 # screen bounds
pygame.display.set_mode((display_width, display_height),pygame.SCALED)
pygame.display.set_caption("Pygame")
screen = pygame.display.get_surface()

################### Level Manager ###################
# Generate world
tile_count = 100
tile_folder = "output_tiles"
scene_width = scene_height = player_size * 100 # scene bounds
world = World(scene_width, scene_height)
scene = world.get_scene(0,0)
mapper = TileMapper(tile_folder, tile_count, scene)
tile_images = mapper.get_tile_images_list()
tile_size = mapper.get_tile_size()
mapper.add_char_to_dict(' ', 80)
mapper.add_char_to_dict('T', 15)
mapper.add_char_to_dict('M', 16)
mapper.map_chars_to_tiles()

tilemap_data = mapper.get_tilemap()

#field = pygame.Surface((display_width, display_height))   # surface scene is drawn on
field = pygame.Surface((scene_width, scene_height))   # surface scene is drawn on

mapper.draw_tiles(tilemap_data, tile_size, tile_images, field)

################## Setup character ##################
player_start_pos = (field.get_width()/2, field.get_height()/2) ; player_speed = 1.5
player_images =[pygame.image.load(f"character-slices_new/tile_{i}.png") for i in range(0,8)]
player = Controller(player_images, player_start_pos, player_speed, scene_width, scene_height) # display vs scene
#####################################################

# Game loop vars
clock = pygame.time.Clock()
playing = True
white = (255, 255, 255)
black = (0, 0, 0)
previousFrameTicks = 0
currentFrameTicks = 0
deltaTime = 0
half_screen_width = display_width / 2
half_screen_height = display_height / 2
camera_speed = 1.0  # Adjust this value as needed for the desired camera speed

temp = pygame.Surface((field.get_size()))
################ Game Loop ##################
while playing:

    # Populating delta time
    currentFrameTicks = pygame.time.get_ticks()
    deltaTime = currentFrameTicks - previousFrameTicks
    previousFrameTicks = currentFrameTicks

    player.update() # get input, move

    ############## DRAW ################
    temp.blit(field, (0, 0))
    player.draw(temp, deltaTime)
    # screen.blit(temp, (0, 0))  # Blit directly to the screen without camera offset


    player_x, player_y = player.world_position

    ################ DEBUG STUFF #################
    Debug.print(temp, player.world_position, player_y - 10, player_x + 15)
    Debug.print(temp, half_screen_width, player_y + 15, player_x + 20)
    Debug.debug_playerRect((player_x, player_y), (tile_size, tile_size), temp)
    Debug.debug_screenRect((scene_width - display_width, scene_height - display_height), temp) # swapped
    ################################################

    # Calculate the Viewport position "Camera" that follows the player around
    camera_x = max(0, min(player_x - half_screen_width, scene_width - display_width))
    camera_y = max(0, min(player_y - half_screen_height, scene_height - display_height))

    screen.blit(temp, (-camera_x, -camera_y))

    # Update the surface/display (OpenGL support?)
    pygame.display.flip()
    ##################################################

    # Define framerate
    clock.tick(60)

# Quit Pygame (don't need sys.exit()?)
pygame.quit()