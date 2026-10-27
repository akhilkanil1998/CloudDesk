
import { instance } from "./axiosClient";

export const loginUser = async (email: string, password: string) => {

    const formData = new URLSearchParams();

    // OAuth2PasswordRequestForm expects the field to be named username.
    formData.append("username", email);
    formData.append("password", password);

    const response = await instance.post("/auth/login", formData);
    
    return response.data; 
};