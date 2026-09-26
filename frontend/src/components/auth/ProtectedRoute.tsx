import { Navigate } from "react-router-dom";
import type { ReactNode } from "react";
import { useAuth } from "../../hooks/useAuth";


interface ProtectedRouteProvider {
    children: ReactNode;
}

export const ProtectedRoute = ({children}:ProtectedRouteProvider) => {
    // Get the authentication state from authcontext
    const {user,loading} = useAuth();

    if(loading)
    {
       
        return "Loading...";
    }

    if(user===null){
        return <Navigate to="/"  replace />;
    }
    
    return (children);
    

};

