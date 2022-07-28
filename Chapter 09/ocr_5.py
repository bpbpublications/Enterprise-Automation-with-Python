# List of available languages
print(pytesseract.get_languages(config=''))

# French text image to string
# print(pytesseract.image_to_string(Image.open('test-european.jpg'), lang='fra'))

# Batch processing with a single file containing the list of multiple image file paths
# print(pytesseract.image_to_string('images.txt'))

# Get a searchable PDF
pdf = pytesseract.image_to_pdf_or_hocr('test.png', extension='pdf')
with open('test.pdf', 'w+b') as f:
    f.write(pdf) # pdf type is bytes by default

# Get HOCR output
hocr = pytesseract.image_to_pdf_or_hocr('test.png', extension='hocr')

# Get ALTO XML output
xml = pytesseract.image_to_alto_xml('test.png')
