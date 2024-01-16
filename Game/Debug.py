import pygame
import random
pygame.init()

font = pygame.font.SysFont('monospace', 10, True)

class Debug:
    def print(screen, info, y = 10, x = 10):
        """print info to screen; y = x = 10 by default"""
        #display_surf = pygame.display.get_surface()  # get the screen
        debug_surf = font.render(str(info), True, 'Black')
        debug_rect = debug_surf.get_rect(topleft=(x,y))
        screen.blit(debug_surf, debug_rect)

    def debug_playerRect(left_top, width_height, temp):
        """Rect for player bounds"""
        playerRect = pygame.Rect(left_top ,width_height)
        pygame.draw.rect(temp, (0,0,0), playerRect, 1)

    def debug_screenRect(width_height, temp, left_top=(0,0)): 
        """Rect for visualizing viewport bounds"""
        screenRect = pygame.Rect(left_top, width_height)
        screenRect.center = temp.get_rect().center
        pygame.draw.rect(temp, (255,0,0), screenRect, 1)
        