from asciimatics.effects import Effect
from asciimatics.exceptions import StopApplication
from asciimatics.screen import Screen
from asciimatics.scene import Scene  # Import Scene
import math
import random

class BouncingCircleEffect(Effect):
    def __init__(self, screen, colors, min_size, max_size):
        super(BouncingCircleEffect, self).__init__(screen)
        self._colors = colors
        self._min_size = min_size
        self._max_size = max_size
        self._x = random.randint(0, screen.width - 1)
        self._y = random.randint(0, screen.height - 1)
        self._angle = random.uniform(0, 2 * math.pi)
        self._speed = 1

    def update(self, frame_no):
        # Update the position of the circle
        self._x += self._speed * math.cos(self._angle)
        self._y += self._speed * math.sin(self._angle)

        # Bounce when reaching the edges
        if self._x <= 0 or self._x >= self._screen.width - 1:
            self._angle = math.pi - self._angle
        if self._y <= 0 or self._y >= self._screen.height - 1:
            self._angle = -self._angle

    def _draw_circle(self):
        # Draw the circle on the screen
        size = random.randint(self._min_size, self._max_size)
        color = random.choice(self._colors)
        char = 'o'  # Use a character that displays better
        for angle in range(0, 360, 5):
            x = int(self._x + size * math.cos(math.radians(angle)))
            y = int(self._y + size * math.sin(math.radians(angle)))
            if 0 <= x < self._screen.width and 0 <= y < self._screen.height:
                self._screen.print_at(char, x, y, color=color)

    def reset(self):
        # Reset the screen or do any cleanup if necessary
        pass

    def stop_frame(self):
        raise StopApplication("User quit")

    def _update(self, frame_no):
        # Minimal implementation for _update
        pass

    def _draw(self, frame_no):
        self._draw_circle()

# Run the effect
colors = [Screen.COLOUR_RED, Screen.COLOUR_GREEN, Screen.COLOUR_BLUE, Screen.COLOUR_YELLOW]
min_size = 3
max_size = 8

def main(screen):
    effect = BouncingCircleEffect(screen, colors, min_size, max_size)
    scenes = [
        Scene([effect], -1),
    ]
    screen.play(scenes, stop_on_resize=True)

Screen.wrapper(main)
