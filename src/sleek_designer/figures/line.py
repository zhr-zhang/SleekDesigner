from typing import Self

import numpy as np
from numpy.typing import NDArray

from sleek_designer.figures.base import Figure
from sleek_designer.point import Point
from sleek_designer.types import Color


class Line(Figure):
    """A line segment defined by two points."""

    def __init__(
        self,
        a: Point,
        b: Point,
        color: Color,
        distance: float = 1.0,
    ) -> None:
        super().__init__(color=color, distance=distance)
        self.a = a
        self.b = b
        # Direction vector (a -> b) and projection coefficients
        self.dx = b.x - a.x
        self.dy = b.y - a.y
        self.offset = -a.x * self.dx - a.y * self.dy
        self.length_sq = self.dx**2 + self.dy**2

    def distance2(
        self, xp: NDArray[np.float64], yp: NDArray[np.float64]
    ) -> NDArray[np.float64]:
        r = (xp * self.dx + yp * self.dy + self.offset) / self.length_sq
        xc = self.a.x + r * self.dx
        yc = self.a.y + r * self.dy

        dist2: NDArray[np.float64] = np.where(
            r < 0,
            (xp - self.a.x) ** 2 + (yp - self.a.y) ** 2,
            np.where(
                r > 1,
                (xp - self.b.x) ** 2 + (yp - self.b.y) ** 2,
                (xp - xc) ** 2 + (yp - yc) ** 2,
            ),
        )
        return dist2

    def rotate(self, degree: float) -> Self:
        return self.__class__(
            a=self.a.rotate(degree),
            b=self.b.rotate(degree),
            color=self.color,
            distance=self.distance,
        )
