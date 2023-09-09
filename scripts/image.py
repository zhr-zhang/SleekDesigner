import numpy as np
from PIL import Image
from tqdm import tqdm
import json
from logo import Logo
from circle import Circle
from utils import *


# Define a class for generating and customizing the Z logo image
class LogoImage:
    """
    A class for generating and customizing the Z logo image.

    Attributes:
        width (int): Width of the image.
        height (int): Height of the image.
        use_round_shape (bool): Whether to use a round shape for the logo.
        logo_size_ratio (float): Ratio of logo size to the smaller dimension of the image.
        circle_size_ratio (float): Ratio of circle size to the smaller dimension of the image.
        outline_thickness (float): Thickness of the logo and circle outlines.
        background_color (tuple): RGBA color tuple for the background color.
        outside_line_body_color (tuple): RGBA color tuple for the body color of outside lines.
        outside_line_outline_color (tuple): RGBA color tuple for the outline color of outside lines.
        inside_line_body_color (tuple): RGBA color tuple for the body color of inside lines.
        inside_line_outline_color (tuple): RGBA color tuple for the outline color of inside lines.
        single_line_body_color (tuple): RGBA color tuple for the body color of single line.
        single_line_outline_color (tuple): RGBA color tuple for the outline color of single line.
        circle_body_color (tuple): RGBA color tuple for the body color of the circle.
        circle_outline_color (tuple): RGBA color tuple for the outline color of the circle.
        result (PIL.Image): The final generated logo image.
    """

    def __init__(
        self,
        width: int = 3840,
        height: int = 2160,
        use_round_shape: bool = False,
        logo_size_ratio: float = 0.5,
        circle_size_ratio: float = 0.6,
        outline_thickness: float = 2,
        background_color=BLACK,
        outside_line_body_color=LIGHT,
        outside_line_outline_color=LIGHT,
        inside_line_body_color=LIGHT,
        inside_line_outline_color=LIGHT,
        single_line_body_color=Z_RED,
        single_line_outline_color=Z_RED,
        circle_body_color=DARK,
        circle_outline_color=DARK,
    ) -> None:
        """
        Initialize the LogoImage class with various customizable parameters.

        Parameters:
            width (int): Width of the image.
            height (int): Height of the image.
            use_round_shape (bool): Whether to use a round shape for the logo.
            logo_size_ratio (float): Ratio of logo size to the smaller dimension of the image.
            circle_size_ratio (float): Ratio of circle size to the smaller dimension of the image.
            outline_thickness (float): Thickness of the logo and circle outlines.
            background_color (tuple): RGBA color tuple for the background color.
            outside_line_body_color (tuple): RGBA color tuple for the body color of outside lines.
            outside_line_outline_color (tuple): RGBA color tuple for the outline color of outside lines.
            inside_line_body_color (tuple): RGBA color tuple for the body color of inside lines.
            inside_line_outline_color (tuple): RGBA color tuple for the outline color of inside lines.
            single_line_body_color (tuple): RGBA color tuple for the body color of single line.
            single_line_outline_color (tuple): RGBA color tuple for the outline color of single line.
            circle_body_color (tuple): RGBA color tuple for the body color of the circle.
            circle_outline_color (tuple): RGBA color tuple for the outline color of the circle.
        """
        # Initialize customizable attributes based on the provided parameters
        self.width = int(width)
        self.height = int(height)
        self.use_round_shape = use_round_shape
        self.logo_size_ratio = logo_size_ratio
        self.circle_size_ratio = circle_size_ratio
        self.outline_thickness = outline_thickness
        self.outside_line_body_color = outside_line_body_color
        self.outside_line_outline_color = outside_line_outline_color
        self.inside_line_body_color = inside_line_body_color
        self.inside_line_outline_color = inside_line_outline_color
        self.single_line_body_color = single_line_body_color
        self.single_line_outline_color = single_line_outline_color
        self.circle_body_color = circle_body_color
        self.circle_outline_color = circle_outline_color
        self.background_color = background_color
        self.result = None

    def draw(self) -> None:
        """
        Draw the image
        """
        # Generate an information string for file naming
        self.infomation = self.get_info()

        # Create an empty RGBA image with the specified background color
        self.value = np.full(
            (self.width, self.height, 4), self.background_color, dtype=np.uint8
        )

        if self.use_round_shape:
            # Draw a circular region in the center of the image
            self.circle_radius = int(
                min(self.height, self.width) * self.circle_size_ratio // 2
            )
            circle_start_x = self.width // 2 - self.circle_radius
            circle_end_x = circle_start_x + self.circle_radius * 2
            circle_start_y = self.height // 2 - self.circle_radius
            circle_end_y = circle_start_y + self.circle_radius * 2

            # Generate the circle image with specified colors and outline thickness
            self.value[
                circle_start_x:circle_end_x, circle_start_y:circle_end_y
            ] = Circle(
                radius=self.circle_radius,
                outline_thickness=self.outline_thickness,
                body_color=self.circle_body_color,
                outline_color=self.circle_outline_color,
                image_slice=self.value[
                    circle_start_x:circle_end_x, circle_start_y:circle_end_y
                ],
            ).get_circle()

        # Place the logo in the center of the image
        self.logo_size = int(min(self.height, self.width) * self.logo_size_ratio)
        logo_start_x = (self.width - self.logo_size) // 2
        logo_end_x = logo_start_x + self.logo_size
        logo_start_y = (self.height - self.logo_size) // 2
        logo_end_y = logo_start_y + self.logo_size

        # Generate the logo image with specified colors and outline thickness
        self.value[logo_start_x:logo_end_x, logo_start_y:logo_end_y] = (
            Logo(
                logo_size=self.logo_size,
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

        # Convert the NumPy array to a PIL Image
        self.result = Image.fromarray(self.value.transpose(1, 0, 2), "RGBA")

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
            + str(self.circle_size_ratio)
            + "_"
            + str(self.outline_thickness)
            + "_"
            + COLOR_MAP.get(self.background_color, "UNKNOWN")
            + "_"
            + COLOR_MAP.get(self.circle_body_color, "UNKNOWN")
            + "_"
            + COLOR_MAP.get(self.circle_outline_color, "UNKNOWN")
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
            "use_round_shape": self.use_round_shape,
            "logo_size_ratio": self.logo_size_ratio,
            "circle_size_ratio": self.circle_size_ratio,
            "outline_thickness": self.outline_thickness,
            "background_color": self.background_color,
            "outside_line_body_color": self.outside_line_body_color,
            "outside_line_outline_color": self.outside_line_outline_color,
            "inside_line_body_color": self.inside_line_body_color,
            "inside_line_outline_color": self.inside_line_outline_color,
            "single_line_body_color": self.single_line_body_color,
            "single_line_outline_color": self.single_line_outline_color,
            "circle_body_color": self.circle_body_color,
            "circle_outline_color": self.circle_outline_color,
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

   

