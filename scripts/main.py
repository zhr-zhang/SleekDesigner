from logo import Logo, logos
from pattern import Pattern
from PIL import Image
import os
from utils import *


llf = Pattern(
    figures=[
        Dot((-3, 7), color=WHITE, distance=5),
        Line((-3, 0), (3, 0), color=WHITE),
        Line((-3, 7), (-3, -7), color=RED),
        Line((-3, -7), (3, -7), color=WHITE),
    ],
    size=25,
)
Pattern.save(obj=llf.generate_image(), path="llf.png")


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
