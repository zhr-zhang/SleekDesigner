import math
from line import Line
from figure import Figure
from arc import Arc


class Logo:
    def __init__(
        self,
        logo_size,
        angle_degrees,
        outline_thickness,
        outside_line_body_color,
        outside_line_outline_color,
        inside_line_body_color,
        inside_line_outline_color,
        single_line_body_color,
        single_line_outline_color,
        arc_body_color,
        arc_outline_color,
        image_slice,
    ) -> None:
        self.size = logo_size
        self.tensor = image_slice
        self.unit = self.size / (4 * math.sqrt(34) + 2)
        angle=angle_degrees*math.pi/180

        # Define the figures for the logo
        self.figures = [
            Line(
                a=(-6, 6),
                b=(6, 6),
                body_color=outside_line_body_color,
                outline_color=outside_line_outline_color,
            ),
            Line(
                a=(-6, -6),
                b=(6, -6),
                body_color=outside_line_body_color,
                outline_color=outside_line_outline_color,
            ),
            Line(
                a=(-2, 2),
                b=(2, 2),
                body_color=inside_line_body_color,
                outline_color=inside_line_outline_color,
            ),
            Line(
                a=(-2, -2),
                b=(2, -2),
                body_color=inside_line_body_color,
                outline_color=inside_line_outline_color,
            ),
            Line(
                a=(6, 6),
                b=(-6, -6),
                body_color=single_line_body_color,
                outline_color=single_line_outline_color,
            ),
            Arc(
                center=(0, 0),
                a=(10, -6),
                b=(10, 6),
                body_color=arc_body_color,
                outline_color=arc_outline_color,
            ),
            Arc(
                center=(0, 0),
                a=(-10, 6),
                b=(-10, -6),
                body_color=arc_body_color,
                outline_color=arc_outline_color,
            ),
            Arc(
                center=(0, 0),
                a=(6, 10),
                b=(-6, 10),
                body_color=arc_body_color,
                outline_color=arc_outline_color,
            ),
            Arc(
                center=(0, 0),
                a=(-6, -10),
                b=(6, -10),
                body_color=arc_body_color,
                outline_color=arc_outline_color,
            ),
        ]

        standard_distance2 = pow(Figure.STANDARD_DISTANCE * self.unit, 2)
        body_distance2 = pow(
            Figure.STANDARD_DISTANCE * self.unit - outline_thickness, 2
        )
        unit2 = pow(self.unit, 2)
        for x in range(self.size):
            for y in range(self.size):
                m = (x - self.size / 2) / self.unit
                n = (y - self.size / 2) / self.unit
                x_in_logo = m * math.cos(angle) + n * math.sin(angle)
                y_in_logo = -m * math.sin(angle) + n * math.cos(angle)
                for figure in self.figures:
                    distance2 = figure.distance2(x_in_logo, y_in_logo) * unit2
                    if distance2 <= body_distance2:
                        self.tensor[x, y, :] = figure.body_color
                        break
                    elif distance2 <= standard_distance2:
                        self.tensor[x, y, :] = figure.outline_color
                        break

    def get_logo(self):
        return self.tensor
