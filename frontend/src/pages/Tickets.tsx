import { useState, useEffect } from "react";
import {fetchTickets} from "../services/TicketService"
import type { PaginatedTicket } from "../types/ticket";

export const Tickets = () =>{

  const[page, setPage] = useState(1);
  const [loading, setLoading] = useState<boolean>(true);
  const[ticket, setTicket] = useState<PaginatedTicket|null>(null);
   const [error, setError] = useState<string | null>(null);

  useEffect(() => {
      const loadData = async() => {
         try{
            setError(null);
         setLoading(true);

         if (loading === true){
            console.log("Loading");
         }

         const data = await fetchTickets(page,20);
            console.log("API response:", data);

         setTicket(data);
         }
         catch (err) {
        setError(err instanceof Error ? err.message : "An error occurred");
      } finally {
        setLoading(false);
      }
      };
      loadData();
      
  },
//   Useeffect will be ran when the page changes.
  [page]);

  console.log(ticket?.total);
 return(<div>
        <h1>Tickets ({ticket?.total ?? 0})</h1>
        {loading && <p>Loading Tickets...</p>}
        {error && <p>{error}</p>}

        {!loading && !error && ticket &&(
         <div>
            {ticket.items.map((item) => (
               <div key={item.id}>
                  <h3>{item.title}</h3>
                  <p>{item.description}</p>
               </div>
            )
            )}
            </div>
        )}
    
 </div>);
};