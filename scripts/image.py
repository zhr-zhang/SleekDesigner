import numpy as np
from PIL import Image
import json
from logo import Logo
from utils import *
import math


# Define a class for generating and customizing the Z logo image
class LogoImage:
    """
    A class for generating and customizing the Z logo image.
    """

    def __init__(
        self,
        width: int = 3840,
        height: int = 2160,
        angle=math.pi/4,
        logo_size_ratio: float = 0.5,
        outline_thickness: float = 2,
        background_color=BLACK,
        outside_line_body_color=LIGHT,
        outside_line_outline_color=LIGHT,
        inside_line_body_color=LIGHT,
        inside_line_outline_color=LIGHT,
        single_line_body_color=Z_RED,
        single_line_outline_color=Z_RED,
    ) -> None:
        """
        Initialize the LogoImage class with various customi
        """
        # Initialize customizable attributes based on the provided parameters
        self.width = int(width)
        self.height = int(height)
        self.logo_size_ratio = logo_size_ratio
        self.angle=angle
        self.outline_thickness = outline_thickness
        self.background_color = background_color
        self.outside_line_body_color = outside_line_body_color
        self.outside_line_outline_color = outside_line_outline_color
        self.inside_line_body_color = inside_line_body_color
        self.inside_line_outline_color = inside_line_outline_color
        self.single_line_body_color = single_line_body_color
        self.single_line_outline_color = single_line_outline_color
        self.result = None

    def draw(self) -> None:
        """
        Draw the image
        """
        self.infomation = self.get_info()

        self.value = np.full(
            (self.width, self.height, 4), self.background_color, dtype=np.uint8
        )

        self.logo_size = int(min(self.height, self.width) * self.logo_size_ratio)
        logo_start_x = (self.width - self.logo_size) // 2
        logo_end_x = logo_start_x + self.logo_size
        logo_start_y = (self.height - self.logo_size) // 2
        logo_end_y = logo_start_y + self.logo_size

        self.value[logo_start_x:logo_end_x, logo_start_y:logo_end_y] = (
            Logo(
                logo_size=self.logo_size,
                angle=self.angle,
                outline_thickness=self.outline_thickness,
                outside_line_body_color=self.outside_line_body_color,
                outside_line_outline_color=self.outside_line_outline_color,
                inside_line_body_color=self.inside_line_body_color,
                inside_line_outline_color=self.inside_line_outline_color,
                single_line_body_color=self.single_line_body_color,
                single_line_outline_color=self.single_line_outline_color,
                image_slice=self.value[
                    logo_start_x:logo_end_x, logo_start_y:logo_end_y
                ],
            )
            .get_logo()
            .transpose((1, 0, 2))[::-1, :, :]
        )

        self.result = Image.fromarray(self.value, "RGBA")

    def get_info(self):
        """
        Get information about the logo image for file naming.

        Returns:
            str: Information string for file naming.
        """
        image_info = (
            "z_logo_"
            + str(self.width)
            + "_"
            + str(self.height)
            + "_"
            + str(self.logo_size_ratio)
            + "_"
            + str(self.outline_thickness)
            + "_"
            + COLOR_MAP.get(self.outside_line_body_color, "UNKNOWN")
            + "_"
            + COLOR_MAP.get(self.outside_line_outline_color, "UNKNOWN")
            + "_"
            + COLOR_MAP.get(self.inside_line_body_color, "UNKNOWN")
            + "_"
            + COLOR_MAP.get(self.inside_line_outline_color, "UNKNOWN")
            + "_"
            + COLOR_MAP.get(self.single_line_body_color, "UNKNOWN")
            + "_"
            + COLOR_MAP.get(self.single_line_outline_color, "UNKNOWN")
        )
        return image_info

    def save_cfg(self, path: str = "cfg.json", mode="W") -> None:
        """
        Save the current parameters to a JSON file.

        Parameters:
            path (str): Path to the JSON file.
        """
        # Convert the parameters to a dictionary
        cfg = {
            "width": self.width,
            "height": self.height,
            "logo_size_ratio": self.logo_size_ratio,
            "outline_thickness": self.outline_thickness,
            "outside_line_body_color": self.outside_line_body_color,
            "outside_line_outline_color": self.outside_line_outline_color,
            "inside_line_body_color": self.inside_line_body_color,
            "inside_line_outline_color": self.inside_line_outline_color,
            "single_line_body_color": self.single_line_body_color,
            "single_line_outline_color": self.single_line_outline_color,
        }

        # Save the dictionary to a JSON file
        with open(path, mode=mode) as f:
            json.dump(cfg, f, indent=4)

    def save(self, path, format) -> None:
        """
        Save the final image to a file.
        """
        self.result.save(path, format=format)

    def get_image(self):
        """
        Get the final image.

        Returns:
            Image: The final image.
        """
        return self.result
