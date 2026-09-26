import { BrowserRouter, Routes, Route } from "react-router-dom";
import { Login } from "./pages/Login";
import { Dashboard } from "./pages/Dashboard";
import { AuthProvider } from "./contexts/AuthProvider";
import { ProtectedRoute } from "./components/auth/ProtectedRoute";
// Component in react.
function App(){
   return (
    // BrowserRouter- Watches the browser URL and keeps React in sync with it.
        <BrowserRouter>
        <AuthProvider>
        {/* Routes - A container that decides which page should be displayed. */}
            <Routes>
                {/* Actual routing happens here. */}
                <Route path="/" element={<Login />} />
                {/* This dashboard element should be rendered if the user is authenticated. 
                For that ProtectedRoute is used */}
                <Route path="/dashboard" element={<ProtectedRoute>
            <Dashboard />
            </ProtectedRoute>
            } />
               
            </Routes>
            </AuthProvider>
        </BrowserRouter>
    );
}

export default App;