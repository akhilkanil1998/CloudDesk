import type{ Roles } from "./roles";

export interface MenuItem {
    label: string;
    path: string;
    roles: Roles[];
}