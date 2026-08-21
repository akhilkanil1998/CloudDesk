import {LoginCard} from "../components/LoginCard";


export const Login = () => {


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
        {/* calls the logincard component which has the login functionality */}
        <LoginCard/>
    </div>
</div>);
};