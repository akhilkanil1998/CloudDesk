import { useAuth } from "../../hooks/useAuth";
import "./css/header.css"
export const Header = () =>{
    const {user} = useAuth();
    

    if (user === null) {
        return null;
    }
    return(
        <div className="header">
                <h5>{user.employee_name}</h5>
        </div>
    );
};