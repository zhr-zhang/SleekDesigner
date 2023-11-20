from logo import Logo, logos
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


# arrow = Pattern(
#     figures=[
#         Line((10, 0), (0, 10), color=WHITE),
#         Line((10, 0), (0, -10), color=WHITE),
#         Line((-10, 0), (10, 0), color=RED),
#     ],
#     size=22,
# )
# Pattern.save(obj=arrow.generate_image(), path="arrow.png")

# i = 0
# for logo in logos:
#     Image.fromarray(
#         logo.generate_image(),
#         mode="RGBA",
#     ).save(os.path.join(output_folder, f"{i}.png"))
#     i += 1
