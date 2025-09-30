import React from 'react';
import './App.css';
import FileUpload from './components/FileUpload'; // Import our new component

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Document Verification App</h1>
        {/* Render the FileUpload component here */}
        <FileUpload />
      </header>
    </div>
  );
}

export default App;