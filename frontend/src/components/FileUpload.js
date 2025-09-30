import React, { useState } from 'react';
import { verifyDocument } from '../services/apiService';
import ResultDisplay from './ResultDisplay';
import Spinner from './Spinner';

const FileUpload = () => {
  const [selectedFile, setSelectedFile] = useState(null);
  const [uploadResult, setUploadResult] = useState(null);
  const [isLoading, setIsLoading] = useState(false);

  const handleFileChange = (event) => {
    setSelectedFile(event.target.files[0]);
    setUploadResult(null);
  };

  const handleUpload = async () => {
    if (!selectedFile) {
      alert("Please select a file first!");
      return;
    }
    setIsLoading(true);
    setUploadResult(null);
    const result = await verifyDocument(selectedFile);
    setUploadResult(result);
    setIsLoading(false);
  };

  return (
    // We apply the 'upload-card' class to the main container
    <div className="upload-card">
      <h2>Upload Your Document</h2>
      
      {/* Wrapper for our custom-styled file input */}
      <div className="file-input-wrapper">
        <input 
          type="file" 
          id="file" 
          className="file-input" 
          onChange={handleFileChange} 
        />
        {/* This label is what the user sees and clicks */}
        <label htmlFor="file" className="file-label">
          {selectedFile ? selectedFile.name : 'Choose a File'}
        </label>
      </div>

      <button 
        onClick={handleUpload} 
        disabled={isLoading}
        className="verify-button" // Apply the button style
      >
        {isLoading ? 'Verifying...' : 'Verify Document'}
      </button>

      {isLoading && <Spinner />}
      {!isLoading && <ResultDisplay result={uploadResult} />}
    </div>
  );
};

export default FileUpload;