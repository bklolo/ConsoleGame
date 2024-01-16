import pygame
import sys

pygame.init()

# Set up screen
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Centered Rect")

# Set up red rectangle
rect_width, rect_height = 50, 50
rect = pygame.Rect(0, 0, rect_width, rect_height)
rect.center = screen.get_rect().center  # Center the rectangle in the screen

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Draw
    screen.fill((255, 255, 255))  # White background
    pygame.draw.rect(screen, (255, 0, 0), rect)  # Red rectangle

    pygame.display.flip()
