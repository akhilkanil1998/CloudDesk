// Context API in React provides a way to share data globally across components without prop drilling. 
// It allows creating a lightweight global state accessible by any component.
import {  createContext, useState, type ReactNode, useEffect } from "react";
import { fetchCurrentUser } from "../services/UserService";

// This interface would be returned.
interface User {
    employee_id: string;
    email: string;
    employee_name: string;
    role: string;
}

interface AuthContextType{
    user: User | null;
    loading: boolean

}

interface AuthProviderProps{
    children: ReactNode;
}

// Create a React Context(like a container) whose value will either be AuthContextType or undefined.
export const AuthContext = createContext<AuthContextType | undefined>(undefined);


export const AuthProvider = ({children}: AuthProviderProps) => {
    // user is initially null
    // user → actual current value
    // setUser  → function to change it
    const [user, setUser] = useState<User|null> (null);
    // loading is initially true.
    const [loading, setLoading] = useState<boolean>(true);

   useEffect(() => {
    const loadCurrentUser =async() => {
        const token = localStorage.getItem("access_token");
         if (!token) {
            setLoading(false);
            return;
         }

        try {
            const user = await fetchCurrentUser();
            setUser(user);
        } catch (error) {
            console.error("Failed to fetch current user", error);
        } finally {
            setLoading(false);
        }
        };   
   
     loadCurrentUser();
     // [] - Run this effect when AuthProvider mounts.
   },[]);


    return (
        <AuthContext.Provider value={{user, loading}}> 
            {children}
        </AuthContext.Provider>
    )
};

