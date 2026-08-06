import { useState, type SubmitEvent } from "react";
import type { loginDetails } from "../types/login";
import { login } from "../services/authService";
import "../styles/Login.css"
import logo from"../assets/clouddesk_logo.png"
import { useNavigate } from "react-router-dom";
import { FaEye, FaEyeSlash } from "react-icons/fa";


export const Login = () => {

    const navigate = useNavigate();
    const [loginDetails, setLoginDetails] = useState<loginDetails>({
        email: "",
        password: ""
    });    

    const[showPassword, setShowPassword] = useState(false);
   const togglePassword = () => {
    setShowPassword(!showPassword);
};
    const handleLogin = async ( event: SubmitEvent<HTMLFormElement>) => {
    event.preventDefault();
console.log("Login clicked");
    const response = await login(loginDetails.email, loginDetails.password);
 console.log(response);
    localStorage.setItem("access_token", response.access_token);
     console.log("Navigating...");
    navigate("/dashboard");
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
       <span>Invalid login credentials</span>
        <button type="submit" className="login-button">
            Login
        </button>
        <div className="form-links">
        <div className="forgot-password">
            <a href="">Forgot Passord?</a>
        </div>

        <div className="signup">
            
            <a href=""> Sign Up</a>
        </div>

        </div>
         <div className="logo-container">
                <img src={logo} 
                    alt="clouddesk_logo" className="logo" />
            </div>

    </form>
    </div>
    </div>
</div>);
};