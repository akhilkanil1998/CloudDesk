import type { ReactElement } from "react";
import type { Roles } from "../types/roles";
import { Dashboard } from "../pages/Dashboard";
import { Tickets } from "../pages/Tickets";
import { CreateTicketForm } from "../components/tickets/CreateTicket";

export interface RouteConfigProps  {
    path: string;
    element: ReactElement;
    allowedRoles: Roles[];
};


export const routes: RouteConfigProps[] = [
   {path: "/dashboard", element: <Dashboard/>, allowedRoles: ["Admin", "Agent", "User"]},
   {path: "/tickets", element: <Tickets/>, allowedRoles: ["Admin", "Agent", "User"]},
   {path: "/tickets/create", element: <CreateTicketForm/>, allowedRoles: ["Admin", "User"]}
   
];


