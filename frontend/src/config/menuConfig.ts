import type { MenuItem } from "../types/menu";

 export const menuItems: MenuItem[] = [ {
        label: "Dashboard",
        path: "/dashboard",
        roles: ["Admin","Agent","User"]
    },
    {
        label: "Tickets",
        path: "/tickets",
        roles: ["Admin","Agent","User"]
    },
    {
        label: "Users",
        path: "/users",
        roles: ["Admin"]
    },
    {
        label: "Reports",
        path: "/reports",
        roles: ["Admin","Agent"]
    },
    {
        label: "Settings",
        path: "/settings",
        roles: ["Admin","Agent","User"]
    }];
