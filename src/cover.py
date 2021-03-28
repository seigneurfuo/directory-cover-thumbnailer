#!/bin/env python3

from sys import argv
from os import path, listdir
from urllib.parse import unquote

try:
    from PIL import Image, ImageDraw
except ImportError:
    import Image


available_covers_names = ["cover", "Cover"]
available_covers_extensions = ['.png', '.jpg', '.jpeg']
excludes = ("trash://")


folder_path = argv[1] # Which file are we working with?
output_file = argv[2] # Where do does the file have to be saved?
size = int(argv[3]) # Required size?


if folder_path.startswith(excludes):
    exit(0)

# Remove "file://" and convert url to path
folder_path = folder_path.replace('file://', '')
folder_path = unquote(folder_path)

covers = [cover for cover in listdir(folder_path) if path.splitext(cover)[0] in available_covers_names and path.splitext(cover)[1] in available_covers_extensions]

# print(folder_path, ":", covers)

# Pure python convert - We can also use imagemagick
if covers and path.isfile(path.join(folder_path, covers[0])):
    cover_filepath = path.join(folder_path, covers[0])

    picture = Image.open(cover_filepath)
    picture.thumbnail((size, size), Image.ANTIALIAS)
    # if im.mode == "CMYK":
    # im = im.convert("RGB")
    picture.save(output_file, "PNG")

else:
    exit(1)
