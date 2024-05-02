from typing import Callable
from pattern import Pattern
from figure import Line, Dot
from point import Point
from color import LIGHT, RED, BLACK
from moviepy.editor import ImageSequenceClip


def dynamic_pattern(time: float) -> Pattern:
    if time == 0:
        pattern = Pattern(
            figures=[Dot(Point(0, 0), color=LIGHT)],
            background_color=BLACK,
        )
    else:
        pattern = Pattern(
            figures=[Line(a=Point(-3 * time, 0), b=Point(3 * time, 0), color=LIGHT)],
            background_color=BLACK,
        )
    return pattern


class VideoGenerator:
    def __init__(
        self,
        dynamic_pattern_function: Callable[[float], Pattern],
    ):
        self.dynamic_pattern = dynamic_pattern_function

    def generate(
        self,
        fps: float = 30,
        width: int = 640,
        height: int = 480,
        ratio: float = 0.7,
    ) -> None:
        time = 0
        frames = []
        while True:
            pattern = self.dynamic_pattern(time)
            if pattern == "finished":
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
        frames = self.generate(
            fps=fps,
            width=width,
            height=height,
            ratio=ratio,
        )
        clip = ImageSequenceClip(frames, fps=fps)
        clip.write_videofile(file_path)
