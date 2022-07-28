from PyPDF2 import PdfFileWriter

pdf_file_writer = PdfFileWriter()

page = pdf_file_writer.addBlankPage(width=72, height=72)

with open("blank_pdf.pdf",'wb') as file:
    pdf_file_writer.write(file)
