import { getUsers } from "../api/userApi";

export const fetchUsers = async () => {
    const users = await getUsers();
    return users;
};