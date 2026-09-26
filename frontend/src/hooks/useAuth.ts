import { useContext } from "react";
import { AuthContext } from "../contexts/AuthContext";


export const useAuth =()=>{

   const result= useContext(AuthContext);
   
   if(result===undefined){
    throw new Error("useAuth must be used within AuthProvider");
    
   }

   return result;

   
};