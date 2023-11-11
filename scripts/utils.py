import os
from figure import *

# Define RGBA color constants for easy reference
RED = (240, 0, 80, 255)
BLUE = (8, 131, 163, 255)
YELLOW = (240, 222, 24, 255)

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


# Define the folder where the generated logo images will be saved
script_directory = os.path.dirname(os.path.abspath(__file__))
output_folder = os.path.join(script_directory, "..", "output")
os.makedirs(output_folder, exist_ok=True)

CLASSIC_LOGO_FIGURES = [
    Line(
        a=(-6, 6),
        b=(6, 6),
        color=WHITE,
    ),
    Line(
        a=(-6, -6),
        b=(6, -6),
        color=WHITE,
    ),
    Line(
        a=(-2, 2),
        b=(2, 2),
        color=WHITE,
    ),
    Line(
        a=(-2, -2),
        b=(2, -2),
        color=WHITE,
    ),
    Line(
        a=(6, 6),
        b=(-6, -6),
        color=RED,
    ),
    # Arc(
    #     center=(0, 0),
    #     a=(10, -6),
    #     b=(10, 6),
    #     color=RED,
    # ),
    # Arc(
    #     center=(0, 0),
    #     a=(-10, 6),
    #     b=(-10, -6),
    #     color=RED,
    # ),
    # Arc(
    #     center=(0, 0),
    #     a=(6, 10),
    #     b=(-6, 10),
    #     color=RED,
    # ),
    # Arc(
    #     center=(0, 0),
    #     a=(-6, -10),
    #     b=(6, -10),
    #     color=RED,
    # ),
]
CLASSIC_LOGO_SIZE = 2 + 12 * math.sqrt(2)
