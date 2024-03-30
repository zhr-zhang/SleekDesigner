import os
from logo import *
from pattern import Pattern
from color import *
from tqdm import tqdm
from moviepy.editor import ImageSequenceClip
from video_generator import VideoGenerator

obj = llf_pattern
format = "png"

obj.rotate(0).save_image(
    path=f"logos/{obj.name}/{obj.name}new.{format}",
    format=format,
)


# def dynamic_zhr(time: float) -> Pattern:
#     stretch = 0.4
#     point_appear = 0.2
#     rotate = 0.4

#     grid_x = 12 * math.sqrt(2) + 2
#     grid_y = 12 * math.sqrt(2) + 2
#     background_color = BLACK
#     single_color = RED
#     normal_color = LIGHT
#     if time == 0:
#         pattern = Pattern(
#             figures=[
#                 Dot(Point(0, 0), color=single_color),
#             ],
#             background_color=background_color,
#             grids_x=grid_x,
#             grids_y=grid_y,
#         )
#     elif time <= stretch:
#         t = time - 0
#         pattern = Pattern(
#             figures=[
#                 Line(
#                     a=Point(-6 * math.sqrt(2) / stretch * t, 0),
#                     b=Point(6 * math.sqrt(2) / stretch * t, 0),
#                     color=single_color,
#                 ),
#             ],
#             background_color=background_color,
#             grids_x=grid_x,
#             grids_y=grid_y,
#         )
#     elif time <= stretch + point_appear:
#         t = time - stretch
#         pattern = Pattern(
#             figures=[
#                 Dot(
#                     Point(-6 * math.sqrt(2), 0),
#                     color=normal_color,
#                     distance=t / point_appear,
#                 ),
#                 Dot(
#                     Point(6 * math.sqrt(2), 0),
#                     color=normal_color,
#                     distance=t / point_appear,
#                 ),
#                 Dot(
#                     Point(-2 * math.sqrt(2), 0),
#                     color=normal_color,
#                     distance=t / point_appear,
#                 ),
#                 Dot(
#                     Point(2 * math.sqrt(2), 0),
#                     color=normal_color,
#                     distance=t / point_appear,
#                 ),
#                 Line(
#                     a=Point(-6 * math.sqrt(2), 0),
#                     b=Point(6 * math.sqrt(2), 0),
#                     color=single_color,
#                 ),
#             ],
#             background_color=background_color,
#             grids_x=grid_x,
#             grids_y=grid_y,
#         )
#     elif time <= stretch + point_appear + rotate:
#         t = time - stretch - point_appear
#         pattern = Pattern(
#             figures=[
#                 Line(
#                     a=Point(-6 * math.sqrt(2), 0),
#                     b=Point(
#                         -6 * math.sqrt(2) + 6 * math.sqrt(2) * t / rotate,
#                         6 * math.sqrt(2) * t / rotate,
#                     ),
#                     color=normal_color,
#                 ),
#                 Line(
#                     a=Point(6 * math.sqrt(2), 0),
#                     b=Point(
#                         6 * math.sqrt(2) - 6 * math.sqrt(2) * t / rotate,
#                         -6 * math.sqrt(2) * t / rotate,
#                     ),
#                     color=normal_color,
#                 ),
#                 Line(
#                     a=Point(-2 * math.sqrt(2), 0),
#                     b=Point(
#                         -2 * math.sqrt(2) + 2 * math.sqrt(2) * t / rotate,
#                         2 * math.sqrt(2) * t / rotate,
#                     ),
#                     color=normal_color,
#                 ),
#                 Line(
#                     a=Point(2 * math.sqrt(2), 0),
#                     b=Point(
#                         2 * math.sqrt(2) - 2 * math.sqrt(2) * t / rotate,
#                         -2 * math.sqrt(2) * t / rotate,
#                     ),
#                     color=normal_color,
#                 ),
#                 Line(
#                     a=Point(
#                         -6 * math.sqrt(2) + 6 * math.sqrt(2) * t / rotate,
#                         6 * math.sqrt(2) * t / rotate,
#                     ),
#                     b=Point(
#                         6 * math.sqrt(2) - 6 * math.sqrt(2) * t / rotate,
#                         -6 * math.sqrt(2) * t / rotate,
#                     ),
#                     color=single_color,
#                 ),
#             ],
#             background_color=background_color,
#             grids_x=grid_x,
#             grids_y=grid_y,
#         )
#     else:
#         return "finished"
#     return pattern


# vidio_generator = VideoGenerator(dynamic_pattern_function=dynamic_zhr)
# vidio_generator.save_video(
#     fps=60,
#     width=1920 * 2,
#     height=1080 * 2,
#     ratio=0.5,
#     file_path="zhr4k60.mp4",
# )
