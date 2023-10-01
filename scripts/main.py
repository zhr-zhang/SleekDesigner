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
    filename="wide8k120",
    width=7680,
    height=4320,
    frame_frequency=120,
    arc_body_color=BLUE,
    arc_outline_color=BLUE,
    single_line_body_color=BLUE,
    single_line_outline_color=BLUE,
)
