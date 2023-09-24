from utils import *
from image import LogoImage

class BaseBatchGenerator:
    def __init__(
        self,
        logo_size_ratio=0.7,
        image_shape="wide",
        save_format="PNG",
        power_range=range(3),
        min_width=128,
        min_height=128,
    ):
        self.logo_size_ratio = logo_size_ratio
        self.image_shape = image_shape
        self.save_format = save_format
        self.power_range = power_range
        self.min_width = min_width
        self.min_height = min_height

    def generate(
        self,
        draw=True,
        show=False,
        save=False,
        save_cfg=False,
    ):
        pass


class DefaultBatchGenerator(BaseBatchGenerator):
    def __init__(
        self,
        logo_size_ratio=0.7,
        image_shape="wide",
        save_format="PNG",
        power_range=range(3),
        min_width=128,
        min_height=128,
        angle_degrees=45,
    ):
        super().__init__(
            logo_size_ratio,
            image_shape,
            save_format,
            power_range,
            min_width,
            min_height,
        )
        self.angle_degrees = angle_degrees

    def generate(
        self,
        draw=True,
        show=False,
        save=False,
        save_cfg=False,
    ):
        # Generate logo images for diffetent sizes and shapes
        for power in self.power_range:
            width = self.min_width * pow(2, power)
            height = self.min_height * pow(2, power)

            # Generate logo images for different background colors
            for background_color in BACKGROUND_COLORS:
                # corner_color = TRANSPARENT
                history_colors = []
                # Create a directory to save images with different sizes and shapes

                save_folder = os.path.join(
                    output_folder,
                    # "test",
                    self.image_shape,
                    COLOR_MAP.get(background_color, "unknown"),
                    str(width),
                )
                os.makedirs(save_folder, exist_ok=True)

                # Generate logo images for different theme colors
                for theme_color in THEME_COLORS:
                    line_colors = [theme_color, LIGHT, DARK]

                    # Generate logo images for different single line colors
                    for color1 in line_colors:
                        single_line_color = color1

                        # Generate logo images for different normal line colors
                        for color2 in line_colors:
                            normal_line_color = color2

                            # Skip combinations where the normal line color is the same as the single line color
                            if normal_line_color == single_line_color:
                                continue

                            # Check if the current combination has been used before to avoid duplicates
                            repeated = False
                            current_combination = [single_line_color, normal_line_color]
                            for history_color in history_colors:
                                # Check if the current combination is the same as the previous one
                                if current_combination == history_color:
                                    repeated = True
                                    break
                            # If the combination is not repeated, continue
                            if repeated:
                                continue

                            # If the combination is not black or white, and the background color is black, continue
                            if (
                                single_line_color == DARK or normal_line_color == DARK
                            ) and background_color == BLACK:
                                continue
                            # If the combination is not light or white, and the background color is white, continue
                            if (
                                single_line_color == LIGHT or normal_line_color == LIGHT
                            ) and background_color == WHITE:
                                continue

                            # Generate and save the logo image with the current combination of colors
                            instance = LogoImage(
                                width=width,
                                height=height,
                                logo_size_ratio=self.logo_size_ratio,
                                angle_degrees=self.angle_degrees,
                                background_color=background_color,
                                single_line_body_color=single_line_color,
                                single_line_outline_color=single_line_color,
                                outside_line_body_color=normal_line_color,
                                outside_line_outline_color=normal_line_color,
                                inside_line_body_color=normal_line_color,
                                inside_line_outline_color=normal_line_color,
                            )
                            if draw:
                                instance.draw()
                            if show:
                                instance.result.show()
                            if save:
                                instance.save(
                                    path=os.path.join(
                                        save_folder,
                                        f"{instance.get_info()}.{self.save_format}",
                                    ),
                                    format=self.save_format,
                                )
                            if save_cfg:
                                instance.save_cfg(
                                    path=os.path.join(
                                        cfg_folder, f"{instance.get_info()}.cfg"
                                    ),
                                    mode="a",
                                )

                            # Add the current combination to the history colors
                            history_colors.append(current_combination)


