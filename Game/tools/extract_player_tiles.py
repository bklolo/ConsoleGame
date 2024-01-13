# ExtractTiles.py

# Import necessary libraries
import os
import pygame
from pygame.locals import QUIT, KEYDOWN, K_ESCAPE

# Initialize Pygame
pygame.init()

# Load the source image containing tiles
image_path = "Game/images/chars_nobg.png"
original_image = pygame.image.load(image_path)

# Define the size of each tile
tile_size = 16
tile_width_offset = 3
tile_height_offset = 4
# Calculate the number of tiles in each row and column
num_cols = 8 #original_image.get_width() // tile_size
num_rows = 1 #original_image.get_height() // tile_size

sprite_height = 16
sprite_width = [16,16,13,14,16,16,14,13]

# Create an empty list to store extracted tiles
tiles = []

# Extract tiles from the original image
for spriteW in sprite_width:
    x = tile_width_offset 
    y = tile_height_offset 
    tile = original_image.subsurface(pygame.Rect(x, y, spriteW, sprite_height))
    tiles.append(tile)
    tile_width_offset += spriteW

# for row in range(num_rows):
#     for col in range(num_cols):
#         x = col * tile_size + tile_width_offset
#         y = row * tile_size + tile_height_offset
#         tile = original_image.subsurface(pygame.Rect(x, y, tile_size, tile_size))
#         tiles.append(tile)

# Create a folder to save the extracted tiles
output_folder = "character-slices"
os.makedirs(output_folder, exist_ok=True)

# Save each tile as a separate image file
for index, tile in enumerate(tiles):
    tile_filename = os.path.join(output_folder, f"tile_{index}.png")
    pygame.image.save(tile, tile_filename)

# Quit Pygame
pygame.quit()
