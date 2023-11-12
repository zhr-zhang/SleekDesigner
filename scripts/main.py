# from utils import *
from logo import Logo, logos
from PIL import Image
import os
from utils import *

# logo = Logo()
# Image.fromarray(logo.generate_image(), mode="RGBA").save("test.png")
# # logo.generate_video(filename="test.mp4")
i = 0
for logo in logos:
    Image.fromarray(logo.generate_image(), mode="RGBA").save(
        os.path.join(output_folder, f"{i}.png")
    )
    i += 1
