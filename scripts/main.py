import os
from logo import *
from pattern import Pattern
from color import *

obj = zhr_pattern
format = "png"

obj.generate_video(
    ratio=0.5,
    path="logos/zhr/zhrwallpaperair.mp4",
    width=105 * 16 * 2,
    height=105 * 10 * 2,
    start_angle_degrees=45,
    degree_per_second=30,
    fps=60,
    time_seconds=6,
)


obj.save_image(
    obj=obj.generate_image(
        width=1920,
        height=1080,
        ratio=0.5,
        angle_degrees=45,
    ),
    path=f"logos/{obj.name}/{obj.name}.{format}",
    format=format,
)
