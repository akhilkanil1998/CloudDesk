import {Link} from "react-router-dom"
import { menuItems } from "../../config/menuConfig"
import "./css/sidebar.css"
import logo from "../../assets/Clouddesk log new.png"
export const Sidebar = () =>{

    
   
    return (
        <aside className="sidebar">
        <nav>
            <div className="logo-sidebar-container">
        <img src={logo} 
                    alt="clouddesk_logo" className="logo-sidebar" />
                    </div>
        {menuItems.map((item) => (
        <div className="menu-items" key={item.path}>
        <Link to={item.path}>{item.label}</Link>
        </div>
        ))}
</nav>
</aside>)
}