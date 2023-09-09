from utils import *
from batch_generator import *

if __name__ == "__main__":
    generator = DefaultBatchGenerator(
        image_shape="16:9",
        min_width=128,
        min_height=128,
        logo_size_ratio=0.7,
        power_range=range(1),
        use_round_shape=False,
    )
    generator.generate(
        draw=True,
        save=True,
    )
