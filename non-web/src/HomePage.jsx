import React, { useState } from 'react';
import { Link } from 'react-router-dom';

function HomePage() {
  const [count, setCount] = useState(0);

  // การใช้ฟังก์ชัน updater ช่วยให้แน่ใจว่าค่านับเป็นปัจจุบัน
  const incrementCount = () => setCount(prevCount => prevCount + 1);

  return (
    <div>
      <h1>Vite + React</h1>
      <div className="card">
        <button onClick={incrementCount} aria-label="Increment counter">
          count is {count}
        </button>
        <p>Edit <code>src/App.jsx</code> and save to test HMR (Hot Module Replacement)</p>
      </div>
      <p className="read-the-docs">
        Click on the Vite and React logos to learn more
      </p>
      <Link to="/about" className="link-to-about">Go to About Page</Link>
    </div>
  );
}

export default HomePage;
