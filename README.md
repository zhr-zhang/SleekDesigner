# Sleek Designer
sleek designer is a simple and lightweight python framework for creating beautiful and smooth logos.

## Usage
'''python'''
arrow = Pattern(
    figures=[
        Line((10, 0), (0, 10), color=WHITE),
        Line((10, 0), (0, -10), color=WHITE),
        Line((-10, 0), (10, 0), color=RED),
    ],
    size=22,
)
Pattern.save(obj=arrow.generate_image(), path="arrow.png")
'''python'''
output/0.png
