import os
import pygame
from pygame.locals import QUIT, KEYDOWN, K_ESCAPE
from Player import Controller
from LevelManager import *
from Debug import Debug
import Audio

######################## TODO #######################
# Player 
#   - animation tied to speed
#   - considering player size for the offsets?
# World
#   - open world, generate scene based on position?
#####################################################

os.environ['SDL_VIDEO_WINDOW_POS'] = "700,30"  # where window is located
# Pygame init
pygame.init()

###################### Screen #######################
player_size = 16
display_width = player_size * 25
display_height = display_width * 0.75
display = pygame.display.set_mode((display_width, display_height),pygame.SCALED)
pygame.display.set_caption("Pygame")
screen = pygame.display.get_surface()

####################### Level #######################
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
# Create surface to draw on
field = pygame.Surface((scene_width, scene_height))
# Draw on surface
mapper.draw_tiles(tilemap_data, tile_size, tile_images, field)
################## Setup character ##################
player_start_pos = (field.get_width()/2, field.get_height()/2) ; player_speed = 0.2
player_images =[pygame.image.load(f"character-slices_new/tile_{i}.png") for i in range(0,8)]
player = Controller(player_images, player_start_pos, player_speed, scene_width, scene_height) # display vs scene
#####################################################

# Colors
color_black = (0, 0, 0)
color_white = (255, 255, 255)
color_btn_quit = (200, 0, 0)
color_btn_play = (0, 160, 0)
color_btn_highlight = (53, 115, 255)

# Game loop vars
temp = pygame.Surface((field.get_size()))
debug = 0
clock = pygame.time.Clock()

# Audio
music = Audio.Audio('Game\\Audio\\title.wav')
####################################################
##################### Functions ####################
####################################################

def text_objects(text, font):
    textSurface = font.render(text, True, color_black)
    return textSurface, textSurface.get_rect()

def button(message, x, y, width, height, inactive_color, active_color, action=None):
    # Get mouse position and button state
    mouse_x, mouse_y = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    # Check if the mouse is over the button
    if (x < mouse_x < x + width) and (y < mouse_y < y + height):
        pygame.draw.rect(display, active_color, (x, y, width, height))  # highlight
        if click[0] == 1 and action is not None:
            action()  # call passed function
    else:
        pygame.draw.rect(display, inactive_color, (x, y, width, height))
    # Button font
    font = pygame.font.SysFont('monospace', 20, True)
    text_surface, text_rect = text_objects(message, font)
    text_rect.center = (x + (width / 2), y + (height / 2))
    display.blit(text_surface, text_rect)


def game_intro():
    music.play_song()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Background
        bg = pygame.image.load('Game\\images\\title_bg.png')
        display.blit(bg, (-250,-250))

        # Title
        ## font
        title_font = pygame.font.SysFont('monospace', 44, True)
        title_text = title_font.render("Console Game", True, (0, 0, 0))
        ## surface
        title_surface = pygame.Surface((display_width - 75, display_height/2 - 100), pygame.SRCALPHA)
        title_surface.fill((255,255,255, 150))  # title color and alpha
        title_surface.blit(title_text, (0,0))
        display.blit(title_surface, (50,50))

        # Buttons
        button("Play", 50, display_height / 2 + 20, 100, 50, color_btn_play, color_btn_highlight, game_loop)
        button("Quit", 200, display_height / 2 + 20, 100, 50, color_btn_quit, color_btn_highlight, quitgame)

        pygame.display.update()


def game_loop():
    # Game loop vars
    playing = True
    previousFrameTicks = 0
    currentFrameTicks = 0
    deltaTime = 0
    half_screen_width = display_width / 2
    half_screen_height = display_height / 2
    camera_speed = 1.0  # Adjust this value as needed for the desired camera speed

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
        if(debug):
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


def quitgame():
    pygame.quit()
    quit()


game_intro()
game_loop()
pygame.quit()   # pygame quit
quit()          # sys quit