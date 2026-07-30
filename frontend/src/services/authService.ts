import { loginUser } from "../api/authApi";

export const login = async (email:string, password:string) => {
    const response = await loginUser(email, password);
    return response;
};