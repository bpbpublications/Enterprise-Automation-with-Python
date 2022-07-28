from PIL import Image
import pytesseract
import pdfminer
import pdfminer.layout
import pdfminer.high_level

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Get a searchable PDF
pdf = pytesseract.image_to_pdf_or_hocr('ocrTest.jpg', extension='pdf')
with open('ocrTest.pdf', 'w+b') as f:
    f.write(pdf)

# PDF
text = pdfminer.high_level.extract_text('ocrTest.pdf')
print(text)
