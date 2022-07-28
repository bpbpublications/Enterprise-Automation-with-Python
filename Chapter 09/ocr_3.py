from PIL import Image

import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Get bounding box estimates
print(pytesseract.image_to_boxes(Image.open('ocrTest.jpg')))

# Get verbose data including boxes, confidences, line and page numbers
print(pytesseract.image_to_data(Image.open('ocrTest.jpg')))

# Get information about orientation and script detection
print(pytesseract.image_to_osd(Image.open('ocrTest.jpg')))


