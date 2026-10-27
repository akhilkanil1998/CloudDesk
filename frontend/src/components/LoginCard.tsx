import { useState, type SubmitEvent } from "react";
import type { LoginDetails } from "../types/login";
import { login } from "../services/AuthService";
import "../styles/Login.css"
import logo from"../assets/clouddesk_logo.png"
import { useNavigate } from "react-router-dom";
import { FaEye, FaEyeSlash } from "react-icons/fa";
import axios from "axios";
import { useContext } from "react";
import { AuthContext } from "../contexts/AuthContext";

export const LoginCard = ()=>{
    const navigate = useNavigate();
    const [loginDetails, setLoginDetails] = useState<LoginDetails>({
        email: "",
        password: ""
    });    
    
    const [loginError, setLoginError] = useState("");

    const[showPassword, setShowPassword] = useState(false);
   const togglePassword = () => {
    setShowPassword(!showPassword);
    };

    const authContext = useContext(AuthContext);

    if (!authContext) {
        throw new Error("LoginCard must be inside AuthProvider");
    }

    const { refreshUser } = authContext;

      
    const handleLogin = async ( event: SubmitEvent<HTMLFormElement>) => {
    event.preventDefault();

    if(!loginDetails.email && !loginDetails.password)
    {
        setLoginError("Enter your email and password");
        return;
    }

     if (!loginDetails.email) {
        setLoginError("Please enter your email");
        return;
    }

    if (!loginDetails.password) {
        setLoginError("Please enter your password");
        return;
    }

    try{
        const response = await login(loginDetails.email, loginDetails.password);
        localStorage.setItem("access_token", response.access_token);   
        // Fetch the logged-in user's details and update Context.
        await refreshUser();
        console.log("Login successful - navigating");     
        navigate("/dashboard");
    }
    catch(error)
    {
        if (axios.isAxiosError(error) && error.response?.status === 401) {
            setLoginError("Invalid login credentials");
        }
        else {
        localStorage.removeItem("access_token");
        setLoginError("Login failed. Please try again.");
        console.error("Login or user initialization failed", error);
    }
    }
    
 
    
    
};  

return(
<div className="login-card">
         <form className="login-form" onSubmit={handleLogin}>
        <div className="form-group">
           
             <h2 className="form-text">Welcome Back</h2>

        <p className="form-text">
            Sign in to your CloudDesk account
        </p>
        
        <input
            type="email"
            placeholder="Email"
            value={loginDetails.email}
            onChange={(event)=> {
                setLoginDetails(
                {
                    // Keep everythings that is already inside the object.
                    ...loginDetails,
                    email: event.target.value
                }
            )
            setLoginError("");
            }}
        />
        </div>
        
        <div className="form-group">
        <div className="password-container">
        <input
            type={showPassword ? "text" : "password"}
            placeholder="Password"
            value={loginDetails.password}
            onChange={(event)=> {
                setLoginDetails(
                {
                    // Keep everythings that is already inside the object.
                    ...loginDetails,
                    password: event.target.value
                }
            )
            setLoginError("");
            }}
        />
        <button
            type="button"
            className="toggle-password"
           onClick={togglePassword}>

            {showPassword ? <FaEyeSlash /> : <FaEye />}
        </button>
        </div>
       </div>
        <div className="form-links">
        <div className="forgot-password">
            <a href="">Forgot Password?</a>
        </div>
    
        </div>
       <span className="error">{loginError}</span>
        <button type="submit" className="login-button">
            Login
        </button>
       
         <div className="logo-container">
                <img src={logo} 
                    alt="clouddesk_logo" className="logo" />
            </div>

    </form>
    </div>
);
        
};