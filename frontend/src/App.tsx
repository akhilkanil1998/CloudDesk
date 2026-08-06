import { BrowserRouter, Routes, Route } from "react-router-dom";
import { Login } from "./pages/Login";
import { Dashboard } from "./pages/Dashboard";
// Component in react.
function App(){
   return (
    // BrowserRouter- Watches the browser URL and keeps React in sync with it.
        <BrowserRouter>
        {/* Routes - A container that decides which page should be displayed. */}
            <Routes>
                {/* Actual routing happens here. */}
                <Route path="/" element={<Login />} />
                <Route path="/dashboard" element={<Dashboard />} />
            </Routes>
        </BrowserRouter>
    );
}

export default App;