import { type ReactNode } from "react";
import type { Roles } from "../../types/roles";
import { useAuth } from "../../hooks/useAuth";


export interface RoleGuardProps {
    allowedRoles: Roles[],
    children: ReactNode

}

export const RoleGuard = (roleGuarddata: RoleGuardProps) =>
{
    const {user,loading} = useAuth();

    if(loading){
      return( <h1> checking authorization...</h1>);
    }
    else if(user=== null){
        throw new Error("Unauthorized");
    
    }
    
    if(!roleGuarddata.allowedRoles.includes(user.role))
    {
        throw new Error("Unauthorized");        
        
    }  
    else{
        return(roleGuarddata.children);
    }
    
}