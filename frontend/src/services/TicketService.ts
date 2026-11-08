import { createTicket, fetchPaginatedTickets } from "../api/ticketsApi";
import type {
  TicketStatus,
  TicketPriority,
  CreateTicket,
} from "../types/ticket";

export const fetchTickets = async (
  page: number,
  page_size: number,
  status?: TicketStatus,
  priority?: TicketPriority,
) => {
  return await fetchPaginatedTickets(page, page_size, status, priority);
};

export const CreateTicketService = async (ticket: CreateTicket) => {
  return await createTicket(ticket);
};
