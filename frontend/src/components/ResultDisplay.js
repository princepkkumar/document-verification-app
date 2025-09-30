import React from 'react';

// A simple component to display the verification result
const ResultDisplay = ({ result }) => {
  // If there's no result yet, render nothing
  if (!result) {
    return null;
  }

  const { is_document_valid, message, extracted_data } = result;
  
  // Style for the result box based on validity
  const resultStyle = {
    marginTop: '20px',
    padding: '15px',
    border: `2px solid ${is_document_valid ? 'green' : '#d9534f'}`, // Red border
    borderRadius: '8px',
    backgroundColor: is_document_valid ? '#e9f7ef' : '#fdf7f7', // Light red background
    color: '#333333', // <-- Set text color to dark gray for readability
    textAlign: 'left',
  };

  return (
    <div style={resultStyle}>
      <h3 style={{ color: is_document_valid ? 'green' : '#d9534f', marginTop: 0 }}>
        {is_document_valid ? '✓ Document Valid' : '✗ Document Invalid'}
      </h3>
      <p><strong>Status:</strong> {message}</p>
      {extracted_data && (
        <div>
          <h4 style={{marginTop: '15px', marginBottom: '5px'}}>Extracted Data:</h4>
          <ul>
            {Object.entries(extracted_data).map(([key, value]) => (
              value && <li key={key}><strong>{key.replace('_', ' ').toUpperCase()}:</strong> {value}</li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
};

export default ResultDisplay;