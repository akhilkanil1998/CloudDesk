import {Sidebar} from "../components/layout/Sidebar"
import { useAuth } from "../hooks/useAuth";



export const Dashboard = () => {

    const {user,loading} = useAuth();
     if(user===null){
            throw new Error("User is null.");            
         }
    return (       
        <div>        
        {loading?<h1>Still loading</h1>:<><h1>Welcome to CloudDesk Dashboard, {user.employee_name}-{user.role}</h1>
        <Sidebar/>
        </>
         }
        </div>     
        );
};