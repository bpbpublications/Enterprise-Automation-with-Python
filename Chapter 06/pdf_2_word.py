import pdfminer
import pdfminer.layout
import pdfminer.high_level
from docx import Document
from docx.shared import Inches

text = pdfminer.high_level.extract_text('small_pdf.pdf')

def valid_xml_char_ordinal(c):
    codepoint = ord(c)
    # conditions ordered by presumed frequency
    return (
        0x20 <= codepoint <= 0xD7FF or
        codepoint in (0x9, 0xA, 0xD) or
        0xE000 <= codepoint <= 0xFFFD or
        0x10000 <= codepoint <= 0x10FFFF
        )
cleaned_string = ''.join(c for c in text if valid_xml_char_ordinal(c))

document = Document()
p = document.add_paragraph(cleaned_string)
document.add_page_break()
document.save("pdf_doc.docx")
