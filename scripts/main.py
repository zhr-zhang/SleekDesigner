# from utils import *
from pattern import Logo
from PIL import Image

logo = Logo()
Image.fromarray(logo.generate_image(), mode="RGBA").save("test.png")
# logo.generate_video(filename="test.mp4")
