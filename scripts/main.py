from logo import syc
from pattern import Pattern
from PIL import Image
import os
from utils import *

Pattern.save(
    obj=syc.generate_image(
        width=2048,
        height=2048,
        ratio=0.7,
        angle_degrees=0,
    ),
    path=f"{syc.name}.png",
    format="png",
)
