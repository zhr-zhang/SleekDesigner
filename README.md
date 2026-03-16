# SleekDesigner

A lightweight Python framework for creating beautiful geometric logos and animations.

## Installation

Requires Python 3.12+. Install with [uv](https://docs.astral.sh/uv/):

```bash
uv sync
```

## Getting Started

Built-in patterns are available in `examples/logos.py`:

```python
from sleek_designer import Pattern, Line, Point, RED, LIGHT, BLACK

pattern = Pattern(
    figures=[
        Line(a=Point(-6, 6), b=Point(6, 6), color=LIGHT),
        Line(a=Point(6, 6), b=Point(-6, -6), color=RED),
    ],
    grids_x=20,
    grids_y=20,
    background_color=BLACK,
)
pattern.save_image(path="my_logo.png")
```

Generate all built-in logos:

```bash
uv run python examples/logos.py
```

Generate an animation:

```bash
uv run python examples/dynamic_zhr.py
```

## License

GPL — see [LICENSE](LICENSE).
