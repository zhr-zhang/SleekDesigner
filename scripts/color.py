import os
from figure import *

# Define RGBA color constants for easy reference
RED = (240, 0, 80, 255)
BLUE = (8, 131, 163, 255)
YELLOW = (240, 222, 24, 255)
PURPLE = (140, 80, 230, 255)

DARK = (15, 15, 15, 255)
LIGHT = (240, 240, 240, 255)

WHITE = (255, 255, 255, 255)
BLACK = (0, 0, 0, 255)

TRANSPARENT = (0, 0, 0, 0)


# Create a color map to associate color constants with human-readable names
COLOR_MAP = {
    RED: "r",
    BLUE: "u",
    YELLOW: "y",
    DARK: "d",
    LIGHT: "l",
    WHITE: "w",
    BLACK: "a",
    TRANSPARENT: "t",
}

# Define the theme colors and background colors for the logo (used in color combinations)
THEME_COLORS = [RED, BLUE, YELLOW]
BACKGROUND_COLORS = [BLACK, WHITE, TRANSPARENT]

color_schemes = [
    [RED, LIGHT, BLACK],
    [RED, DARK, WHITE],
    [LIGHT, RED, BLACK],
    [DARK, RED, WHITE],
    [BLUE, LIGHT, BLACK],
    [BLUE, DARK, WHITE],
    [LIGHT, BLUE, BLACK],
    [DARK, BLUE, WHITE],
    [YELLOW, LIGHT, BLACK],
    [YELLOW, DARK, WHITE],
    [LIGHT, YELLOW, BLACK],
    [DARK, YELLOW, WHITE],
]
