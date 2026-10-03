import { Navigate, Outlet } from "react-router-dom";
import { useAuth } from "../../hooks/useAuth";


export const ProtectedRoute = () => {
    // Get the authentication state from authcontext
    const {user,loading} = useAuth();
  console.log("ProtectedRoute:", { user, loading });
    if(loading)
    {
       
        return "Loading...";
    }

    if(user===null){
        return <Navigate to="/"  replace />;
    }
    
    return <Outlet/>;
    

};

