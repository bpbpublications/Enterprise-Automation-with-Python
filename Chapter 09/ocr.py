from PIL import Image

import pytesseract

# You neeed to specify the tesseract location by specifying the tesseract installation path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# convert image to string and print the image
print(pytesseract.image_to_string(Image.open('ocrTest.jpg')))



