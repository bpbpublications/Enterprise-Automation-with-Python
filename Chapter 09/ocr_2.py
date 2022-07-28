from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Timeout/terminate the OCR after a period of time
try:
    # Timeout after 0.1 second
    print(pytesseract.image_to_string('ocrTest.jpg', timeout=0.1))
except RuntimeError as timeout_error:
    # Tesseract processing is terminated
    print("TIMED OUT")
    pass
