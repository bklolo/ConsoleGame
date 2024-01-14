import pygame
from LevelManager import World


width = 24
height = 12

test = World(2,2)
test.generate_scene(0,0)
test.get_scene(0,0)
print(test)


