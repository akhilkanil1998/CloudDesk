import { BrowserRouter, Routes, Route } from "react-router-dom";
import { Login } from "./pages/Login";
import { Dashboard } from "./pages/Dashboard";
import { AuthProvider } from "./contexts/AuthProvider";
import { ProtectedRoute } from "./components/auth/ProtectedRoute";
import { Unauthorized } from "./pages/Unauthorized";
import { AppLayout } from "./components/layout/AppLayout";
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
                <Route path="/unauthorized" element={<Unauthorized />} />

                {/* This dashboard element should be rendered if the user is authenticated. 
                For that ProtectedRoute is used */}
                <Route element={<ProtectedRoute />}>
                        <Route element={<AppLayout />}>
                            <Route
                                path="/dashboard"
                                element={<Dashboard />}
                            />
                            
                           
                        </Route>
                    </Route>
            </Routes>
            </AuthProvider>
        </BrowserRouter>
    );
}

export default App;