 
# backend/src/core/validator.py

# Verhoeff algorithm lookup tables
d = [
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 0, 6, 7, 8, 9, 5],
    [2, 3, 4, 0, 1, 7, 8, 9, 5, 6],
    [3, 4, 0, 1, 2, 8, 9, 5, 6, 7],
    [4, 0, 1, 2, 3, 9, 5, 6, 7, 8],
    [5, 9, 8, 7, 6, 0, 4, 3, 2, 1],
    [6, 5, 9, 8, 7, 1, 0, 4, 3, 2],
    [7, 6, 5, 9, 8, 2, 1, 0, 4, 3],
    [8, 7, 6, 5, 9, 3, 2, 1, 0, 4],
    [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],
]

p = [
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 5, 7, 6, 2, 8, 3, 0, 9, 4],
    [5, 8, 0, 3, 7, 9, 6, 1, 4, 2],
    [8, 9, 1, 6, 0, 4, 3, 5, 2, 7],
    [9, 4, 5, 3, 1, 2, 6, 8, 7, 0],
    [4, 2, 8, 6, 5, 7, 3, 9, 0, 1],
    [2, 7, 9, 3, 8, 0, 6, 4, 1, 5],
    [7, 0, 4, 6, 9, 1, 3, 2, 5, 8],
]

inv = [0, 4, 3, 2, 1, 5, 6, 7, 8, 9]

def _generate_checksum(uid_string: str) -> str:
    """Generates the Verhoeff checksum digit for a given UID string."""
    c = 0
    for i, item in enumerate(reversed(uid_string)):
        c = d[c][p[(i + 1) % 8][int(item)]]
    return str(inv[c])

def validate_aadhaar_number(aadhaar_string: str) -> bool:
    """
    Validates a 12-digit Aadhaar number using the Verhoeff algorithm.

    Args:
        aadhaar_string: The 12-digit Aadhaar number as a string.

    Returns:
        True if the number is valid, False otherwise.
    """
    # Remove spaces and check if it's a 12-digit number
    cleaned_number = aadhaar_string.replace(" ", "")
    if not (cleaned_number.isdigit() and len(cleaned_number) == 12):
        return False

    uid = cleaned_number[:11]
    checksum = cleaned_number[11]

    # Generate the checksum for the first 11 digits and compare it
    # with the 12th digit.
    return checksum == _generate_checksum(uid)