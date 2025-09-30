 
# backend/src/core/parser.py

import re
from typing import Dict, Optional

def parse_aadhaar_info(ocr_text: str) -> Dict[str, Optional[str]]:
    """
    Parses raw OCR text to extract structured information from an Aadhaar card.

    Args:
        ocr_text: A string containing the text extracted from the document.

    Returns:
        A dictionary containing the extracted fields.
    """
    data = {
        "name": None,
        "dob": None,
        "gender": None,
        "aadhaar_number": None
    }

    # Regex to find a 12-digit number, possibly with spaces.
    # This is a strong indicator of the Aadhaar number.
    aadhaar_pattern = r'\b\d{4}\s\d{4}\s\d{4}\b'
    aadhaar_match = re.search(aadhaar_pattern, ocr_text)
    if aadhaar_match:
        data["aadhaar_number"] = aadhaar_match.group(0)

    # Regex to find a date of birth in DD/MM/YYYY or DD-MM-YYYY format.
    dob_pattern = r'\b(\d{2}[/-]\d{2}[/-]\d{4})\b'
    # We look for lines containing "DOB" or "Birth" to be more accurate.
    for line in ocr_text.split('\n'):
        if "DOB" in line or "Birth" in line:
            dob_match = re.search(dob_pattern, line)
            if dob_match:
                data["dob"] = dob_match.group(1)
                break # Stop after finding the first match

    # Find Gender by looking for specific keywords.
    if re.search(r'\b(Male|MALE)\b', ocr_text):
        data["gender"] = "Male"
    elif re.search(r'\b(Female|FEMALE)\b', ocr_text):
        data["gender"] = "Female"

    # --- Heuristic for finding the Name ---
    # The name is often a line of 2-3 capitalized words just before the DOB line.
    # This is not foolproof and is a common challenge in OCR parsing.
    lines = ocr_text.split('\n')
    dob_line_index = -1
    for i, line in enumerate(lines):
        if data["dob"] and data["dob"] in line:
            dob_line_index = i
            break
    
    if dob_line_index > 0:
        # Check the line right above the DOB line
        potential_name_line = lines[dob_line_index - 1].strip()
        # A name usually consists of 2 or 3 words and is in title or upper case.
        if 2 <= len(potential_name_line.split()) <= 3 and potential_name_line.replace(' ', '').isalpha():
            data["name"] = potential_name_line

    return data