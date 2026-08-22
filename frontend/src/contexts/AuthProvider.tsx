// Context API in React provides a way to share data globally across components without prop drilling. 
// It allows creating a lightweight global state accessible by any component.

import { useState, useEffect, type ReactNode } from "react";
import { AuthContext, type User } from "./authContext";
import { fetchCurrentUser } from "../services/UserService";


// This is to show who is allowed inside the Provider
interface AuthProviderProps{
    children: ReactNode;
}



// children is a prop here. 
// The prop coming into this function must follow AuthProviderProps.
export const AuthProvider = ({children}: AuthProviderProps) => {

    // user is initially null
    // user → actual current value
    // setUser  → function to change it
    // useState → gives us a place to store user
    // fetchCurrentUser() → gets user from backend
    // setUser(user) → puts backend result into that state
    const [user, setUser] = useState<User|null> (null);
    // loading is initially true.
    const [loading, setLoading] = useState<boolean>(true);

    // this is used how we should load the current user.
    useEffect(() => {
    // this is the function which will run when the page loads to get the user.
    const loadCurrentUser = async() => {
        const token = localStorage.getItem("access_token");
        // Before calling /user/me, check whether we even have a token.
        // We don't call /user/me because there's no token to authenticate the request.
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
        // Every component inside me can access user and loading.
        <AuthContext.Provider value={{user, loading}}> 
            {children}
        </AuthContext.Provider>
    )
};

