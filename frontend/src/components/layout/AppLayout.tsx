import { Header } from "./Header";
import { Sidebar } from "./Sidebar";
import { Outlet } from "react-router-dom"; 
import "./css/appLayout.css"

export const AppLayout = () =>
{
    return (
<div className="app-layout">
            <Sidebar />

            <div className="main-area">
                <Header />

                <main className="page-content">
                   <Outlet />
                </main>
            </div>
        </div>

    );

};