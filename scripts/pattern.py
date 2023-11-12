import math
import numpy as np
from PIL import Image
from tqdm import tqdm
from moviepy.editor import ImageSequenceClip
from utils import *
from figure import Figure


class Pattern:
    def __init__(
        self,
        figures=CLASSIC_LOGO_FIGURES,
        size=CLASSIC_LOGO_SIZE,
        background_color=BLACK,
    ) -> None:
        self.figures = figures
        self.size = size
        self.background_color = background_color

    def generate_image(
        self,
        width=1920,
        height=1080,
        ratio=0.5,
        angle_degrees=45,
    ):
        logo_size = int(min(width, height) * ratio)
        self.value = np.full((width, height, 4), self.background_color, dtype=np.uint8)
        logo_slice = np.full(
            (logo_size, logo_size, 4), self.background_color, dtype=np.uint8
        )

        unit = logo_size / self.size
        unit2 = pow(unit, 2)
        standard_distance2 = pow(Figure.STANDARD_DISTANCE * unit, 2)
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
                    distance2 = figure.distance2(x_in_logo, y_in_logo) * unit2
                    if distance2 <= standard_distance2:
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
        ratio=0.5,
        filename="wide1080",
        width: int = 1920,
        height: int = 1080,
        background_color=BLACK,
        start_angle_degrees=45,
        degree_per_second=45,
        fps=30,
        time_seconds=4,
    ):
        save_folder = os.path.join(output_folder, "video")
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


