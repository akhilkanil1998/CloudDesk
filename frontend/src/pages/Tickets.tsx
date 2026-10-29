import { useState, useEffect } from "react";
import { fetchTickets } from "../services/TicketService";
import type { PaginatedTicket } from "../types/ticket";
import "./css/tickets.css";
import { FiEdit2 } from "react-icons/fi";

export const Tickets = () => {
  const [page, setPage] = useState(1);
  const [loading, setLoading] = useState<boolean>(true);
  const [ticket, setTicket] = useState<PaginatedTicket | null>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(
    () => {
      const loadData = async () => {
        try {
          setError(null);
          setLoading(true);

          if (loading === true) {
            console.log("Loading");
          }

          const data = await fetchTickets(page, 20);
          console.log("API response:", data);

          setTicket(data);
        } catch (err) {
          setError(err instanceof Error ? err.message : "An error occurred");
        } finally {
          setLoading(false);
        }
      };
      loadData();
    },
    //   Useeffect will be ran when the page changes.
    [page],
  );

  console.log(ticket);
  return (
    <div className="tickets-page">
      <h1>Tickets ({ticket?.total ?? 0})</h1>
      {loading && <p>Loading Tickets...</p>}
      {error && <p>{error}</p>}
      <div className="tickets-table-container">
        <table className="tickets-table">
          <thead>
            <tr>
              <th>Ticket id</th>
              <th>Title</th>
              <th>Status</th>
              <th>Priority</th>
              <th>Assigned To</th>
              <th>Created By</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            {!loading &&
              !error &&
              ticket &&
              ticket.items.map((item) => (
                <tr key={item.id}>
                  <td>{item.id}</td>
                  <td>{item.title}</td>
                  <td>
                    <span
                      className={`status-badge status-${item.status.toLowerCase().replace(" ", "-")}`}
                    >
                      {item.status}
                    </span>
                  </td>
                  <td>
                    <span
                      className={`priority-badge priority-${item.priority.toLowerCase()}`}
                    >
                      {item.priority}{" "}
                    </span>
                  </td>
                  <td>{item.assigned_to_name}</td>
                  <td>{item.created_by_name}</td>
                  <td>
                    <button
                      className="action-btn edit-btn"
                      // onClick={() => handleEdit(item.id)}
                      title="Edit ticket"
                      aria-label={`Edit ticket ${item.id}`}
                    >
                      <FiEdit2 />
                    </button>
                  </td>
                </tr>
              ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};
