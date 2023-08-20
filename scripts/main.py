import os

from utils import *
from Logo_image import LogoImage

# Define the folder where the generated logo images will be saved
script_directory = os.path.dirname(os.path.abspath(__file__))
output_folder = os.path.join(script_directory, "..", "output")
os.makedirs(output_folder, exist_ok=True)


def main():
    # Set configuration parameters
    logo_size_ratio = 0.7
    circle_size_ratio = 1
    use_round_shape = False
    image_shape = "wide"
    save_format = "PNG"

    # Generate logo images for diffetent sizes and shapes
    for power in range(3):
        width = 1920 * pow(2, power)
        height = 1080 * pow(2, power)

        # Generate logo images for different background colors
        for background_color in BACKGROUND_COLORS:
            circle_color = background_color
            # corner_color = TRANSPARENT
            history_colors = []
            # Create a directory to save images with different sizes and shapes

            save_folder = os.path.join(
                output_folder,
                # "test",
                image_shape,
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
                            if current_combination == history_color:
                                repeated = True
                                break
                        if repeated:
                            continue

                        if (
                            single_line_color == DARK or normal_line_color == DARK
                        ) and background_color == BLACK:
                            continue
                        if (
                            single_line_color == LIGHT or normal_line_color == LIGHT
                        ) and background_color == WHITE:
                            continue

                        # Generate and save the logo image with the current combination of colors
                        instance = LogoImage(
                            height=height,
                            width=width,
                            logo_size_ratio=logo_size_ratio,
                            circle_size_ratio=circle_size_ratio,
                            use_round_shape=use_round_shape,
                            background_color=background_color,
                            circle_body_color=circle_color,
                            circle_outline_color=circle_color,
                            single_line_body_color=single_line_color,
                            single_line_outline_color=single_line_color,
                            normal_line_body_color=normal_line_color,
                            normal_line_outline_color=normal_line_color,
                        )
                        instance.save(
                            os.path.join(
                                save_folder,
                                f"{instance.get_info()}.{save_format}",
                            ),
                            format=save_format,
                        )

                        # Add the current combination to the history colors
                        history_colors.append(current_combination)


if __name__ == "__main__":
    main()
