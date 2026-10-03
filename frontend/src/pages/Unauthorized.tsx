import { Link } from "react-router-dom";


export const Unauthorized =() =>{
    return(
        <div>
        <h1>Access Denied...</h1>

        <h4>You do not have permission to view this page.</h4>

        <Link to="/dashboard">Go to Dashboard</Link>

        </div>
    );
};