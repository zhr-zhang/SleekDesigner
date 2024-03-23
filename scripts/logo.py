from color import *  # Assuming this imports predefined color constants
from pattern import Pattern
from figure import *
import math

# Define a pattern named 'zhr' with lines forming a specific geometric shape.
# This pattern includes horizontal lines at the top and bottom, a cross in the center,
# and additional horizontal lines in the middle.
zhr_pattern = Pattern(
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

# Define a pattern named 'syc' with arcs and lines creating a symmetrical design.
# This includes an arc centered at the origin and lines extending in different directions.
syc_pattern = Pattern(
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

# Define a pattern named 'llf' with a combination of dots and lines to form a unique layout.
# This pattern features a prominent dot, vertical and horizontal lines creating a framework.
llf_pattern = Pattern(
    figures=[
        Dot(position=(-1.5, 5), color=BLUE, distance=4),
        Line(a=(-1.5, -2), b=(4.5, -2), color=DARK),
        Line(a=(-1.5, 5), b=(-1.5, -8), color=BLUE),
        Line(a=(-1.5, -8), b=(4.5, -8), color=DARK),
    ],
    size=18,
    background_color=WHITE,
    name="llf",
)
