import { useState } from "react";
import type { loginDetails } from "../types/login";
import { login } from "../services/authService";

export const Login = () => {

    const [loginDetails, setLoginDetails] = useState<loginDetails>({
        email: "",
        password: ""
    });

   

    return (
    <form onSubmit={async (event) =>{
        event.preventDefault();
       const response =  await login(loginDetails.email, loginDetails.password);
       
       const token = response.access_token;
       localStorage.setItem("access_token", token);
    }}>
        <input
            type="email"
            value={loginDetails.email}
            onChange={(event)=> {
                setLoginDetails(
                {
                    // Keep everythings that is already inside the object.
                    ...loginDetails,
                    email: event.target.value
                }
            )
            }}
        />
        <input
            type="password"
            value={loginDetails.password}
            onChange={(event)=> {
                setLoginDetails(
                {
                    // Keep everythings that is already inside the object.
                    ...loginDetails,
                    password: event.target.value
                }
            )
            }}
        />
        <button type="submit" >
            Login
        </button>
    </form>
);

};