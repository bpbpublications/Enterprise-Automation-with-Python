import os
from PIL import Image
from PIL import ImageEnhance

infile = "loadImage.png"
image = Image.open(infile)

enhancer = ImageEnhance.Sharpness(image)
enhancer.enhance(2).save('loadImageSharpned.png')
