
import { Header } from "../components/layout/Header";
import {Sidebar} from "../components/layout/Sidebar"
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
        <div className="dashboard-layout">        
        
        <Sidebar/>
   
        
        <main className="dashboard-content">
            <Header />
                <h1>
                    Welcome to CloudDesk Dashboard,{" "}
                    {user.employee_name}-{user.role}
                </h1>
            </main>
         
        </div>
           
        );
};