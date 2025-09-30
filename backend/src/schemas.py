 
# backend/src/schemas.py

from pydantic import BaseModel
from typing import Optional, Dict

class VerificationResult(BaseModel):
    """
    Defines the structure of the JSON response for a verification request.
    """
    is_document_valid: bool
    message: str
    extracted_data: Optional[Dict[str, str]] = None
    error_code: Optional[str] = None

class VerificationError(BaseModel):
    """
    Defines the structure for an error response.
    """
    detail: str