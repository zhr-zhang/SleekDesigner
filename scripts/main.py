import os
from logo import *
from pattern import Pattern
from color import *

obj = llf
format = "png"

obj.generate_video(filename="llf1024")

# Pattern.save(
#     obj=obj.generate_image(
#         width=2048,
#         height=2048,
#         ratio=0.7,
#         angle_degrees=0,
#     ),
#     path=f"{obj.name}.{format}",
#     format=format,
# )
