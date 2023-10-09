import math


class Figure:
    STANDARD_DISTANCE = 1

    def __init__(self, body_color, outline_color):
        self.body_color = body_color
        self.outline_color = outline_color

    def distance2(self, xp, yp):
        pass


class Line(Figure):
    """
    A nested class for defining the lines used in the Z logo.
    """

    def __init__(self, a, b, body_color, outline_color) -> None:
        """
        Initialize the Line class.
        """
        super().__init__(body_color, outline_color)
        self.x1, self.y1 = a
        self.x2, self.y2 = b
        self.A = self.x2 - self.x1
        self.B = self.y2 - self.y1
        self.C = -self.x1 * self.A - self.y1 * self.B
        self.D = pow(self.A, 2) + pow(self.B, 2)

    def distance2(self, xp, yp):
        """
        Calculate the square of the distance between a point and the line.
        """
        r = (xp * self.A + yp * self.B + self.C) / self.D
        if r <= 0:
            return pow(xp - self.x1, 2) + pow(yp - self.y1, 2)
        elif r >= 1:
            return pow(xp - self.x2, 2) + pow(yp - self.y2, 2)
        else:
            xc = self.x1 + r * self.A
            yc = self.y1 + r * self.B
            return pow(xp - xc, 2) + pow(yp - yc, 2)


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
