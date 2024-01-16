import pygame
import os
import sys

# Demo of the PyGame blit method doing a BLEND_ADD of a image and a mask
# in this case a muted image of a rubrics cube and a mask with rectangles to brighten
# the red, green, blue channels by a bit, and the to brighten all the channels in the last region
# (C) 2020 Gerry Jenkins


def wait_key():  # flip and then await any key or quit
    pygame.display.flip()  # write to screen then wait
    while True:  # keep looping till key
        for event in pygame.event.get():  # loop to get all events
            if event.type == pygame.KEYDOWN:  # if key, then return
                return
            elif event.type == pygame.QUIT:
                sys.exit()

# setup


os.environ['SDL_VIDEO_WINDOW_POS'] = "1100,100"  # where window is located
pygame.init()
screen = pygame.display.set_mode((800, 400))  # create surface screen associated with display
font = pygame.font.SysFont("San Serif", 28)
bgcolor = 255, 255, 255  # white
screen.fill(bgcolor)

image = pygame.image.load("rubics.png").convert_alpha()  # create picture surface
mask = pygame.image.load("mask.png").convert_alpha()

screen.blit(image, (50, 50))  # show original image
screen.blit(mask, (300, 50))  # and mask
screen.blit(image, (550, 50))  # and where original will change

text = font.render("hit key to see blend", True, (0, 0, 0))
screen.blit(text, (50, 275))

wait_key()
pygame.draw.rect(screen, bgcolor, text.get_rect().move(50, 275))  # erase text

# now overwrite image with blended image + mask
image.blit(mask, (0, 0), special_flags=pygame.BLEND_RGB_ADD)
screen.blit(image, (550, 50))
wait_key()