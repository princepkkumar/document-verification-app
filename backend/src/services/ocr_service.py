 
# backend/src/services/ocr_service.py

import easyocr
import numpy as np

# Initialize the EasyOCR reader. 
# This is done once when the module is loaded to avoid reloading the heavy model on every API call.
# ['en'] specifies that we are looking for English text.
print("Loading EasyOCR model into memory...")
reader = easyocr.Reader(['en'], gpu=False) # Set gpu=False to use CPU
print("EasyOCR model loaded.")


def extract_text_from_image(image_bytes: bytes) -> str:
    """
    Uses EasyOCR to detect and extract text from an image.

    Args:
        image_bytes: The image file in bytes.

    Returns:
        A string containing all the text found in the image, separated by newlines.
    """
    try:
        # The reader.readtext method can take bytes directly
        result = reader.readtext(image_bytes)

        if not result:
            return "" # Return an empty string if no text is found

        # The result is a list of tuples, where each tuple contains
        # (bounding_box, text, confidence_score).
        # We only need the text part.
        extracted_texts = [text for bbox, text, conf in result]
        
        # Join all the extracted text fragments with a newline character
        return "\n".join(extracted_texts)

    except Exception as e:
        print(f"An error occurred during EasyOCR processing: {e}")
        # In a real app, you might want to handle this more gracefully
        raise e