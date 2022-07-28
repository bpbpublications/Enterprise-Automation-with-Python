import os
from PIL import Image

infile = "loadImage.png"

f, e = os.path.splitext(infile)
outfile = f + ".jpg"
if infile != outfile:
    try:
        with Image.open(infile) as im:
            rgb_im = im.convert('RGB')
            rgb_im.save(outfile)
    except OSError:
        print("cannot convert", infile)
