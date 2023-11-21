from logo import Logo
from pattern import Pattern
from PIL import Image
import os
from utils import *


llf = Pattern(
    figures=[
        Dot((-1.5, 5), color=BLUE, distance=4),
        Line((-1.5, -2), (4.5, -2), color=DARK),
        Line((-1.5, 5), (-1.5, -8), color=BLUE),
        Line((-1.5, -8), (4.5, -8), color=DARK),
    ],
    size=18,
    background_color=WHITE,
)
Pattern.save(
    obj=llf.generate_image(
        width=2048,
        height=2048,
        ratio=0.7,
    ),
    path="llf.png",
)
