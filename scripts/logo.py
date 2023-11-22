from color import *
from pattern import Pattern
from figure import *


zhr = Pattern(
    figures=[
        Line(a=(-6, 6), b=(6, 6), color=LIGHT),
        Line(a=(-6, -6), b=(6, -6), color=LIGHT),
        Line(a=(-2, 2), b=(2, 2), color=LIGHT),
        Line(a=(-2, -2), b=(2, -2), color=LIGHT),
        Line(a=(6, 6), b=(-6, -6), color=RED),
    ],
    size=12 * math.sqrt(2) + 2,
    background_color=BLACK,
    name="zhr",
)

syc = Pattern(
    figures=[
        Arc(
            center=(0, 0),
            a=(8 * math.sqrt(2), 4),
            b=(8 * math.sqrt(2), -4),
            color=LIGHT,
        ),
        Line(a=(0, 0), b=(-4 * math.sqrt(2), 4 * math.sqrt(2)), color=PURPLE),
        Line(a=(0, 0), b=(-4 * math.sqrt(2), -4 * math.sqrt(2)), color=PURPLE),
        Line(a=(0, 0), b=(12, 0), color=LIGHT),
    ],
    size=26,
    background_color=BLACK,
    name="syc",
)

llf = Pattern(
    figures=[
        Dot((-1.5, 5), color=BLUE, distance=4),
        Line((-1.5, -2), (4.5, -2), color=DARK),
        Line((-1.5, 5), (-1.5, -8), color=BLUE),
        Line((-1.5, -8), (4.5, -8), color=DARK),
    ],
    size=18,
    background_color=WHITE,
    name="llf",
)
