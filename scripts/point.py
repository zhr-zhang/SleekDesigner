import math


class Point:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def rotate(self, degree: float) -> "Point":
        radian = math.radians(degree)
        new_x = self.x * math.cos(radian) - self.y * math.sin(radian)
        new_y = self.x * math.sin(radian) + self.y * math.cos(radian)
        return Point(new_x, new_y)
