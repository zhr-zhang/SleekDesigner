from abc import ABC, abstractmethod
from typing import Self

import numpy as np
from numpy.typing import NDArray

from sleek_designer.types import Color


class Figure(ABC):
    """A base class for geometric figures."""

    def __init__(self, color: Color, distance: float = 1.0) -> None:
        self.color = color
        self.distance = distance

    @abstractmethod
    def distance2(
        self, xp: NDArray[np.float64], yp: NDArray[np.float64]
    ) -> NDArray[np.float64]:
        """Squared distance from points (xp, yp) to the figure."""
        ...

    def is_inside(
        self, xp: NDArray[np.float64], yp: NDArray[np.float64]
    ) -> NDArray[np.bool_]:
        """Whether points (xp, yp) are inside the figure's distance threshold."""
        return self.distance2(xp, yp) <= self.distance**2

    @abstractmethod
    def rotate(self, degree: float) -> Self:
        """Rotate the figure by a given angle (in degrees)."""
        ...
