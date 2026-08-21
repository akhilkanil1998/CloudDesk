import {  getCurrentUser, getUsers } from "../api/userApi";

export const fetchUsers = async () => {
    const users = await getUsers();
    return users;
};

export const fetchCurrentUser = async()=> {
    const user = await getCurrentUser();
    return user;
}