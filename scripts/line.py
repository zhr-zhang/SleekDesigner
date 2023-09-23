from figure import Figure


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
