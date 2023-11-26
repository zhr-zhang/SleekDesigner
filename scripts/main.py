import os
from logo import *
from pattern import Pattern
from color import *

obj = syc
format = "png"

obj.generate_video(path="syc1024.mp4",time_seconds=1)

Pattern.save_image(
    obj=obj.generate_image(
        width=2048,
        height=2048,
        ratio=0.7,
        angle_degrees=0,
    ),
    path=f"{obj.name}.{format}",
    format=format,
)
