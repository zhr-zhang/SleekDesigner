# from utils import *


# class Function:
#     @staticmethod
#     def batch_generate_logo(
#         logo_size_ratio=0.5,
#         image_shape="wide",
#         save_format="png",
#         power_range=range(3),
#         min_width=128,
#         min_height=128,
#         angle_degrees=45,
#     ):
#         for power in power_range:
#             width = min_width * pow(2, power)
#             height = min_height * pow(2, power)
#             for background_color in BACKGROUND_COLORS:
#                 history_colors = []
#                 save_folder = os.path.join(
#                     output_folder,
#                     "batch",
#                     image_shape,
#                     COLOR_MAP.get(background_color, "unknown"),
#                     str(width),
#                 )
#                 os.makedirs(save_folder, exist_ok=True)
#                 for theme_color in THEME_COLORS:
#                     line_colors = [theme_color, LIGHT, DARK]
#                     for color1 in line_colors:
#                         single_line_color = color1
#                         for color2 in line_colors:
#                             normal_line_color = color2
#                             if normal_line_color == single_line_color:
#                                 continue
#                             repeated = False
#                             current_combination = [single_line_color, normal_line_color]
#                             for history_color in history_colors:
#                                 if current_combination == history_color:
#                                     repeated = True
#                                     break
#                             if repeated:
#                                 continue
#                             if (
#                                 single_line_color == DARK or normal_line_color == DARK
#                             ) and background_color == BLACK:
#                                 continue
#                             if (
#                                 single_line_color == LIGHT or normal_line_color == LIGHT
#                             ) and background_color == WHITE:
#                                 continue
#                             instance = LogoImage(
#                                 width=width,
#                                 height=height,
#                                 logo_size_ratio=logo_size_ratio,
#                                 angle_degrees=angle_degrees,
#                                 background_color=background_color,
#                                 single_line_body_color=single_line_color,
#                                 single_line_outline_color=single_line_color,
#                                 outside_line_body_color=normal_line_color,
#                                 outside_line_outline_color=normal_line_color,
#                                 inside_line_body_color=normal_line_color,
#                                 inside_line_outline_color=normal_line_color,
#                                 arc_body_color=single_line_color,
#                                 arc_outline_color=single_line_color,
#                             )
#                             instance.save(
#                                 path=os.path.join(
#                                     save_folder,
#                                     f"{instance.get_info()}.{save_format}",
#                                 ),
#                                 format=save_format,
#                             )
#                             history_colors.append(current_combination)
