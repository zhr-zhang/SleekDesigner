import numpy as np
import os
from PIL import Image
from color import *
from figure import *


class Pattern:

    def __init__(
        self,
        figures: list[Figure] = None,
        grids_x: int = 10,
        grids_y: int = 10,
        background_color: Color = BLACK,
        name: str = "pattern",
    ) -> None:
        if figures is None:
            figures = [Line(a=(0, -3), b=(0, 3), color=RED)]
        self.figures = figures
        self.grids_x = grids_x
        self.grids_y = grids_y
        self.background_color = background_color
        self.name = name
        self.canvas_ratio = self.grids_x / self.grids_y

    def rotate(self, degree) -> "Pattern":
        new_figures = []
        for figure in self.figures:
            new_figures.append(figure.rotate(degree))
        return Pattern(
            figures=new_figures,
            grids_x=self.grids_x,
            grids_y=self.grids_y,
            background_color=self.background_color,
            name=self.name,
        )

    def generate(self, width=1024, height=1024, ratio=0.7) -> np.ndarray:
        image_ratio = width / height
        if image_ratio > self.canvas_ratio:
            canvas_height = int(height * ratio)
            canvas_width = int(canvas_height * self.canvas_ratio)
        else:
            canvas_width = int(width * ratio)
            canvas_height = int(canvas_width / self.canvas_ratio)

        # Create a full background canvas
        self.value = np.full((height, width, 4), self.background_color, dtype=np.uint8)

        # Generate a meshgrid for x and y coordinates
        xs, ys = np.meshgrid(
            np.linspace(-self.grids_x / 2, self.grids_x / 2, canvas_width),
            np.linspace(-self.grids_y / 2, self.grids_y / 2, canvas_height),
        )

        # Check for each figure if the points are inside, vectorized
        for figure in self.figures:
            mask = figure.is_inside(xs, ys)
            self.value[
                (height - canvas_height) // 2 : (height + canvas_height) // 2,
                (width - canvas_width) // 2 : (width + canvas_width) // 2,
            ][mask] = figure.color

        self.value = np.flipud(self.value)
        return self.value

    def save_image(
        self,
        width=1024,
        height=1024,
        ratio=0.7,
        path: str = "my_image.png",
        format: str = "png",
    ) -> None:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        Image.fromarray(
            self.generate(
                width=width,
                height=height,
                ratio=ratio,
            ),
            "RGBA",
        ).save(path, format=format)
