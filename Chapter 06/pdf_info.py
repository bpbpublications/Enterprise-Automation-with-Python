from PyPDF2 import PdfFileReader

pdf = PdfFileReader("large_file.pdf")

# getting the number of pages in PDF
print("Number of pages: " + str(pdf.getNumPages()))

# Printing document information
print(pdf.documentInfo)
