import pdfminer
import pdfminer.layout
import pdfminer.high_level
print(pdfminer.__version__)

text = pdfminer.high_level.extract_text('large_file.pdf')
print(repr(text))
print(text)
