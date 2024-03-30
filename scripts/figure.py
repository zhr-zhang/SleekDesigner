import math
import numpy as np
from typing import Tuple
from abc import ABC, abstractmethod
from point import Point


Color = Tuple[np.uint8, np.uint8, np.uint8, np.uint8]


class Figure(ABC):
    """A base class for geometric figures, representing basic properties and methods."""

    def __init__(self, color: Color, distance: float = 1.0) -> None:
        self.color = color
        self.distance = distance

    @abstractmethod
    def distance2(self, xp: float, yp: float) -> float:
        """Calculates the squared distance from a point (xp, yp) to the figure.
        To be implemented by subclasses."""
        raise NotImplementedError

    def is_inside(self, xp: float, yp: float) -> bool:
        """Determines if a point (xp, yp) is inside the figure based on a distance threshold."""
        return self.distance2(xp, yp) <= self.distance**2

    @abstractmethod
    def rotate(self, degree: float):
        """Rotates the figure by a given angle (in degrees)."""
        raise NotImplementedError


class Line(Figure):
    """A class representing a line segment defined by two points."""

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
        self.A = b.x - a.x
        self.B = b.y - a.y
        self.C = -a.x * self.A - a.y * self.B
        self.D = self.A**2 + self.B**2

    def distance2(self, xp: np.ndarray, yp: np.ndarray) -> np.ndarray:
        r = (xp * self.A + yp * self.B + self.C) / self.D
        condition1 = r < 0
        condition2 = r > 1
        xc = self.a.x + r * self.A
        yc = self.a.y + r * self.B

        dist2 = np.where(
            condition1,
            (xp - self.a.x) ** 2 + (yp - self.a.y) ** 2,
            np.where(
                condition2,
                (xp - self.b.x) ** 2 + (yp - self.b.y) ** 2,
                (xp - xc) ** 2 + (yp - yc) ** 2,
            ),
        )
        return dist2

    def rotate(self, degree: float):
        new_a = self.a.rotate(degree)
        new_b = self.b.rotate(degree)
        return Line(
            a=new_a,
            b=new_b,
            color=self.color,
            distance=self.distance,
        )


class Arc(Figure):
    """A class representing an arc segment defined by its center and two boundary points."""

    def __init__(
        self,
        center: Point,
        a: Point,
        b: Point,
        color: Color,
        distance: float = 1.0,
    ):
        super().__init__(color=color, distance=distance)
        self.center = center
        self.a = a
        self.b = b
        self.radius = math.sqrt((a.x - center.x) ** 2 + (a.y - center.y) ** 2)
        self.direction = (a.x - center.x) * (b.y - center.y) - (b.x - center.x) * (
            a.y - center.y
        )

    def distance2(self, xp: np.ndarray, yp: np.ndarray) -> np.ndarray:
        xp_adj = xp - self.center.x
        yp_adj = yp - self.center.y
        m = (xp_adj * self.b.y - self.b.x * yp_adj) / (
            self.a.x * self.b.y - self.b.x * self.a.y
        )
        n = (xp_adj * self.a.y - self.a.x * yp_adj) / (
            self.b.x * self.a.y - self.a.x * self.b.y
        )

        condition1 = m >= 0
        condition2 = n >= 0
        dist_to_center = np.sqrt(xp_adj**2 + yp_adj**2) - self.radius

        dist_a = (self.a.x - xp_adj) ** 2 + (self.a.y - yp_adj) ** 2
        dist_b = (self.b.x - xp_adj) ** 2 + (self.b.y - yp_adj) ** 2

        # Handling the direction and conditions for distances
        if self.direction > 0:
            condition = np.logical_and(condition1, condition2)
            dist = np.where(
                condition, dist_to_center**2, np.where(m >= n, dist_a, dist_b)
            )
        else:
            condition = np.logical_and(condition1, condition2)
            dist = np.where(
                condition, np.where(m >= n, dist_a, dist_b), dist_to_center**2
            )

        return dist

    def rotate(self, degree: float):
        new_center = self.center.rotate(degree)
        new_a = self.a.rotate(degree)
        new_b = self.b.rotate(degree)
        return Arc(
            center=new_center,
            a=new_a,
            b=new_b,
            color=self.color,
            distance=self.distance,
        )


class Dot(Figure):
    """A class representing a dot, essentially a point in space."""

    def __init__(
        self,
        position: Point,
        color: Color,
        distance: float = 1.0,
    ) -> None:
        super().__init__(color=color, distance=distance)
        self.position = position

    def distance2(self, xp: np.ndarray, yp: np.ndarray) -> np.ndarray:
        return (self.position.x - xp) ** 2 + (self.position.y - yp) ** 2

    def rotate(self, degree: float):
        new_position = self.position.rotate(degree)
        return Dot(
            position=new_position,
            color=self.color,
            distance=self.distance,
        )
