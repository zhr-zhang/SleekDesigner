import math
from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Point:
    x: float
    y: float

    def rotate(self, degree: float) -> "Point":
        radian = math.radians(degree)
        new_x = self.x * math.cos(radian) - self.y * math.sin(radian)
        new_y = self.x * math.sin(radian) + self.y * math.cos(radian)
        return Point(new_x, new_y)
