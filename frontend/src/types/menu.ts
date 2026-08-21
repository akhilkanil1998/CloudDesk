export type Role = "Admin" | "Agent" | "User";

export interface MenuItem {
    label: string;
    path: string;
    roles: Role[];
}