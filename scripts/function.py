from utils import *
from image import LogoImage
from tqdm import tqdm
from PIL import Image
from moviepy.editor import ImageSequenceClip
import numpy as np


class Function:
    @staticmethod
    def generate_single_logo(
        width=3840,
        height=2160,
        angle_degrees=45,
        logo_size_ratio=0.5,
        outline_thickness=2,
        background_color=BLACK,
        outside_line_color=LIGHT,
        inside_line_color=LIGHT,
        single_line_color=RED,
        arc_color=RED,
        filename="logo.png",
    ):
        save_folder = os.path.join(output_folder, "single")
        os.makedirs(save_folder, exist_ok=True)
        image = LogoImage(
            width=width,
            height=height,
            angle_degrees=angle_degrees,
            logo_size_ratio=logo_size_ratio,
            outline_thickness=outline_thickness,
            background_color=background_color,
            outside_line_body_color=outside_line_color,
            outside_line_outline_color=outside_line_color,
            inside_line_body_color=inside_line_color,
            inside_line_outline_color=inside_line_color,
            single_line_body_color=single_line_color,
            single_line_outline_color=single_line_color,
            arc_body_color=arc_color,
            arc_outline_color=arc_color,
        )
        image.draw()
        image.save(path=os.path.join(save_folder, filename), format="png")

    @staticmethod
    def batch_generate_logo(
        logo_size_ratio=0.5,
        image_shape="wide",
        save_format="png",
        power_range=range(3),
        min_width=128,
        min_height=128,
        angle_degrees=45,
        draw=True,
        show=False,
        save=True,
        save_cfg=False,
    ):
        for power in power_range:
            width = min_width * pow(2, power)
            height = min_height * pow(2, power)
            for background_color in BACKGROUND_COLORS:
                history_colors = []
                save_folder = os.path.join(
                    output_folder,
                    "batch",
                    image_shape,
                    COLOR_MAP.get(background_color, "unknown"),
                    str(width),
                )
                os.makedirs(save_folder, exist_ok=True)
                for theme_color in THEME_COLORS:
                    line_colors = [theme_color, LIGHT, DARK]
                    for color1 in line_colors:
                        single_line_color = color1
                        for color2 in line_colors:
                            normal_line_color = color2
                            if normal_line_color == single_line_color:
                                continue
                            repeated = False
                            current_combination = [single_line_color, normal_line_color]
                            for history_color in history_colors:
                                if current_combination == history_color:
                                    repeated = True
                                    break
                            if repeated:
                                continue
                            if (
                                single_line_color == DARK or normal_line_color == DARK
                            ) and background_color == BLACK:
                                continue
                            if (
                                single_line_color == LIGHT or normal_line_color == LIGHT
                            ) and background_color == WHITE:
                                continue
                            instance = LogoImage(
                                width=width,
                                height=height,
                                logo_size_ratio=logo_size_ratio,
                                angle_degrees=angle_degrees,
                                background_color=background_color,
                                single_line_body_color=single_line_color,
                                single_line_outline_color=single_line_color,
                                outside_line_body_color=normal_line_color,
                                outside_line_outline_color=normal_line_color,
                                inside_line_body_color=normal_line_color,
                                inside_line_outline_color=normal_line_color,
                                arc_body_color=single_line_color,
                                arc_outline_color=single_line_color,
                            )
                            if draw:
                                instance.draw()
                            if show:
                                instance.result.show()
                            if save:
                                instance.save(
                                    path=os.path.join(
                                        save_folder,
                                        f"{instance.get_info()}.{save_format}",
                                    ),
                                    format=save_format,
                                )
                            if save_cfg:
                                instance.save_cfg(
                                    path=os.path.join(
                                        cfg_folder, f"{instance.get_info()}.cfg"
                                    ),
                                    mode="a",
                                )
                            history_colors.append(current_combination)

    @staticmethod
    def generate_video(
        logo_size_ratio=0.5,
        filename="wide1080",
        width: int = 1920,
        height: int = 1080,
        outline_thickness: float = 2,
        background_color=BLACK,
        outside_line_body_color=LIGHT,
        outside_line_outline_color=LIGHT,
        inside_line_body_color=LIGHT,
        inside_line_outline_color=LIGHT,
        single_line_body_color=RED,
        single_line_outline_color=RED,
        arc_body_color=RED,
        arc_outline_color=RED,
        start_angle_degrees=45,
        degree_per_second=45,
        frame_frequency=30,
        time_seconds=4,
    ):
        save_folder = os.path.join(output_folder, "video")
        os.makedirs(save_folder, exist_ok=True)

        num_frames = time_seconds * frame_frequency
        angle_degree_per_frame = degree_per_second / frame_frequency

        frame_folder = os.path.join(save_folder, "frames")
        os.makedirs(frame_folder, exist_ok=True)

        frames = []
        progress_bar = tqdm(total=num_frames, desc="Generating frames", unit="frames")
        for i in range(num_frames):
            present_angle_degree = start_angle_degrees + i * angle_degree_per_frame
            frame = LogoImage(
                width=width,
                height=height,
                logo_size_ratio=logo_size_ratio,
                angle_degrees=present_angle_degree,
                outline_thickness=outline_thickness,
                background_color=background_color,
                outside_line_body_color=outside_line_body_color,
                outside_line_outline_color=outside_line_outline_color,
                inside_line_body_color=inside_line_body_color,
                inside_line_outline_color=inside_line_outline_color,
                single_line_body_color=single_line_body_color,
                single_line_outline_color=single_line_outline_color,
                arc_body_color=arc_body_color,
                arc_outline_color=arc_outline_color,
            )
            frame.draw()
            frame_path = os.path.join(frame_folder, f"{i:06d}.png")
            frame.save(frame_path, format="png")
            frames.append(np.array(Image.open(frame_path)))
            progress_bar.update(1)
        progress_bar.close()

        clip = ImageSequenceClip(frames, fps=frame_frequency)
        output_path = os.path.join(save_folder, f"{filename}.mp4")
        clip.write_videofile(
            output_path,
            codec="libx264",
            fps=frame_frequency,
            preset="ultrafast",
            ffmpeg_params=["-crf", "0"],
        )

        print(f"无损视频已创建：{output_path}")
