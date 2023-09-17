import math
from tqdm import tqdm
from line import Line
from stripe import Stripe


class Logo:
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
        self.size = logo_size
        self.tensor = image_slice
        self.unit = self.size / 14

        # Define the lines for the logo
        self.lines = [
            Line((-6, 6), (6, 6), outside_line_body_color, outside_line_outline_color),
            Line(
                (-6, -6), (6, -6), outside_line_body_color, outside_line_outline_color
            ),
            Line((-2, 2), (2, 2), inside_line_body_color, inside_line_outline_color),
            Line((-2, -2), (2, -2), inside_line_body_color, inside_line_outline_color),
            Line((6, 6), (-6, -6), single_line_body_color, single_line_outline_color),
        ]

        # Draw the logo by iterating over all pixels
        progress_bar = tqdm(total=self.size, desc="Generating Logo")

        # Pre-calculate variables for the loop
        standard_distance2 = pow(Stripe.STANDARD_DISTANCE * self.unit, 2)
        sqrt2_standard_distance = math.sqrt(2) * Stripe.STANDARD_DISTANCE
        body_distance2 = pow(
            Stripe.STANDARD_DISTANCE * self.unit - outline_thickness, 2
        )
        # Calculate the square of the distance between the center of the logo and the point
        unit2 = pow(self.unit, 2)
        # Iterate through each point in the logo
        for x in range(self.size):
            for y in range(self.size):
                # Calculate the distance between the point and the center of the logo
                x_in_logo = (x - self.size / 2) / self.unit
                y_in_logo = (y - self.size / 2) / self.unit
                # Check if the point is within the standard distance of the logo
                # Iterate through each line in the logo
                for line in self.lines:
                    # Calculate the square of the distance between the point and the line
                    distance2 = line.distance2(x_in_logo, y_in_logo) * unit2
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
        return self.tensor
