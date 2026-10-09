
import { useAuth } from "../hooks/useAuth";
import "./css/dashboard.css";



export const Dashboard = () => {

    const {user,loading} = useAuth();

     if (loading) {
        return <h1>Still loading</h1>;
    }

    if (user === null) {
        return null;
    }
     
    return (       
          
        
        <main className="dashboard-content">
            
                <h1>
                    Welcome to CloudDesk Dashboard,{" "}
                    {user.employee_name}-{user.role}
                </h1>
            </main>
         
       
           
        );
};