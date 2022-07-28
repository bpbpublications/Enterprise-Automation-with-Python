from PyPDF2 import PdfFileReader

pdf_reader = PdfFileReader("large_file.pdf")

with open("large_file.txt",'w', encoding='utf-8') as file:
    for page in pdf_reader.pages:
        text = page.extractText()
        file.write(text)
