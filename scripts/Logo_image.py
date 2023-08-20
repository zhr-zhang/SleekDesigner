import numpy as np
from PIL import Image
import math
from tqdm import tqdm

from utils import *


# Define a class for generating and customizing the Z logo image
class LogoImage:
    def __init__(
        self,
        width: int = 3840,
        height: int = 2160,
        use_round_shape: bool = False,
        logo_size_ratio: float = 0.5,
        circle_size_ratio: float = 0.6,
        outline_thickness: float = 2,
        background_color=BLACK,
        normal_line_body_color=LIGHT,
        normal_line_outline_color=LIGHT,
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
            normal_line_body_color (tuple): RGBA color tuple for normal line body color.
            normal_line_outline_color (tuple): RGBA color tuple for normal line outline color.
            single_line_body_color (tuple): RGBA color tuple for single line body color.
            single_line_outline_color (tuple): RGBA color tuple for single line outline color.
            circle_body_color (tuple): RGBA color tuple for circle body color.
            circle_outline_color (tuple): RGBA color tuple for circle outline color.
        """
        # Initialize customizable attributes based on the provided parameters
        self.height = int(height)
        self.width = int(width)
        self.use_round_shape = use_round_shape
        self.logo_size_ratio = logo_size_ratio
        self.circle_size_ratio = circle_size_ratio
        self.outline_thickness = outline_thickness
        self.normal_line_body_color = normal_line_body_color
        self.normal_line_outline_color = normal_line_outline_color
        self.single_line_body_color = single_line_body_color
        self.single_line_outline_color = single_line_outline_color
        self.circle_body_color = circle_body_color
        self.circle_outline_color = circle_outline_color
        self.background_color = background_color

        # Generate an information string for file naming
        self.infomation = self.get_info()

        # Create an empty RGBA image with the specified background color
        self.value = np.full(
            (self.width, self.height, 4), self.background_color, dtype=np.uint8
        )

        if use_round_shape:
            # Draw a circular region in the center of the image
            self.circle_radius = int(
                min(self.height, self.width) * circle_size_ratio // 2
            )
            circle_start_x = self.width // 2 - self.circle_radius
            circle_end_x = circle_start_x + self.circle_radius * 2
            circle_start_y = self.height // 2 - self.circle_radius
            circle_end_y = circle_start_y + self.circle_radius * 2

            # Generate the circle image with specified colors and outline thickness
            self.value[
                circle_start_x:circle_end_x, circle_start_y:circle_end_y
            ] = self.Circle(
                radius=self.circle_radius,
                outline_thickness=self.outline_thickness,
                body_color=self.circle_body_color,
                outline_color=self.circle_outline_color,
                image_slice=self.value[
                    circle_start_x:circle_end_x, circle_start_y:circle_end_y
                ],
            ).get_circle()

        # Place the logo in the center of the image
        self.logo_size = int(min(self.height, self.width) * logo_size_ratio)
        logo_start_x = (self.width - self.logo_size) // 2
        logo_end_x = logo_start_x + self.logo_size
        logo_start_y = (self.height - self.logo_size) // 2
        logo_end_y = logo_start_y + self.logo_size

        # Generate the logo image with specified colors and outline thickness
        self.value[logo_start_x:logo_end_x, logo_start_y:logo_end_y] = (
            self.Logo(
                logo_size=self.logo_size,
                outline_thickness=self.outline_thickness,
                normal_line_body_color=self.normal_line_body_color,
                normal_line_outline_color=self.normal_line_outline_color,
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

    # Nested class for generating the logo
    class Logo:
        def __init__(
            self,
            logo_size,
            outline_thickness,
            normal_line_body_color,
            normal_line_outline_color,
            single_line_body_color,
            single_line_outline_color,
            image_slice,
        ) -> None:
            """
            Initialize the Logo class for generating the Z logo.

            Parameters:
                logo_size (int): Size of the logo.
                outline_thickness (float): Thickness of the logo outlines.
                normal_line_body_color (tuple): RGBA color tuple for normal line body color.
                normal_line_outline_color (tuple): RGBA color tuple for normal line outline color.
                single_line_body_color (tuple): RGBA color tuple for single line body color.
                single_line_outline_color (tuple): RGBA color tuple for single line outline color.
                image_slice (np.array): Image slice for the logo.
            """
            self.size = logo_size
            self.tensor = image_slice
            self.unit = self.size / (6 + self.Line.standard_distance * 2)

            # Define the lines for the logo
            self.lines = [
                self.Line(
                    (-3, 0), (0, 3), normal_line_body_color, normal_line_outline_color
                ),
                self.Line(
                    (3, 0), (0, -3), normal_line_body_color, normal_line_outline_color
                ),
                self.Line(
                    (-1, 0), (0, 1), normal_line_body_color, normal_line_outline_color
                ),
                self.Line(
                    (1, 0), (0, -1), normal_line_body_color, normal_line_outline_color
                ),
                self.Line(
                    (3, 0), (-3, 0), single_line_body_color, single_line_outline_color
                ),
            ]

            # Draw the logo by iterating over all pixels
            progress_bar = tqdm(total=self.size, desc="Generating Logo")

            # Pre-calculate variables for the loop
            standard_distance2 = pow(self.Line.standard_distance * self.unit, 2)
            sqrt2_standard_distance = math.sqrt(2) * self.Line.standard_distance
            body_distance2 = pow(
                self.Line.standard_distance * self.unit - outline_thickness, 2
            )
            unit2 = pow(self.unit, 2)

            # Iterate over all pixels in the slice
            for x in range(self.size):
                for y in range(self.size):
                    # Transform the coordinates to logo coordinates
                    x_in_logo = (x - self.size / 2) / self.unit
                    y_in_logo = (y - self.size / 2) / self.unit

                    if (
                        (
                            not (
                                x_in_logo >= self.Line.standard_distance
                                and y_in_logo >= self.Line.standard_distance
                            )
                        )
                        and (
                            not (
                                x_in_logo <= -self.Line.standard_distance
                                and y_in_logo <= -self.Line.standard_distance
                            )
                        )
                        and (not (x_in_logo - y_in_logo > 3 + sqrt2_standard_distance))
                        and (not (x_in_logo - y_in_logo < -3 - sqrt2_standard_distance))
                    ):
                        for line in self.lines:
                            distance2 = (
                                line.distance2(
                                    x_in_logo,
                                    y_in_logo,
                                )
                                * unit2
                            )
                            if distance2 <= body_distance2:
                                self.tensor[x, y, :] = line.body_color
                                break
                            elif distance2 <= standard_distance2:
                                self.tensor[x, y, :] = line.outline_color
                                break
                progress_bar.update(1)
            progress_bar.close()

        # Nested class for defining the lines used in the logo
        class Line:
            standard_distance = math.sqrt(2) / 4

            def __init__(self, a, b, body_color, outline_color) -> None:
                """
                Initialize the Line class.

                Parameters:
                    a (tuple): Start point coordinates of the line.
                    b (tuple): End point coordinates of the line.
                    body_color (tuple): RGBA color tuple for line body color.
                    outline_color (tuple): RGBA color tuple for line outline color.
                """
                self.body_color = body_color
                self.outline_color = outline_color
                self.x1, self.y1 = a
                self.x2, self.y2 = b
                self.A = self.x2 - self.x1
                self.B = self.y2 - self.y1
                self.C = -self.x1 * self.A - self.y1 * self.B
                self.D = pow(self.A, 2) + pow(self.B, 2)

            def distance2(self, x, y):
                """
                Calculate the distance between a point and the line.

                Parameters:
                    x (float): X-coordinate of the point.
                    y (float): Y-coordinate of the point.

                Returns:
                    float: Distance between the point and the line.
                """
                r = (x * self.A + y * self.B + self.C) / self.D
                if r <= 0:
                    return pow(x - self.x1, 2) + pow(y - self.y1, 2)
                elif r >= 1:
                    return pow(x - self.x2, 2) + pow(y - self.y2, 2)
                else:
                    xc = self.x1 + r * self.A
                    yc = self.y1 + r * self.B
                    return pow(x - xc, 2) + pow(y - yc, 2)

        def get_logo(self):
            """
            Get the generated logo.

            Returns:
                np.array: The generated logo as a NumPy array.
            """
            return self.tensor

    # Nested class for generating the circular region used in round-shaped logos
    class Circle:
        def __init__(
            self, radius, outline_thickness, body_color, outline_color, image_slice
        ) -> None:
            """
            Initialize the Circle class for generating the circular region.

            Parameters:
                radius (int): Radius of the circle.
                outline_thickness (float): Thickness of the circle outline.
                body_color (tuple): RGBA color tuple for circle body color.
                outline_color (tuple): RGBA color tuple for circle outline color.
                image_slice (np.array): Image slice for the circle.
            """
            self.tensor = image_slice
            self.radius = radius

            # Draw the circle by iterating over all pixels
            progress_bar = tqdm(total=self.radius * 2, desc="Generating Circle")
            radius2 = pow(radius, 2)
            body_distance2 = pow(radius - outline_thickness, 2)
            for x in range(self.radius * 2):
                for y in range(self.radius * 2):
                    r2 = pow(x - radius, 2) + pow(y - radius, 2)
                    if r2 <= body_distance2:
                        self.tensor[x, y, :] = body_color
                    elif r2 <= radius2:
                        self.tensor[x, y, :] = outline_color
                progress_bar.update(1)
            progress_bar.close()

        def get_circle(self):
            """
            Get the generated circle.

            Returns:
                np.array: The generated circle as a NumPy array.
            """
            return self.tensor

    def get_image(self):
        """
        Get the final image.

        Returns:
            Image: The final image.
        """
        return self.result

    def save(self, path, format) -> None:
        """
        Save the final image to a file.
        """
        self.result.save(path, format=format)

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
            + COLOR_MAP.get(self.normal_line_body_color, "UNKNOWN")
            + "_"
            + COLOR_MAP.get(self.single_line_body_color, "UNKNOWN")
            + "_"
            + COLOR_MAP.get(self.normal_line_outline_color, "UNKNOWN")
            + "_"
            + COLOR_MAP.get(self.single_line_outline_color, "UNKNOWN")
        )
        return image_info
