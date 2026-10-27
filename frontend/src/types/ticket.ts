export interface Ticket{
    id: number;
    title: string;
    description: string;
    status: string;
    priority: string;

}

export interface PaginatedTicket{
    items: Ticket[];
    page: number;
    page_size: number;
    total: number;
    total_pages: number;
}

export type TicketStatus =
  | "OPEN"
  | "IN_PROGRESS"
  | "RESOLVED"
  | "CLOSED";

export type TicketPriority =
  | "LOW"
  | "HIGH"
  | "URGENT";