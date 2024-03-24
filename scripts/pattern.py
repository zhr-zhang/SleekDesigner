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

    def generate(
        self,
        width=1024,
        height=1024,
        ratio=0.7,
    ) -> np.ndarray:
        image_ratio = width / height
        if image_ratio > self.canvas_ratio:
            canvas_height = int(height * ratio)
            canvas_width = int(canvas_height * self.canvas_ratio)
        else:
            canvas_width = int(width * ratio)
            canvas_height = int(canvas_width / self.canvas_ratio)
        self.value = np.full((width, height, 4), self.background_color, dtype=np.uint8)
        logo_slice = np.full(
            (canvas_width, canvas_height, 4), self.background_color, dtype=np.uint8
        )

        unit = canvas_width / self.grids_x
        half_width = canvas_width / 2
        half_height = canvas_height / 2
        for x in range(canvas_width):
            for y in range(canvas_height):
                m = (x - half_width) / unit
                n = (y - half_height) / unit
                for figure in self.figures:
                    if figure.is_inside(m, n):
                        logo_slice[x, y, :] = figure.color
                        break

        self.value[
            (width - canvas_width) // 2 : (width + canvas_width) // 2,
            (height - canvas_height) // 2 : (height + canvas_height) // 2,
        ] = logo_slice
        self.value = np.rot90(self.value)

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
