import math
from typing import Self

import numpy as np
from numpy.typing import NDArray

from sleek_designer.figures.base import Figure
from sleek_designer.point import Point
from sleek_designer.types import Color


class Arc(Figure):
    """An arc segment defined by its center and two boundary points."""

    def __init__(
        self,
        center: Point,
        a: Point,
        b: Point,
        color: Color,
        distance: float = 1.0,
    ) -> None:
        super().__init__(color=color, distance=distance)
        self.center = center
        self.a = a
        self.b = b
        self.radius = math.sqrt((a.x - center.x) ** 2 + (a.y - center.y) ** 2)
        self.direction = (a.x - center.x) * (b.y - center.y) - (b.x - center.x) * (
            a.y - center.y
        )

    def distance2(
        self, xp: NDArray[np.float64], yp: NDArray[np.float64]
    ) -> NDArray[np.float64]:
        xp_adj = xp - self.center.x
        yp_adj = yp - self.center.y
        denom_m = self.a.x * self.b.y - self.b.x * self.a.y
        m = (xp_adj * self.b.y - self.b.x * yp_adj) / denom_m
        n = (xp_adj * self.a.y - self.a.x * yp_adj) / (-denom_m)

        dist_to_center = np.sqrt(xp_adj**2 + yp_adj**2) - self.radius
        dist_a = (self.a.x - xp_adj) ** 2 + (self.a.y - yp_adj) ** 2
        dist_b = (self.b.x - xp_adj) ** 2 + (self.b.y - yp_adj) ** 2

        condition = np.logical_and(m >= 0, n >= 0)
        if self.direction > 0:
            dist2: NDArray[np.float64] = np.where(
                condition,
                dist_to_center**2,
                np.where(m >= n, dist_a, dist_b),
            )
        else:
            dist2 = np.where(
                condition,
                np.where(m >= n, dist_a, dist_b),
                dist_to_center**2,
            )
        return dist2

    def rotate(self, degree: float) -> Self:
        return self.__class__(
            center=self.center.rotate(degree),
            a=self.a.rotate(degree),
            b=self.b.rotate(degree),
            color=self.color,
            distance=self.distance,
        )
