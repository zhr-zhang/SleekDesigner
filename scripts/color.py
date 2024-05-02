from typing import Dict, List, Tuple

Color = Tuple[int, int, int, int]

RED: Color = (240, 0, 80, 255)
BLUE: Color = (8, 131, 163, 255)
YELLOW: Color = (240, 222, 24, 255)
PURPLE: Color = (140, 80, 230, 255)

DARK: Color = (15, 15, 15, 255)
LIGHT: Color = (240, 240, 240, 255)
WHITE: Color = (255, 255, 255, 255)
BLACK: Color = (0, 0, 0, 255)
TRANSPARENT: Color = (0, 0, 0, 0)

COLOR_MAP: Dict[Color, str] = {
    RED: "r",
    BLUE: "u",
    YELLOW: "y",
    PURPLE: "p",
    DARK: "d",
    LIGHT: "l",
    WHITE: "w",
    BLACK: "a",
    TRANSPARENT: "t",
}

THEME_COLORS: List[Color] = [RED, BLUE, YELLOW]
BACKGROUND_COLORS: List[Color] = [BLACK, WHITE, TRANSPARENT]

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
