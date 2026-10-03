import { type ReactNode } from "react";
import type { Roles } from "../../types/roles";
import { useAuth } from "../../hooks/useAuth";
import { Navigate } from "react-router-dom";


export interface RoleGuardProps {
    allowedRoles: Roles[],
    children: ReactNode

}

export const RoleGuard = (roleGuardData: RoleGuardProps) =>
{
    const {user,loading} = useAuth();

    if(loading){
      return( <h1> checking authorization...</h1>);
    }
    else if(user=== null){
         return <Navigate to="/" replace/>; 
    
    }
    
    if(!roleGuardData.allowedRoles.includes(user.role))
    {
        return <Navigate to="/unauthorized" replace />; 
        
    }  
    else{
        return(roleGuardData.children);
    }
    
    
}