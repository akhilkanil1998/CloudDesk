import type { ReactElement } from "react";
import type { Roles } from "../types/roles";
import { Dashboard } from "../pages/Dashboard";

export interface RouteConfigProps  {
    path: string;
    element: ReactElement;
    allowedRoles: Roles[];
};


export const routes: RouteConfigProps[] = [
   {path: "/dashboard", element: <Dashboard/>, allowedRoles: ["Admin", "Agent", "User"]},
   
   
];


