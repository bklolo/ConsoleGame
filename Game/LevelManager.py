import pygame
from tools.SceneGenerator import SceneGenerator

class Scene:
    def __init__(self):
        self.contents = []

class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.world = [[Scene() for _ in range(width)] for _ in range(height)]

    def get_world(self):
        return [[scene.contents for scene in row] for row in self.world]
    
    
    def get_scene(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.world[y][x].contents
        else:
            return None

    def add_scene_contents(self, x, y, contents):
        if 0 <= x < self.width and 0 <= y < self.height:
            self.world[y][x].contents.extend(contents)

    def generate_scene(self, x, y):
        generator = SceneGenerator(self.width, self.height)
        new_contents = generator.generate_scene()
        self.add_scene_contents(x, y, new_contents)

'''
# Example usage:
screen_width = 10
screen_height = 5
grid = 4
world = World(3, 3) # world grid
world.generate_scene(0,0)
world.generate_scene(2,2)

start_level = world.get_scene(0,0)
level1 = world.get_scene(2,2)
# Access contents of a scene
print(world.get_world())
'''