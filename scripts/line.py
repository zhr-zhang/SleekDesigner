import math
# Nested class for defining the lines used in the logo
class Line:
    """
    A nested class for defining the lines used in the Z logo.

    Attributes:
        body_color (tuple): RGBA color tuple for line body color.
        outline_color (tuple): RGBA color tuple for line outline color.
            x1 (float): X-coordinate of the start point of the line.
            y1 (float): Y-coordinate of the start point of the line.
            x2 (float): X-coordinate of the end point of the line.
            y2 (float): Y-coordinate of the end point of the line.
            A (float): Difference between x2 and x1.
            B (float): Difference between y2 and y1.
            C (float): Constant term for the line equation.
            D (float): Sum of squares of A and B.
    """

    standard_distance = math.sqrt(2) / 4

    def __init__(self, a, b, body_color, outline_color) -> None:
        """
        Initialize the Line class.

        Parameters:
            a (tuple): Start point coordinates of the line.
            b (tuple): End point coordinates of the line.
            body_color (tuple): RGBA color tuple for line body color.
            outline_color (tuple): RGBA color tuple for line outline color.
        """
        self.body_color = body_color
        self.outline_color = outline_color
        self.x1, self.y1 = a
        self.x2, self.y2 = b
        self.A = self.x2 - self.x1
        self.B = self.y2 - self.y1
        self.C = -self.x1 * self.A - self.y1 * self.B
        self.D = pow(self.A, 2) + pow(self.B, 2)

    def distance2(self, x, y):
        """
        Calculate the square of the distance between a point and the line.

        Parameters:
            x (float): X-coordinate of the point.
            y (float): Y-coordinate of the point.

        Returns:
            float: Square of the distance between the point and the line.
        """
        r = (x * self.A + y * self.B + self.C) / self.D
        if r <= 0:
            return pow(x - self.x1, 2) + pow(y - self.y1, 2)
        elif r >= 1:
            return pow(x - self.x2, 2) + pow(y - self.y2, 2)
        else:
            xc = self.x1 + r * self.A
            yc = self.y1 + r * self.B
            return pow(x - xc, 2) + pow(y - yc, 2)

