from utils import *
from pattern import Pattern


class Logo(Pattern):
    def __init__(
        self,
        size=2 + 12 * math.sqrt(2),
        single_color=RED,
        outer_color=WHITE,
        inner_color=WHITE,
        blackground_color=BLACK,
    ):
        super().__init__(
            size=size,
            background_color=blackground_color,
        )
        self.single_color = single_color
        self.outer_color = outer_color
        self.inner_color = inner_color
        self.blackground_color = blackground_color

        self.figures = [
            Line(
                a=(-6, 6),
                b=(6, 6),
                color=outer_color,
            ),
            Line(
                a=(-6, -6),
                b=(6, -6),
                color=outer_color,
            ),
            Line(
                a=(-2, 2),
                b=(2, 2),
                color=inner_color,
            ),
            Line(
                a=(-2, -2),
                b=(2, -2),
                color=inner_color,
            ),
            Line(
                a=(6, 6),
                b=(-6, -6),
                color=single_color,
            ),
        ]

    def get_info(self):
        """
        Get information about the logo image for file naming.

        Returns:
            str: Information string for file naming.
        """
        image_info = (
            COLOR_MAP.get(self.outer_color, "UNKNOWN")
            + "_"
            + COLOR_MAP.get(self.inner_color, "UNKNOWN")
            + "_"
            + COLOR_MAP.get(self.inner_color, "UNKNOWN")
            + "_"
            + COLOR_MAP.get(self.single_color, "UNKNOWN")
        )
        return image_info
