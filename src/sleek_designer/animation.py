from collections.abc import Callable

import numpy as np
from numpy.typing import NDArray
from moviepy import ImageSequenceClip  # type: ignore[import-untyped]

from sleek_designer.pattern import Pattern


class VideoGenerator:
    def __init__(
        self,
        dynamic_pattern_function: Callable[[float], Pattern | None],
    ) -> None:
        self.dynamic_pattern = dynamic_pattern_function

    def generate(
        self,
        fps: float = 30,
        width: int = 640,
        height: int = 480,
        ratio: float = 0.7,
    ) -> list[NDArray[np.uint8]]:
        time = 0.0
        frames: list[NDArray[np.uint8]] = []
        while True:
            pattern = self.dynamic_pattern(time)
            if pattern is None:
                break
            frames.append(pattern.generate(width=width, height=height, ratio=ratio))
            time += 1 / fps
        return frames

    def save_video(
        self,
        fps: float = 30,
        width: int = 640,
        height: int = 480,
        ratio: float = 0.7,
        file_path: str = "test.mp4",
    ) -> None:
        frames = self.generate(fps=fps, width=width, height=height, ratio=ratio)
        clip = ImageSequenceClip(frames, fps=fps)
        clip.write_videofile(file_path)
