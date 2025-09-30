import axios from 'axios';

// The URL of our backend API
const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000/api/v1/verify';

/**
 * Uploads a document image to the backend for verification.
 * @param {File} file The image file to be verified.
 * @returns {Promise<Object>} The verification result from the API.
 */
const verifyDocument = async (file) => {
  // Create a FormData object to send the file
  const formData = new FormData();
  formData.append('file', file);

  try {
    const response = await axios.post(API_URL, formData, {
      headers: {
        'Content-Type': 'multipart/form-data',
      },
    });
    return response.data; // Return the JSON data from the response
  } catch (error) {
    // Handle errors (e.g., network error, server error)
    console.error("Error uploading the file:", error);
    // Return a structured error object
    return {
        is_document_valid: false,
        message: error.response?.data?.detail || "An unexpected error occurred.",
        extracted_data: null,
    };
  }
};

export { verifyDocument };