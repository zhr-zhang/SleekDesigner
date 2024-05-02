# SleekDesigner

`SleekDesigner` is a simple and lightweight python framework for creating beautiful and smooth logos.

## Getting started

`SleekDesigner` has got some build-in patterns, which can be used as examples for your own designs.
To use them, you can simply import every items in `logo` and use them as templates.

```python
from logo import *
from pattern import Pattern
from color import *

obj = syc
format = "png"

obj.generate_video(path="syc1024")

Pattern.save_image(
    obj=obj.generate_image( 
        width=2048,
        height=2048,
        ratio=0.7,
        angle_degrees=0,
    ),
    path=f"{obj.name}.{format}",
    format=format,
)
```

If you want to create your own patterns, you can use the `Pattern` class.
It has got some optional parameters, which can be used to create your own patterns.

```python
from color import *
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

Pattern.save_image(
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
