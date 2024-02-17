import React from "react";
import { BrowserRouter as Router, Routes, Route, useNavigate } from "react-router-dom";
import HomePage from "./components/HomePage"; // ทางเข้าสู่ HomePage component
import TestPage from "./components/TestPage"; // ทางเข้าสู่ TestPage component

// สร้าง component สำหรับปุ่มนำทาง
function NavigateButton({ to, children }) {
  let navigate = useNavigate();
  return (
    <button onClick={() => navigate(to)}>{children}</button>
  );
}

function App() {
  return (
    <Router>
      <div>
        <body>

        
        {/* ปุ่มสำหรับนำทาง */}
        <NavigateButton to="/">Home</NavigateButton>
        <NavigateButton to="/test">Test</NavigateButton>

        {/* Route paths */}
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/test" element={<TestPage />} />
        </Routes>
        </body>
      </div>
    </Router>
  );
}

export default App;
