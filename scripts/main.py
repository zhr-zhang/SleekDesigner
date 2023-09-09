from utils import *
from batch_generator import *

if __name__ == "__main__":
    generator = DefaultBatchGenerator(
        image_shape="16:9",
        min_width=1920,
        min_height=1080,
        logo_size_ratio=0.5,
        power_range=range(3,4),
        use_round_shape=False,
    )
    generator.generate(
        draw=True,
        save=True,
    )
