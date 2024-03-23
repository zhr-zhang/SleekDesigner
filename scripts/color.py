from typing import Dict, List, Tuple

# Type annotation for clarity
Color = Tuple[int, int, int, int]

# RGBA color constants for easy reference
RED: Color = (240, 0, 80, 255)
BLUE: Color = (8, 131, 163, 255)
YELLOW: Color = (240, 222, 24, 255)
PURPLE: Color = (140, 80, 230, 255)

DARK: Color = (15, 15, 15, 255)
LIGHT: Color = (240, 240, 240, 255)
WHITE: Color = (255, 255, 255, 255)
BLACK: Color = (0, 0, 0, 255)
TRANSPARENT: Color = (0, 0, 0, 0)

# Create a color map to associate RGBA color constants with human-readable names
COLOR_MAP: Dict[Color, str] = {
    RED: "r",
    BLUE: "u",
    YELLOW: "y",
    PURPLE: "p",
    DARK: "d",
    LIGHT: "l",
    WHITE: "w",
    BLACK: "a",  # Using 'a' for black to avoid confusion with 'b' potentially representing blue.
    TRANSPARENT: "t",
}

# Define the theme colors and background colors for the logo (used in color combinations)
THEME_COLORS: List[Color] = [RED, BLUE, YELLOW]
BACKGROUND_COLORS: List[Color] = [BLACK, WHITE, TRANSPARENT]

# Define a list of color schemes for the logo, each scheme is a combination of colors
color_schemes: List[List[Color]] = [
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

# The color schemes are organized by primary color (theme color) followed by secondary and background colors.
# This standardized approach makes it easier to understand and modify the color combinations for various design needs.
