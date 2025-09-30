# backend/src/main.py

from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from .schemas import VerificationResult # <-- This line was missing
import os

# Import our modules
from .utils.image_utils import read_image_from_bytes, apply_gaussian_blur
from .services.ocr_service import extract_text_from_image
from .core.parser import parse_aadhaar_info
from .core.validator import validate_aadhaar_number

# Create the FastAPI application instance
app = FastAPI(
    title="Document Verification API",
    description="An API to verify KYC documents using AI/ML.",
    version="1.0.0"
)

# --- Add CORS Middleware ---
origins = [
    "http://localhost:3000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# --- End of new CORS section ---

@app.get("/", tags=["Health Check"])
async def root():
    return {"message": "Welcome to the Document Verification API!"}


@app.post("/api/v1/verify", 
            response_model=VerificationResult,
            tags=["Document Verification"])
async def verify_document_endpoint(file: UploadFile = File(...)):
    try:
        image_bytes = await file.read()

        # 1. Read and preprocess the image
        image = read_image_from_bytes(image_bytes)
        if image is None:
            raise HTTPException(status_code=400, detail="Invalid image file provided.")
        
        # 2. Extract text using OCR service
        extracted_text = extract_text_from_image(image_bytes)
        if not extracted_text:
             raise HTTPException(status_code=400, detail="No text could be extracted from the document.")
        
        # 3. Parse the extracted text to get structured data
        parsed_data = parse_aadhaar_info(extracted_text)

        # 4. Validate the Aadhaar Number
        is_number_valid = False
        aadhaar_number = parsed_data.get("aadhaar_number")
        
        if aadhaar_number:
            is_number_valid = validate_aadhaar_number(aadhaar_number)
            print(f"Aadhaar number validation result: {is_number_valid}")
        else:
            print("Aadhaar number not found in document.")

        if not aadhaar_number:
            message = "Could not find an Aadhaar number to validate."
        elif is_number_valid:
            message = "Aadhaar number is valid."
        else:
            message = "Aadhaar number is invalid."

        return VerificationResult(
            is_document_valid=is_number_valid,
            message=message,
            extracted_data=parsed_data
        )

    except Exception as e:
        raise HTTPException(
            status_code=500, 
            detail=f"An unexpected error occurred: {str(e)}"
        )