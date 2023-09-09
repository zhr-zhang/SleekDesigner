from tqdm import tqdm


class Circle:
    def __init__(
        self, radius, outline_thickness, body_color, outline_color, image_slice
    ) -> None:
        """
        Initialize the Circle class for generating the circular region.

        Parameters:
            radius (int): Radius of the circle.
            outline_thickness (float): Thickness of the circle outline.
            body_color (tuple): RGBA color tuple for circle body color.
            outline_color (tuple): RGBA color tuple for circle outline color.
            image_slice (np.array): Image slice for the circle.
        """
        self.tensor = image_slice
        self.radius = radius

        # Draw the circle by iterating over all pixels
        progress_bar = tqdm(total=self.radius * 2, desc="Generating Circle")
        radius2 = pow(radius, 2)
        body_distance2 = pow(radius - outline_thickness, 2)
        for x in range(self.radius * 2):
            for y in range(self.radius * 2):
                r2 = pow(x - radius, 2) + pow(y - radius, 2)
                if r2 <= body_distance2:
                    self.tensor[x, y, :] = body_color
                elif r2 <= radius2:
                    self.tensor[x, y, :] = outline_color
            progress_bar.update(1)
        progress_bar.close()

    def get_circle(self):
        """
        Get the generated circle.

        Returns:
            np.array: The generated circle as a NumPy array.
        """
        return self.tensor
