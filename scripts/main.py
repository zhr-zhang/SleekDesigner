from video_generator import VideoGenerator
from utils import *
import os

if __name__ == "__main__":
    generator = VideoGenerator(
        time_seconds=5,
        degree_per_second=10,
        logo_size_ratio=0.5,
        width=512,
        height=512,
    )
    generator.generate()
