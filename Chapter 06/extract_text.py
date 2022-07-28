import pdfminer
import pdfminer.layout
import pdfminer.high_level

text = pdfminer.high_level.extract_text('large_file.pdf')
print(text)
