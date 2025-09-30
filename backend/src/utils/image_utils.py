# backend/src/utils/image_utils.py

import cv2
import numpy as np

def read_image_from_bytes(image_bytes: bytes) -> np.ndarray:
    """
    Decodes an image from a byte stream into an OpenCV image format (numpy array).
    """
    # Convert bytes to a numpy array
    nparr = np.frombuffer(image_bytes, np.uint8)
    # Decode the array into an image
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    return img

def apply_gaussian_blur(image: np.ndarray, kernel_size=(5, 5)) -> np.ndarray:
    """
    Applies a Gaussian blur to an image to reduce noise.
    """
    if image is None:
        return None
    
    blurred_image = cv2.GaussianBlur(image, kernel_size, 0)
    return blurred_image 
