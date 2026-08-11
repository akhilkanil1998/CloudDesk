import { useState, type SubmitEvent } from "react";
import type { loginDetails } from "../types/login";
import { login } from "../services/authService";
import "../styles/Login.css"
import logo from"../assets/clouddesk_logo.png"
import { useNavigate } from "react-router-dom";
import { FaEye, FaEyeSlash } from "react-icons/fa";
import axios from "axios";


export const Login = () => {

    const navigate = useNavigate();
    const [loginDetails, setLoginDetails] = useState<loginDetails>({
        email: "",
        password: ""
    });    
    
    const [loginError, setLoginError] = useState("");

    const[showPassword, setShowPassword] = useState(false);
   const togglePassword = () => {
    setShowPassword(!showPassword);
    };

      
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
        navigate("/dashboard");
    }
    catch(error)
    {
        if (axios.isAxiosError(error) && error.response?.status === 401) {
            setLoginError("Invalid login credentials");
        }
    }
    
 
    
    
};  

    return (<div className="login-page">
        {/* Left Form */}
    <div className="left-panel">
        <div className="branding">        
        <h1>CloudDesk</h1>
        <h2>Manage Support Smarter</h2>

        <p>
            Streamline ticket management, collaborate with your team,
            and deliver exceptional customer support from one place.
        </p>
        </div>
    </div>
   

    {/*  Login form */}
    <div className="right-panel">
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
    </div>
</div>);
};