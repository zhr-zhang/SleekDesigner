import math

from sleek_designer import (
    Pattern,
    Line,
    Dot,
    Point,
    VideoGenerator,
    RED,
    LIGHT,
    BLACK,
)

SQRT2 = math.sqrt(2)


def dynamic_zhr(time: float) -> Pattern | None:
    # Phase durations (seconds)
    phase_stretch = 1.0
    phase_appear = 0.5
    phase_rotate = 1.0

    # Style
    grid = 12 * SQRT2 + 2
    bg = BLACK
    accent = RED
    base = LIGHT

    if time == 0:
        return Pattern(
            figures=[Dot(Point(0, 0), color=accent)],
            background_color=bg,
            grids_x=grid,
            grids_y=grid,
        )

    elif time <= phase_stretch:
        t = time
        half = 6 * SQRT2 / phase_stretch * t
        return Pattern(
            figures=[Line(a=Point(-half, 0), b=Point(half, 0), color=accent)],
            background_color=bg,
            grids_x=grid,
            grids_y=grid,
        )

    elif time <= phase_stretch + phase_appear:
        t = time - phase_stretch
        radius = t / phase_appear
        return Pattern(
            figures=[
                Line(a=Point(-6 * SQRT2, 0), b=Point(6 * SQRT2, 0), color=accent),
                Dot(Point(-6 * SQRT2, 0), color=base, distance=radius),
                Dot(Point(6 * SQRT2, 0), color=base, distance=radius),
                Dot(Point(-2 * SQRT2, 0), color=base, distance=radius),
                Dot(Point(2 * SQRT2, 0), color=base, distance=radius),
            ],
            background_color=bg,
            grids_x=grid,
            grids_y=grid,
        )
    elif time <= phase_stretch + phase_appear + phase_rotate:
        t = time - phase_stretch - phase_appear
        progress = t / phase_rotate

        def _lerp(start: float, end: float) -> float:
            return start + (end - start) * progress

        return Pattern(
            figures=[
                # Main diagonal (stretching from horizontal to 45 deg)
                Line(
                    a=Point(_lerp(-6 * SQRT2, 0), _lerp(0, 6 * SQRT2)),
                    b=Point(_lerp(6 * SQRT2, 0), _lerp(0, -6 * SQRT2)),
                    color=accent,
                ),
                # Outer arms
                Line(
                    a=Point(-6 * SQRT2, 0),
                    b=Point(_lerp(-6 * SQRT2, 0), _lerp(0, 6 * SQRT2)),
                    color=base,
                ),
                Line(
                    a=Point(6 * SQRT2, 0),
                    b=Point(_lerp(6 * SQRT2, 0), _lerp(0, -6 * SQRT2)),
                    color=base,
                ),
                # Inner arms
                Line(
                    a=Point(-2 * SQRT2, 0),
                    b=Point(_lerp(-2 * SQRT2, 0), _lerp(0, 2 * SQRT2)),
                    color=base,
                ),
                Line(
                    a=Point(2 * SQRT2, 0),
                    b=Point(_lerp(2 * SQRT2, 0), _lerp(0, -2 * SQRT2)),
                    color=base,
                ),
            ],
            background_color=bg,
            grids_x=grid,
            grids_y=grid,
        )

    else:
        return None


if __name__ == "__main__":
    generator = VideoGenerator(dynamic_pattern_function=dynamic_zhr)
    generator.save_video(
        fps=60,
        width=1920 * 4,
        height=1080 * 4,
        ratio=0.5,
        file_path="zhr4k60.mp4",
    )
