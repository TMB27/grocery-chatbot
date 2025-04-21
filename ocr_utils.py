# ocr_utils.py

import cv2
import pytesseract

def extract_text_from_image(image_path):
    image = cv2.imread(image_path)         # Load the image
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
    text = pytesseract.image_to_string(gray)        # OCR magic happens here!
    return text
