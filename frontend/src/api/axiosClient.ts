import axios from "axios";

// Create ONE Axios instance. This instance is created to call the endpoints with this single instance.
 export const instance = axios.create();

  
instance.interceptors.request.use((config) => {
    const token = localStorage.getItem("access_token");
    // Get the latest token when the request happens.
    // Only add authentication when a token actually exists.
    if (token != null){
        config.headers.Authorization = `Bearer ${token}`;
    }    
    return config;
});



