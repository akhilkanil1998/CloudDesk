export interface Ticket{
    id: number;
    title: string;
    description: string;
    status: string;
    priority: string;
    assigned_to_name: string;
    created_by_name: string;
    modified_by_name: string;

}

export interface PaginatedTicket{
    items: Ticket[];
    page: number;
    page_size: number;
    total: number;
    total_pages: number;
}

export type TicketStatus =
  | "Open"
  | "In Progress"
  | "Resolved"
  | "Closed";

export type TicketPriority =
  | "Low"
  | "High"
  | "Urgent";