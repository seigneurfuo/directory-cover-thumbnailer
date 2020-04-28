#!/bin/env python3

# Date de dernière modification: 2020.04.28

from sys import argv
from os import path, listdir
from urllib.parse import unquote

try:
    from PIL import Image, ImageDraw
except ImportError:
    import Image

allowed_covers_names = ["cover", "Cover"]
allowed_covers_extensions = ['.png', '.jpg', '.jpeg']

# Which file are we working with?
folder_path = argv[1]

# Remove "file://"
folder_path = folder_path.replace('file://', '')
folder_path = unquote(folder_path)

# Where do does the file have to be saved?
output_file = argv[2]

# Required size?
size = int(argv[3])

cover_filename = [cover for cover in listdir(folder_path) if path.splitext(cover)[0] in allowed_covers_names and path.splitext(cover)[1] in allowed_covers_extensions]

# Pure python convert - We can also use imagemagick
if cover_filename:
    cover_filepath = path.join(folder_path, cover_filename[0])

    picture = Image.open(cover_filepath)
    picture.thumbnail((size, size), Image.ANTIALIAS)
    # if im.mode == "CMYK":
    # im = im.convert("RGB")
    picture.save(output_file, "PNG")

else:
    exit(1)
