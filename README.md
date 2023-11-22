# SleekDesigner

`SleekDesigner` is a simple and lightweight python framework for creating beautiful and smooth logos.

## Usage

```python
from utils import *
from pattern import Pattern
from figure import *
arrow = Pattern(
    figures=[
        Line(a=(10, 0), b=(0, 10), color=WHITE),
        Line(a=(10, 0), b=(0, -10), color=WHITE),
        Line(a=(-10, 0), b=(10, 0), color=RED),
    ],
    size=22,
)
Pattern.save(
    obj=arrow.generate_image(),
    path="arrow.png",
    format="png",
)
```

## Installation

This project is written in `python3` , and is based on some libraries. So before you run the code, make sure that you have had them installed.

```bash
$ pip install numpy pillow moviepy
```

## License

This project is licensed under the `GPL` License - see the [LICENSE](LICENSE) file for details.

## Contributing

To contribute to this project, please fork the repository and submit a pull request.
