from utils import *
from logo_image import LogoImage
from create import BaseLogoImageBatchGenerator

if __name__ == "__main__":
    generator = BaseLogoImageBatchGenerator(draw=True,save=True)
    generator.generate()
    # main()
    # instance = LogoImage(
    #     outside_line_body_color=Z_BLUE,
    #     outside_line_outline_color=Z_BLUE,
    #     inside_line_body_color=Z_RED,
    #     inside_line_outline_color=Z_RED,
    #     single_line_body_color=Z_YELLOW,
    #     single_line_outline_color=Z_YELLOW,
    #     use_round_shape=True,
    #     circle_size_ratio=1,
    # )
    # instance.draw()
    # instance.result.show()
