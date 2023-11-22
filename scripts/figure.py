import math
import numpy as np


class Figure:
    def __init__(
        self,
        color: (np.uint8, np.uint8, np.uint8, np.uint8),
        distance: float = 1,
    ):
        self.color = color
        self.distance = distance

    def distance2(self, xp: float, yp: float):
        pass

    def is_inside(self, xp: float, yp: float):
        distance_2 = self.distance2(xp, yp)
        if distance_2 <= pow(self.distance, 2):
            return True
        return False


class Line(Figure):
    def __init__(
        self,
        a: (float, float),
        b: (float, float),
        color: (np.uint8, np.uint8, np.uint8, np.uint8),
        distance: float = 1,
    ) -> None:
        super().__init__(color=color, distance=distance)
        self.x1, self.y1 = a
        self.x2, self.y2 = b
        self.A = self.x2 - self.x1
        self.B = self.y2 - self.y1
        self.C = -self.x1 * self.A - self.y1 * self.B
        self.D = pow(self.A, 2) + pow(self.B, 2)

    def distance2(self, xp: float, yp: float):
        r = (xp * self.A + yp * self.B + self.C) / self.D
        if r <= 0:
            return pow(xp - self.x1, 2) + pow(yp - self.y1, 2)
        elif r >= 1:
            return pow(xp - self.x2, 2) + pow(yp - self.y2, 2)
        xc = self.x1 + r * self.A
        yc = self.y1 + r * self.B
        return pow(xp - xc, 2) + pow(yp - yc, 2)


class Arc(Figure):
    def __init__(
        self,
        center: (float, float),
        a: (float, float),
        b: (float, float),
        color: (np.uint8, np.uint8, np.uint8, np.uint8),
        distance: float = 1,
    ):
        super().__init__(color=color, distance=distance)
        self.x0, self.y0 = center
        self.xa, self.ya = a
        self.xb, self.yb = b
        self.x1 = self.xa - self.x0
        self.y1 = self.ya - self.y0
        self.x2 = self.xb - self.x0
        self.y2 = self.yb - self.y0
        self.radius = math.sqrt((self.x1 - self.x0) ** 2 + (self.y1 - self.y0) ** 2)
        # direction: clockwize > 0
        self.direction = self.x1 * self.y2 - self.x2 * self.y1

    def distance2(self, xp: float, yp: float):
        xp -= self.x0
        yp -= self.y0
        # OP-> = m * OA-> + n * OB->
        m = (xp * self.y2 - self.x2 * yp) / (self.x1 * self.y2 - self.x2 * self.y1)
        n = (xp * self.y1 - self.x1 * yp) / (self.x2 * self.y1 - self.x1 * self.y2)
        if self.direction == 0:
            # TODO
            return 0
        if self.direction > 0:
            if m >= 0 and n >= 0:
                return (math.sqrt(xp**2 + yp**2) - self.radius) ** 2
            if m >= n:
                return (self.x1 - xp) ** 2 + (self.y1 - yp) ** 2
            return (self.x2 - xp) ** 2 + (self.y2 - yp) ** 2

        if m >= 0 and n >= 0:
            if m >= n:
                return (self.x1 - xp) ** 2 + (self.y1 - yp) ** 2
            return (self.x2 - xp) ** 2 + (self.y2 - yp) ** 2
        return (math.sqrt(xp**2 + yp**2) - self.radius) ** 2


class Dot(Figure):
    def __init__(
        self,
        position: (float, float),
        color: (np.uint8, np.uint8, np.uint8, np.uint8),
        distance: float = 1,
    ):
        super().__init__(color=color, distance=distance)
        self.x, self.y = position

    def distance2(self, xp: float, yp: float):
        return (self.x - xp) ** 2 + (self.y - yp) ** 2
