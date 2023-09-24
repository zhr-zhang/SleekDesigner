from image import LogoImage
from utils import *
import os
from tqdm import tqdm
from PIL import Image
from moviepy.editor import ImageSequenceClip
import numpy as np


class VideoGenerator:
    def __init__(
        self,
        logo_size_ratio=0.7,
        filename="wide1080",
        width=1920,
        height=1080,
        outline_thickness: float = 2,
        background_color=BLACK,
        outside_line_body_color=LIGHT,
        outside_line_outline_color=LIGHT,
        inside_line_body_color=LIGHT,
        inside_line_outline_color=LIGHT,
        single_line_body_color=Z_RED,
        single_line_outline_color=Z_RED,
        arc_body_color=Z_RED,
        arc_outline_color=Z_RED,
        start_angle_degrees=0,
        degree_per_second=45,
        frame_frequency=30,
        time_seconds=5,
    ):
        self.logo_size_ratio = logo_size_ratio
        self.width = width
        self.height = height
        self.filename = filename
        self.outline_thickness = outline_thickness
        self.background_color = background_color
        self.outside_line_body_color = outside_line_body_color
        self.outside_line_outline_color = outside_line_outline_color
        self.inside_line_body_color = inside_line_body_color
        self.inside_line_outline_color = inside_line_outline_color
        self.single_line_body_color = single_line_body_color
        self.single_line_outline_color = single_line_outline_color
        self.arc_body_color = arc_body_color
        self.arc_outline_color = arc_outline_color
        
        self.start_angle_degrees = start_angle_degrees
        self.degree_per_second = degree_per_second
        self.frame_frequency = frame_frequency
        self.time_seconds = time_seconds
        self.save_folder = os.path.join(output_folder, "video")
        os.makedirs(self.save_folder, exist_ok=True)

    def generate(self):
        num_frames = self.time_seconds * self.frame_frequency
        angle_degree_per_frame = self.degree_per_second / self.frame_frequency
        present_angle_degree = self.start_angle_degrees

        frame_folder = os.path.join(self.save_folder, "frames")
        os.makedirs(frame_folder, exist_ok=True)

        frames = []
        processing_bar = tqdm(total=num_frames, desc="Generating frames", unit="frames")
        for i in range(num_frames):
            frame = LogoImage(
                width=self.width,
                height=self.height,
                logo_size_ratio=self.logo_size_ratio,
                angle_degrees=present_angle_degree,
                outline_thickness=self.outline_thickness,
                background_color=self.background_color,
                outside_line_body_color=self.outside_line_body_color,
                outside_line_outline_color=self.outside_line_outline_color,
                inside_line_body_color=self.inside_line_body_color,
                inside_line_outline_color=self.inside_line_outline_color,
                single_line_body_color=self.single_line_body_color,
                single_line_outline_color=self.single_line_outline_color,
                arc_body_color=self.arc_body_color,
                arc_outline_color=self.arc_outline_color,
            )
            frame.draw()
            frame_path = os.path.join(frame_folder, f"{i:06d}.png")
            frame.save(frame_path, format="png")
            frames.append(np.array(Image.open(frame_path)))
            present_angle_degree += angle_degree_per_frame
            processing_bar.update(1)
        processing_bar.close()

        clip = ImageSequenceClip(frames, fps=self.frame_frequency)
        output_path = os.path.join(self.save_folder, f"{self.filename}.mp4")
        clip.write_videofile(output_path, codec='libx264', fps=self.frame_frequency, preset='ultrafast', ffmpeg_params=['-crf', '0'])

        print(f'无损视频已创建：{output_path}')
