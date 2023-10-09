from function import Function as F
from utils import *

# F.generate_single_logo(
#     width=7680 * 4,
#     height=4320 * 4,
#     filename="wide32k.png",
# )

# F.batch_generate_logo()

F.generate_video(
    logo_size_ratio=0.5,
    filename="BlueWide2k30",
    width=1920,
    height=1080,
    frame_frequency=30,
    arc_body_color=BLUE,
    arc_outline_color=BLUE,
    single_line_body_color=BLUE,
    single_line_outline_color=BLUE,
)
