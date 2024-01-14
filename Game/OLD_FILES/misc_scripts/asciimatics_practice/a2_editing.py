#!/usr/bin/env python3

from asciimatics.constants import SINGLE_LINE, DOUBLE_LINE, ASCII_LINE
from asciimatics.effects import Print
from asciimatics.exceptions import ResizeScreenError
from asciimatics.renderers import BarChart, VBarChart, FigletText
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.utilities import BoxTool
import sys
import math
import time
from random import randint

'''
class BarChart(
    height: int,
    width: int,
    functions: list[() -> float],
    char: str = "#",
    colour: int = Screen.COLOUR_GREEN,
    bg: int = Screen.COLOUR_BLACK,
    gradient: Any | None = None,
    scale: Any | None = None,
    axes: int = _BarChartBase.Y_AXIS,
    intervals: Any | None = None,
    labels: bool = False,
    border: bool = True,
    keys: Any | None = None,
    gap: Any | None = None
)
'''
def fn():
    return randint(0, 10)

def fn2():
    return randint(0, 6)


def wv(x):
    return lambda: 1 + math.sin(math.pi * (2*time.time()+x) / 5)


def demo(screen):
    scenes = []
    # Horizontal Charts
    hchart4 = BarChart(7, 30, [lambda: time.time() * 10 % 101],
                  gradient=[
                      (33, Screen.COLOUR_RED, Screen.COLOUR_RED),
                      (66, Screen.COLOUR_YELLOW, Screen.COLOUR_YELLOW),
                      (100, Screen.COLOUR_WHITE, Screen.COLOUR_WHITE),
                  ] if screen.colours < 256 else [
                      (10, 234, 234), (20, 236, 236), (30, 238, 238),
                      (40, 240, 240), (50, 242, 242), (60, 244, 244),
                      (70, 246, 246), (80, 248, 248), (90, 250, 250),
                      (100, 252, 252)
                  ],
                  char=">", scale=100.0, labels=True, axes=BarChart.X_AXIS)
    hchart4.border_style = SINGLE_LINE

    # Vertical Charts
    vchart4 = VBarChart(12, 16, [lambda: time.time() * 10 % 101],
                  gradient=[
                      (33, Screen.COLOUR_RED, Screen.COLOUR_RED),
                      (66, Screen.COLOUR_YELLOW, Screen.COLOUR_YELLOW),
                      (100, Screen.COLOUR_WHITE, Screen.COLOUR_WHITE),
                  ] if screen.colours < 256 else [
                      (10, 234, 234), (20, 236, 236), (30, 238, 238),
                      (40, 240, 240), (50, 242, 242), (60, 244, 244),
                      (70, 246, 246), (80, 248, 248), (90, 250, 250),
                      (100, 252, 252)
                  ],
                  char=">", scale=100.0, labels=True, axes=VBarChart.Y_AXIS)
    vchart4.border_style = SINGLE_LINE

    effects = [
        Print(screen, hchart4, x=96, y=2, transparent=False, speed=2),
        Print(screen, vchart4, x=103, y=12, transparent=False, speed=2),
    ]

    scenes.append(Scene(effects, -1))
    screen.play(scenes, stop_on_resize=True)


while True:
    try:
        Screen.wrapper(demo)
        sys.exit(0)
    except ResizeScreenError:
        pass