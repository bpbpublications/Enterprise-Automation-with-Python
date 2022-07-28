from PIL import Image
im = Image.open("loadImage.png")
print(im.format, im.size, im.mode)
im.show()

