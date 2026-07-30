import { instance } from "./axiosClient";

// export       → make this function available to other files
// const        → create a variable that can't be reassigned
// getUsers     → function name
// ()           → no parameters
// =>           → arrow function
// {}           → function body
export const getUsers = async () =>{
    
        const response =  await instance.get("/user/users");
        return response.data; 
};

