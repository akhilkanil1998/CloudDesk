import {Link} from "react-router-dom"
import { menuItems } from "../../config/menuConfig"

export const Sidebar = () =>{

   
    return (
        <aside>
        <nav>
        {menuItems.map((item) => (
        <div className="menu-items" key={item.path}>
        <Link to={item.path}>{item.label}</Link>
        </div>
        ))}
</nav>
</aside>)
}