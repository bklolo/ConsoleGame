# ExtractTiles.py

# Import necessary libraries
import os
import pygame
from pygame.locals import QUIT, KEYDOWN, K_ESCAPE

# Initialize Pygame
pygame.init()

image_path = "Game/images/dq1_sprite_colored.png"
output_folder = "character-slices_new"


# Load the source image containing tiles
original_image = pygame.image.load(image_path)

# Define the size of each tile
tile_size = 16

# Calculate the number of tiles in each row and column
num_cols = original_image.get_width() // tile_size
num_rows = original_image.get_height() // tile_size

# Create an empty list to store extracted tiles
tiles = []

# Extract tiles from the original image
for row in range(num_rows):
    for col in range(num_cols):
        x = col * tile_size
        y = row * tile_size
        tile = original_image.subsurface(pygame.Rect(x, y, tile_size, tile_size))
        tiles.append(tile)

# Create a folder to save the extracted tiles
os.makedirs(output_folder, exist_ok=True)

# Save each tile as a separate image file
for index, tile in enumerate(tiles):
    tile_filename = os.path.join(output_folder, f"tile_{index}.png")
    pygame.image.save(tile, tile_filename)

# Quit Pygame
pygame.quit()
