import { FiEdit2 } from "react-icons/fi";
import type { PaginatedTicket } from "../../types/ticket";

interface TicketTableProps {
  tickets: PaginatedTicket["items"];
  loading: boolean;
  error: string | null;
  onEdit: (id: number) => void;
}

export const TicketTable = ({
  tickets,
  loading,
  error,
  onEdit,
}: TicketTableProps) => {
  if (loading) {
    return <p>Loading Tickets...</p>;
  }

  if (error) {
    return <p>{error}</p>;
  }

  return (
    <div className="tickets-table-container">
      <table className="tickets-table">
        <thead>
          <tr>
            <th>Id</th>
            <th>Title</th>
            <th>Status</th>
            <th>Priority</th>
            <th>Assigned To</th>
            <th>Created By</th>
            <th>Created On</th>
            <th></th>
          </tr>
        </thead>

        <tbody>
          {tickets.map((item) => (
            <tr key={item.id}>
              <td>{item.id}</td>
              <td>{item.title}</td>

              <td>
                <span
                  className={`status-badge status-${item.status
                    .toLowerCase()
                    .replace(" ", "-")}`}
                >
                  {item.status}
                </span>
              </td>

              <td>
                <span
                  className={`priority-badge priority-${item.priority.toLowerCase()}`}
                >
                  {item.priority}
                </span>
              </td>

              <td>{item.assigned_to_name}</td>
              <td>{item.created_by_name}</td>
              <td>{new Date(item.created_on).toLocaleDateString("en-IN")}</td>

              <td>
                <button
                  className="action-btn edit-btn"
                  onClick={() => onEdit(item.id)}
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
  );
};
