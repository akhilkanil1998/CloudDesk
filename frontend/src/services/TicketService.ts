import { fetchPaginatedTickets } from "../api/ticketsApi"
import type {
  TicketStatus, 
  TicketPriority,
} from "../types/ticket";


export const fetchTickets = async ( page: number,
  page_size: number,
  status?: TicketStatus,
  priority?: TicketPriority) => 
    {
    return await fetchPaginatedTickets(page,
    page_size,
    status,
    priority);
    
}