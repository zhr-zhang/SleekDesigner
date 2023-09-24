from figure import Figure
import math


class Arc(Figure):
    def __init__(self, center, a, b, body_color, outline_color):
        super().__init__(body_color, outline_color)
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

    def distance2(self, xp, yp):
        xp -= self.x0
        yp -= self.y0
        # -OP> = m * -OA> + n * -OB>
        m = (xp * self.y2 - self.x2 * yp) / (self.x1 * self.y2 - self.x2 * self.y1)
        n = (xp * self.y1 - self.x1 * yp) / (self.x2 * self.y1 - self.x1 * self.y2)
        if self.direction == 0:
            print("an arc can't have an angle of 180 or 0")
            distance2 = 0
        elif self.direction > 0:
            if m >= 0 and n >= 0:
                distance2 = (math.sqrt(xp**2 + yp**2) - self.radius) ** 2
            elif m >= n:
                distance2 = (self.x1 - xp) ** 2 + (self.y1 - yp) ** 2
            else:
                distance2 = (self.x2 - xp) ** 2 + (self.y2 - yp) ** 2
        else:
            if m >= 0 and n >= 0:
                if m >= n:
                    distance2 = (self.x1 - xp) ** 2 + (self.y1 - yp) ** 2
                else:
                    distance2 = (self.x2 - xp) ** 2 + (self.y2 - yp) ** 2
            else:
                distance2 = (math.sqrt(xp**2 + yp**2) - self.radius) ** 2
        return distance2
