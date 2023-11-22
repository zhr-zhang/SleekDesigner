import os
from logo import *
from pattern import Pattern
from color import *

obj = zhr
format = "png"

Pattern.save(
    obj=obj.generate_image(
        width=2048,
        height=2048,
        ratio=0.7,
        angle_degrees=45,
    ),
    path=f"{obj.name}.{format}",
    format=format,
)
