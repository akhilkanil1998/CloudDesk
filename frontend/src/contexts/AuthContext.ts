import {  createContext } from "react";
import type { Roles } from "../types/roles";

// This interface would be returned.
export interface User {
    employee_id: string;
    email: string;
    employee_name: string;
    role: Roles;
}
// this is for what data should Context provide
interface AuthContextType{
    user: User | null;
    loading: boolean

}

// Create a React Context(like a container) whose value will either be AuthContextType or undefined.
// default value will be undefined which is set inside the ().
export const AuthContext = createContext<AuthContextType | undefined>(undefined);