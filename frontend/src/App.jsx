import { useState, useEffect } from 'react';

function App() {
  const [text, setText] = useState("Waiting for backend...");

  useEffect(() => {
    fetch('http://localhost:8080/hello')
        .then(res => res.json())
        .then(data => setText(data.message))
        .catch(err => setText("Error: " + err.message));
  }, []);

  return (
      <div style={{ textAlign: 'center', marginTop: '50px' }}>
        <h1>My App</h1>
        <p style={{ fontSize: '20px', color: 'blue' }}>{text}</p>
      </div>
  );
}

export default App;
