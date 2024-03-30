from color import *  # Assuming this imports predefined color constants
from pattern import Pattern
from figure import *
import math

# Define a pattern named 'zhr' with lines forming a specific geometric shape.
# This pattern includes horizontal lines at the top and bottom, a cross in the center,
# and additional horizontal lines in the middle.
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

# Define a pattern named 'syc' with arcs and lines creating a symmetrical design.
# This includes an arc centered at the origin and lines extending in different directions.
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

# Define a pattern named 'llf' with a combination of dots and lines to form a unique layout.
# This pattern features a prominent dot, vertical and horizontal lines creating a framework.
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
