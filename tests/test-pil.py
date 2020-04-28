try: from PIL import Image, ImageDraw
except ImportError: import Image

picture = Image.open("dossier de test/cover.png") # ----- ignore this line -----
picture_w, picture_h = picture.size

if picture_w == picture_h:



else:
    background = Image.new("RGBA", (500,400), "white")
    draw = ImageDraw.Draw(background)

    if picture_w < picture_h:
        picture_x =
        picture y =

    else:
        picture_x =
        picture y =
