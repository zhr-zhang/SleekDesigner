import math
import numpy as np
from typing import Tuple

Color = Tuple[np.uint8, np.uint8, np.uint8, np.uint8]
Position = Tuple[float, float]


class Figure:
    """A base class for geometric figures, representing basic properties and methods."""

    def __init__(self, color: Color, distance: float = 1.0) -> None:
        self.color = color
        self.distance = distance

    def distance2(self, xp: float, yp: float) -> float:
        """Calculates the squared distance from a point (xp, yp) to the figure.
        To be implemented by subclasses."""
        raise NotImplementedError

    def is_inside(self, xp: float, yp: float) -> bool:
        """Determines if a point (xp, yp) is inside the figure based on a distance threshold."""
        return self.distance2(xp, yp) <= self.distance**2


class Line(Figure):
    """A class representing a line segment defined by two points."""

    def __init__(
        self, a: Position, b: Position, color: Color, distance: float = 1.0
    ) -> None:
        super().__init__(color=color, distance=distance)
        self.a = a
        self.b = b
        self.A = b[0] - a[0]
        self.B = b[1] - a[1]
        self.C = -a[0] * self.A - a[1] * self.B
        self.D = self.A**2 + self.B**2

    def distance2(self, xp: float, yp: float) -> float:
        """Calculates the squared distance from a point (xp, yp) to the line segment."""
        r = (xp * self.A + yp * self.B + self.C) / self.D
        if r < 0:
            return (xp - self.a[0]) ** 2 + (yp - self.a[1]) ** 2
        elif r > 1:
            return (xp - self.b[0]) ** 2 + (yp - self.b[1]) ** 2
        xc = self.a[0] + r * self.A
        yc = self.a[1] + r * self.B
        return (xp - xc) ** 2 + (yp - yc) ** 2


class Arc(Figure):
    """A class representing an arc segment defined by its center and two boundary points."""

    def __init__(
        self,
        center: Position,
        a: Position,
        b: Position,
        color: Color,
        distance: float = 1.0,
    ):
        super().__init__(color=color, distance=distance)
        self.center = center
        self.a = a
        self.b = b
        self.radius = math.sqrt((a[0] - center[0]) ** 2 + (a[1] - center[1]) ** 2)
        self.direction = (a[0] - center[0]) * (b[1] - center[1]) - (
            b[0] - center[0]
        ) * (a[1] - center[1])

    def distance2(self, xp: float, yp: float) -> float:
        """Calculates the squared distance from a point (xp, yp) to the arc.
        The implementation depends on the arc's specifics and the position of the point.
        """
        # This method needs a proper implementation based on the arc's geometry.
        # Placeholder implementation:
        return 0.0


class Dot(Figure):
    """A class representing a dot, essentially a point in space."""

    def __init__(self, position: Position, color: Color, distance: float = 1.0) -> None:
        super().__init__(color=color, distance=distance)
        self.position = position

    def distance2(self, xp: float, yp: float) -> float:
        """Calculates the squared distance from a point (xp, yp) to the dot."""
        return (self.position[0] - xp) ** 2 + (self.position[1] - yp) ** 2
