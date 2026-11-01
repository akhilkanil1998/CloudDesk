import { useState, useEffect } from "react";
import { fetchTickets } from "../services/TicketService";
import type { PaginatedTicket } from "../types/ticket";
import { TicketHeader } from "../components/tickets/TicketHeader";
import { TicketTable } from "../components/tickets/TicketTable";
import "./css/tickets.css";
import { Pagination } from "../components/common/Pagination";

export const Tickets = () => {
  const [page, setPage] = useState(1);
  const [loading, setLoading] = useState(true);
  const [ticket, setTicket] = useState<PaginatedTicket | null>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const loadData = async () => {
      try {
        setError(null);
        setLoading(true);

        const data = await fetchTickets(page, 20);
        setTicket(data);
      } catch (err) {
        setError(err instanceof Error ? err.message : "An error occurred");
      } finally {
        setLoading(false);
      }
    };

    loadData();
  }, [page]);

  const handleEdit = (id: number) => {
    console.log("Edit ticket:", id);
  };

  return (
    <div className="tickets-page">
      <TicketHeader total={ticket?.total ?? 0} />

      <TicketTable
        tickets={ticket?.items ?? []}
        loading={loading}
        error={error}
        onEdit={handleEdit}
      />

      <Pagination
        currentPage={page}
        totalPages={ticket?.total_pages ?? 0}
        onPageChange={setPage}
      ></Pagination>
    </div>
  );
};
