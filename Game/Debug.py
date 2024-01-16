import pygame
import random
pygame.init()

font = pygame.font.SysFont('monospace', 8, True)

class Debug:
    def print(screen, info, y = 10, x = 10):
        #display_surf = pygame.display.get_surface()  # get the screen
        debug_surf = font.render(str(info), True, 'Black')
        debug_rect = debug_surf.get_rect(topleft=(x,y))
        screen.blit(debug_surf, debug_rect)

    def debug_playerRect(x, y, tile_size, temp):
        playerRect = pygame.Rect(x,y,tile_size,tile_size)
        pygame.draw.rect(temp, (0,0,0), playerRect, 1)

    def debug_screenRect(half_screen_width, half_screen_height, screen_width, screen_height, temp):
        screenRect = pygame.Rect(half_screen_width, half_screen_height, screen_width, screen_height)
        pygame.draw.rect(temp, (255,0,0), screenRect, 1)
        