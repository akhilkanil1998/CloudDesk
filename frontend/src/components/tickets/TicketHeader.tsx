import { useNavigate } from "react-router-dom";
interface TicketHeaderProps {
  total: number;
}

export const TicketHeader = ({ total }: TicketHeaderProps) => {

     const navigate = useNavigate();
  return (
    <div className="ticket-header">
      <h1>Tickets ({total})</h1>
      <button
        className="create-ticket-button"
        onClick={() => navigate("/tickets/create")}
      >
        &nbsp;Create&nbsp;
      </button>
    </div>
  );
};
