import math
from tqdm import tqdm
from line import Line


class Logo:
    """
    A nested class for generating the Z logo.

    Attributes:
        size (int): Size of the logo.
        tensor (np.array): NumPy array representing the logo image.
        unit (float): Unit for scaling logo coordinates.
        lines (list): List of Line objects defining the logo's lines.
    """

    def __init__(
        self,
        logo_size,
        outline_thickness,
        outside_line_body_color,
        outside_line_outline_color,
        inside_line_body_color,
        inside_line_outline_color,
        single_line_body_color,
        single_line_outline_color,
        image_slice,
    ) -> None:
        """
        Initialize the Logo class for generating the Z logo.

        Parameters:
            logo_size (int): Size of the logo.
            outline_thickness (float): Thickness of the logo outline.
            outside_line_body_color (tuple): RGBA color tuple for the body color of outside lines.
            outside_line_outline_color (tuple): RGBA color tuple for the outline color of outside lines.
            inside_line_body_color (tuple): RGBA color tuple for the body color of inside lines.
            inside_line_outline_color (tuple): RGBA color tuple for the outline color of inside lines.
            single_line_body_color (tuple): RGBA color tuple for the body color of single line.
            single_line_outline_color (tuple): RGBA color tuple for the outline color of single line.
            image_slice (np.array): Image slice for the logo.
        """
        self.size = logo_size
        self.tensor = image_slice
        self.unit = self.size / (6 + Line.standard_distance * 2)

        # Define the lines for the logo
        self.lines = [
            Line((-3, 0), (0, 3), outside_line_body_color, outside_line_outline_color),
            Line((3, 0), (0, -3), outside_line_body_color, outside_line_outline_color),
            Line((-1, 0), (0, 1), inside_line_body_color, inside_line_outline_color),
            Line((1, 0), (0, -1), inside_line_body_color, inside_line_outline_color),
            Line((3, 0), (-3, 0), single_line_body_color, single_line_outline_color),
        ]

        # Draw the logo by iterating over all pixels
        progress_bar = tqdm(total=self.size, desc="Generating Logo")

        # Pre-calculate variables for the loop
        standard_distance2 = pow(Line.standard_distance * self.unit, 2)
        sqrt2_standard_distance = math.sqrt(2) * Line.standard_distance
        body_distance2 = pow(Line.standard_distance * self.unit - outline_thickness, 2)
        # Calculate the square of the distance between the center of the logo and the point
        unit2 = pow(self.unit, 2)
        # Iterate through each point in the logo
        for x in range(self.size):
            for y in range(self.size):
                # Calculate the distance between the point and the center of the logo
                x_in_logo = (x - self.size / 2) / self.unit
                y_in_logo = (y - self.size / 2) / self.unit
                # Check if the point is within the standard distance of the logo
                if (
                    (
                        not (
                            x_in_logo >= Line.standard_distance
                            and y_in_logo >= Line.standard_distance
                        )
                    )
                    and (
                        not (
                            x_in_logo <= -Line.standard_distance
                            and y_in_logo <= -Line.standard_distance
                        )
                    )
                    and (not (x_in_logo - y_in_logo > 3 + sqrt2_standard_distance))
                    and (not (x_in_logo - y_in_logo < -3 - sqrt2_standard_distance))
                ):
                    # Iterate through each line in the logo
                    for line in self.lines:
                        # Calculate the square of the distance between the point and the line
                        distance2 = (
                            line.distance2(
                                x_in_logo,
                                y_in_logo,
                            )
                            * unit2
                        )
                        # Check if the square of the distance is less than the body distance
                        if distance2 <= body_distance2:
                            # Set the color of the point to the body color of the line
                            self.tensor[x, y, :] = line.body_color
                            break
                        # Check if the square of the distance is less than the standard distance
                        elif distance2 <= standard_distance2:
                            # Set the color of the point to the outline color of the line
                            self.tensor[x, y, :] = line.outline_color
                            break
            # Update the progress bar
            progress_bar.update(1)
        # Close the progress bar
        progress_bar.close()

    def get_logo(self):
        """
        Get the generated logo.

        Returns:
            np.array: The generated logo as a NumPy array.
        """
        return self.tensor
