from PyPDF2 import PdfFileWriter, PdfFileReader

pdf_file_writer = PdfFileWriter()

large_pdf = PdfFileReader("large_file.pdf")

pdf_file_writer.addPage(large_pdf.getPage(0))

with open("small_pdf.pdf",'wb') as file:
    pdf_file_writer.write(file)
