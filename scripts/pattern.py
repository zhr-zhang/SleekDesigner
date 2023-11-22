import math
import numpy as np
import os
from PIL import Image
from tqdm import tqdm
from moviepy.editor import ImageSequenceClip
from color import *
from figure import *


class Pattern:
    def __init__(
        self,
        figures: list[Figure] = [Line(a=(0, -5), b=(0, 5), color=RED)],
        size: int = 11,
        background_color: (np.uint8, np.uint8, np.uint8, np.uint8) = BLACK,
        name: str = "",
    ) -> None:
        self.figures = figures
        self.size = size
        self.background_color = background_color
        self.name = name

    def generate_image(
        self,
        width: int = 1024,
        height: int = 1024,
        ratio: float = 0.7,
        angle_degrees: float = 0,
    ):
        logo_size = int(min(width, height) * ratio)
        self.value = np.full((width, height, 4), self.background_color, dtype=np.uint8)
        logo_slice = np.full(
            (logo_size, logo_size, 4), self.background_color, dtype=np.uint8
        )

        unit = logo_size / self.size
        half_size = logo_size / 2
        angle_arc = angle_degrees * math.pi / 180
        sin_angle = math.sin(angle_arc)
        cos_angle = math.cos(angle_arc)

        for x in range(logo_size):
            for y in range(logo_size):
                m = (x - half_size) / unit
                n = (y - half_size) / unit
                x_in_logo = m * cos_angle + n * sin_angle
                y_in_logo = -m * sin_angle + n * cos_angle
                for figure in self.figures:
                    if figure.is_inside(x_in_logo, y_in_logo):
                        logo_slice[x, y, :] = figure.color
                        break

        self.value[
            ((width - logo_size) // 2) : ((width + logo_size) // 2),
            ((height - logo_size) // 2) : ((height + logo_size) // 2),
        ] = logo_slice
        self.value = np.rot90(self.value, k=1)

        return self.value

    def generate_video(
        self,
        ratio: float = 0.7,
        filename: str = "wide1080",
        width: int = 1920,
        height: int = 1080,
        background_color: (np.uint8, np.uint8, np.uint8, np.uint8) = BLACK,
        start_angle_degrees: float = 45,
        degree_per_second: float = 45,
        fps: int = 30,
        time_seconds: float = 4,
    ):
        save_folder = "video"
        os.makedirs(save_folder, exist_ok=True)

        num_frames = time_seconds * fps
        angle_degree_per_frame = degree_per_second / fps

        frames = []
        progress_bar = tqdm(total=num_frames, desc="Generating frames", unit="frames")
        for i in range(num_frames):
            present_angle_degrees = start_angle_degrees + i * angle_degree_per_frame
            frames.append(
                self.generate_image(
                    width=width,
                    height=height,
                    background_color=background_color,
                    ratio=ratio,
                    angle_degrees=present_angle_degrees,
                )
            )
            progress_bar.update(1)
        progress_bar.close()

        output_path = os.path.join(save_folder, f"{filename}.mp4")
        clip = ImageSequenceClip(frames, fps=fps)
        clip.write_videofile(
            output_path,
            codec="libx264",
            fps=fps,
            preset="ultrafast",
            ffmpeg_params=["-crf", "0"],
        )

    @staticmethod
    def save(obj, path, format="png") -> None:
        Image.fromarray(obj, "RGBA").save(path, format=format)
