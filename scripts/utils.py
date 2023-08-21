# Define RGBA color constants for easy reference
Z_RED = (240, 0, 80, 255)
Z_BLUE = (8, 131, 163, 255)
Z_YELLOW = (240, 222, 24, 255)

DARK = (15, 15, 15, 255)
LIGHT = (240, 240, 240, 255)

WHITE = (255, 255, 255, 255)
BLACK = (0, 0, 0, 255)

TRANSPARENT = (0, 0, 0, 0)


# Create a color map to associate color constants with human-readable names
COLOR_MAP = {
    Z_RED: "zRed",
    Z_BLUE: "zBlue",
    Z_YELLOW: "zYellow",
    DARK: "dark",
    LIGHT: "light",
    WHITE: "white",
    BLACK: "black",
    TRANSPARENT: "transparent",
}

# Define the theme colors and background colors for the logo (used in color combinations)
THEME_COLORS = [Z_RED, Z_BLUE, Z_YELLOW]
BACKGROUND_COLORS = [BLACK, WHITE, TRANSPARENT]
