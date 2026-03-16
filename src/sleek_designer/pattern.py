from pathlib import Path

import numpy as np
from numpy.typing import NDArray
from PIL import Image

from sleek_designer.color import BLACK
from sleek_designer.figures.base import Figure
from sleek_designer.types import Color


class Pattern:

    def __init__(
        self,
        figures: list[Figure] | None = None,
        grids_x: float = 10,
        grids_y: float = 10,
        background_color: Color = BLACK,
        name: str = "pattern",
    ) -> None:
        self.figures = figures if figures is not None else []
        self.grids_x = grids_x
        self.grids_y = grids_y
        self.background_color = background_color
        self.name = name
        self.canvas_ratio = self.grids_x / self.grids_y

    def rotate(self, degree: float) -> "Pattern":
        new_figures = [f.rotate(degree) for f in self.figures]
        return Pattern(
            figures=new_figures,
            grids_x=self.grids_x,
            grids_y=self.grids_y,
            background_color=self.background_color,
            name=self.name,
        )

    def generate(
        self,
        width: int = 1024,
        height: int = 1024,
        ratio: float = 0.7,
    ) -> NDArray[np.uint8]:
        image_ratio = width / height
        if image_ratio > self.canvas_ratio:
            canvas_height = int(height * ratio)
            canvas_width = int(canvas_height * self.canvas_ratio)
        else:
            canvas_width = int(width * ratio)
            canvas_height = int(canvas_width / self.canvas_ratio)

        xs, ys = np.meshgrid(
            np.linspace(-self.grids_x / 2, self.grids_x / 2, canvas_width),
            np.linspace(-self.grids_y / 2, self.grids_y / 2, canvas_height),
        )

        image_array: NDArray[np.uint8] = np.full(
            (height, width, 4), self.background_color, dtype=np.uint8
        )
        y_start = (height - canvas_height) // 2
        y_end = (height + canvas_height) // 2
        x_start = (width - canvas_width) // 2
        x_end = (width + canvas_width) // 2
        for figure in self.figures:
            mask = figure.is_inside(xs, ys)
            image_array[y_start:y_end, x_start:x_end][mask] = figure.color
        return np.flipud(image_array)

    def save_image(
        self,
        width: int = 1024,
        height: int = 1024,
        ratio: float = 0.7,
        path: Path | str = "my_image.png",
        format: str = "png",
    ) -> None:
        p = Path(path)
        p.parent.mkdir(parents=True, exist_ok=True)
        Image.fromarray(
            self.generate(width=width, height=height, ratio=ratio),
            "RGBA",
        ).save(p, format=format)
