import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create Pygame window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Encounter Screen")

# Font
font = pygame.font.Font(None, 36)

# Enemy information
enemy_name = "Evil Cat"
enemy_health = 100

# Load enemy image
enemy_image = pygame.image.load("Game\images\carIcon.png")  # Replace with your image file

# Menu options
menu_options = ["FIGHT", "ITEM", "CAST", "FLEE"]

def draw_encounter_screen():
    # Clear the screen
    screen.fill(BLACK)

    # Draw enemy information
    enemy_info_text = font.render(f"{enemy_name} - Health: {enemy_health}", True, WHITE)
    screen.blit(enemy_info_text, (10, 10))

    # Draw enemy image
    screen.blit(enemy_image, (WIDTH // 2 - enemy_image.get_width() // 2, HEIGHT // 3))

    # Draw menu options
    menu_y = HEIGHT - 50
    menu_x = WIDTH //2 - 150
    for option in menu_options:
        option_text = font.render(option, True, WHITE)
        option_rect = option_text.get_rect(center=(menu_x, menu_y))
        screen.blit(option_text, option_rect)
        menu_x += 100

    # Update the display
    pygame.display.flip()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw encounter screen
    draw_encounter_screen()

    pygame.time.Clock().tick(FPS)

# Quit Pygame
pygame.quit()
sys.exit()
