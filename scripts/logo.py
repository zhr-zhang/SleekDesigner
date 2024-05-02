from color import *
from pattern import Pattern
from figure import *
import math

zhr_pattern = Pattern(
    figures=[
        Line(a=Point(6, 6), b=Point(-6, -6), color=RED),
        Line(a=Point(-6, 6), b=Point(6, 6), color=LIGHT),
        Line(a=Point(-6, -6), b=Point(6, -6), color=LIGHT),
        Line(a=Point(-2, 2), b=Point(2, 2), color=LIGHT),
        Line(a=Point(-2, -2), b=Point(2, -2), color=LIGHT),
    ],
    grids_x=12 * math.sqrt(2) + 2,
    grids_y=12 * math.sqrt(2) + 2,
    background_color=BLACK,
    name="zhr",
)

syc_pattern = Pattern(
    figures=[
        Arc(
            center=Point(0, 0),
            a=Point(8 * math.sqrt(2), 4),
            b=Point(8 * math.sqrt(2), -4),
            color=LIGHT,
        ),
        Line(a=Point(0, 0), b=Point(-4 * math.sqrt(2), 4 * math.sqrt(2)), color=PURPLE),
        Line(
            a=Point(0, 0), b=Point(-4 * math.sqrt(2), -4 * math.sqrt(2)), color=PURPLE
        ),
        Line(a=Point(0, 0), b=Point(12, 0), color=LIGHT),
    ],
    grids_x=26,
    grids_y=26,
    background_color=BLACK,
    name="syc",
)

llf_pattern = Pattern(
    figures=[
        Dot(position=Point(-1.5, 5), color=BLUE, distance=4),
        Line(a=Point(-1.5, -2), b=Point(4.5, -2), color=DARK),
        Line(a=Point(-1.5, 5), b=Point(-1.5, -8), color=BLUE),
        Line(a=Point(-1.5, -8), b=Point(4.5, -8), color=DARK),
    ],
    grids_x=18,
    grids_y=18,
    background_color=WHITE,
    name="llf",
)

llf_injured_pattern = Pattern(
    figures=[
        Dot(position=Point(0.9, -5.9), color=RED, distance=1),
        Dot(position=Point(-1.5, 5), color=BLUE, distance=4),
        Line(a=Point(-1.5, -2), b=Point(4.5, -2), color=LIGHT),
        Line(a=Point(-1.5, 5), b=Point(-1.5, -8), color=BLUE),
        Line(a=Point(-1.5, -8), b=Point(4.5, -8), color=LIGHT),
        Line(a=Point(-1.5, -8), b=Point(1, -6), color=LIGHT),
        Line(a=Point(1, -6), b=Point(3.5, -5.5), color=LIGHT),
    ],
    grids_x=18,
    grids_y=18,
    background_color=BLACK,
    name="llfInjured",
)

debug = Pattern(
    figures=[
        Dot(Point(3, 3), color=RED, distance=4),
        Dot(Point(-3, 3), color=BLUE, distance=4),
        Dot(Point(-3, -3), color=YELLOW, distance=4),
        Dot(Point(3, -3), color=LIGHT, distance=4),
    ],
    background_color=BLACK,
    grids_x=12,
    grids_y=12,
    name="debug",
)
