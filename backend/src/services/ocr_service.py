# backend/src/services/ocr_service.py

from PIL import Image
import pytesseract
import io

def extract_text_from_image(image_bytes: bytes) -> str:
    """
    Uses Tesseract OCR to extract text from an image.

    Args:
        image_bytes: The image file in bytes.

    Returns:
        A string containing all the text found in the image.
    """
    try:
        # Open the image from the byte stream
        image = Image.open(io.BytesIO(image_bytes))

        # Use pytesseract to extract the text
        text = pytesseract.image_to_string(image)

        print("Successfully extracted text with Tesseract.")
        return text
    except Exception as e:
        print(f"An error occurred during Tesseract OCR processing: {e}")
        return ""