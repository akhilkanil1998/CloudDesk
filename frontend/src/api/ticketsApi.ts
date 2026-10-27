import { instance } from "./axiosClient"
import type {TicketStatus,TicketPriority,PaginatedTicket} from "../types/ticket"


export const fetchPaginatedTickets = async(page:number,
    page_size: number, status?:TicketStatus, priority?:TicketPriority):Promise<PaginatedTicket> => 
        {
    const response = await instance.get<PaginatedTicket>("/tickets",{
    params: {
      page,
      page_size,
      status,
      priority,
    },

    });
    return  response.data;
    };