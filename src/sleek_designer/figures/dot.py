from typing import Self

import numpy as np
from numpy.typing import NDArray

from sleek_designer.figures.base import Figure
from sleek_designer.point import Point
from sleek_designer.types import Color


class Dot(Figure):
    """A dot, essentially a point in space."""

    def __init__(
        self,
        position: Point,
        color: Color,
        distance: float = 1.0,
    ) -> None:
        super().__init__(color=color, distance=distance)
        self.position = position

    def distance2(
        self, xp: NDArray[np.float64], yp: NDArray[np.float64]
    ) -> NDArray[np.float64]:
        return (self.position.x - xp) ** 2 + (self.position.y - yp) ** 2

    def rotate(self, degree: float) -> Self:
        return self.__class__(
            position=self.position.rotate(degree),
            color=self.color,
            distance=self.distance,
        )
