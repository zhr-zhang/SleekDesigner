from utils import *
from pattern import Pattern


class Logo(Pattern):
    def __init__(
        self,
        single_color=RED,
        outer_color=WHITE,
        inner_color=WHITE,
        background_color=BLACK,
    ):
        super().__init__(
            background_color=background_color,
        )
        self.single_color = single_color
        self.outer_color = outer_color
        self.inner_color = inner_color

        self.figures = [
            Line(a=(-6, 6), b=(6, 6), color=outer_color),
            Line(a=(-6, -6), b=(6, -6), color=outer_color),
            Line(a=(-2, 2), b=(2, 2), color=inner_color),
            Line(a=(-2, -2), b=(2, -2), color=inner_color),
            Line(a=(6, 6), b=(-6, -6), color=single_color),
        ]

    def generate_image(self, width=1920, height=1080, ratio=0.5, angle_degrees=45):
        return super().generate_image(width, height, ratio, angle_degrees)


logos = [
    Logo(
        single_color=RED,
        outer_color=LIGHT,
        inner_color=LIGHT,
        background_color=BLACK,
    ),
    Logo(
        single_color=BLUE,
        outer_color=LIGHT,
        inner_color=LIGHT,
        background_color=BLACK,
    ),
    Logo(
        single_color=YELLOW,
        outer_color=LIGHT,
        inner_color=LIGHT,
        background_color=BLACK,
    ),
    Logo(
        single_color=LIGHT,
        outer_color=RED,
        inner_color=RED,
        background_color=BLACK,
    ),
    Logo(
        single_color=LIGHT,
        outer_color=BLUE,
        inner_color=BLUE,
        background_color=BLACK,
    ),
    Logo(
        single_color=LIGHT,
        outer_color=YELLOW,
        inner_color=YELLOW,
        background_color=BLACK,
    ),
    Logo(
        single_color=RED,
        outer_color=DARK,
        inner_color=DARK,
        background_color=WHITE,
    ),
    Logo(
        single_color=BLUE,
        outer_color=DARK,
        inner_color=DARK,
        background_color=WHITE,
    ),
    Logo(
        single_color=YELLOW,
        outer_color=DARK,
        inner_color=DARK,
        background_color=WHITE,
    ),
    Logo(
        single_color=DARK,
        outer_color=RED,
        inner_color=RED,
        background_color=WHITE,
    ),
    Logo(
        single_color=DARK,
        outer_color=BLUE,
        inner_color=BLUE,
        background_color=WHITE,
    ),
    Logo(
        single_color=DARK,
        outer_color=YELLOW,
        inner_color=YELLOW,
        background_color=WHITE,
    ),
]
