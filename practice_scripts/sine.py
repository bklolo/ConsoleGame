import os
import time
import math
import msvcrt
import shutil

# Uses shutil to get the dimensions of the console
def get_console_width():
    try:
        columns, _ = shutil.get_terminal_size()
        return columns
    except:
        return 80  # Default value if unable to get console width

# Draws the ASCII characters
def draw_ascii_art(y_position, x_offset, rng, sine_components):
    vertical_offset = 10

    # Calculate the total value as the sum of individual sine wave components
    # Characteristics of sinewave
    ### 
    total_value = sum(
        amplitude * math.sin(frequency * (y_position - x_offset) + phase)
        for amplitude, frequency, phase in sine_components
    )

    sine_wave = round(total_value + vertical_offset)

    art = ""
    for i in range(rng):
        if i == sine_wave:
            art += "="
        else:
            art += " "
    return art


# Define sine wave components (amplitude, frequency, phase)
sine_components = [
    (1, 0.5, 1),
    (2, 0.4, math.pi / 2),
    (3, 0.3, math.pi),
    (5, 0.2, 2*math.pi)
]

console_width = get_console_width()
rng = console_width - 1  # Set rng to the console width
sleep = 0.05

while True:
    for x in range(console_width):
        x_offset = x % console_width  # Ensure x_offset wraps around
        sine_lines = [draw_ascii_art(y, x_offset, rng, sine_components) for y in range(1, console_width)]
        print("\r" + "\n".join(sine_lines), end="")

        if msvcrt.kbhit():
            key = msvcrt.getch().decode('utf-8')

            if key.lower() == 'q':
                break

        time.sleep(sleep)
