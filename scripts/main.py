from batch_generator import BaseBatchGenerator
from image import LogoImage
from utils import *
import math

if __name__ == "__main__":
    picture = LogoImage(
        width=512,
        height=512,
        logo_size_ratio=1.0,
        angle=0 * math.pi / 180,
    )
    picture.draw()
    picture.save(
        path=f"{os.path.join(output_folder,'test',picture.get_info())}.png",
        format="png",
    )
