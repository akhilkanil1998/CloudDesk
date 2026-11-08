import type { CreateTicket, TicketPriority } from "../../types/ticket";
import "./css/createTicket.css";
import { useNavigate } from "react-router-dom";
import { CreateTicketService } from "../../services/TicketService";
import { useNotification } from "../../hooks/useNotification";

export const CreateTicketForm = () => {
  const priorities: TicketPriority[] = ["Low", "High", "Urgent"];
  const navigate = useNavigate();
  const { showSuccess, showError } = useNotification();

  const handleSubmit = async (event: React.FormEvent<HTMLFormElement>) => {
    console.log("inside handleSubmit");
    // Prevent browser from reloading the page.
    event.preventDefault();

    const data = new FormData(event.currentTarget);
    const title = data.get("title");
    const description = data.get("description");
    const priority = data.get("priority");

    if (
      typeof title !== "string" ||
      typeof description !== "string" ||
      typeof priority !== "string"
    ) {
      console.log("Inside if");
      console.log(typeof priorities);
      console.log(typeof title);
      console.log(typeof description);

      return;
    }

    const payload: CreateTicket = {
      title: title,
      description: description,
      priority: priority,
    };
    console.log(payload);

    try {
      console.log("inside try block");
      await CreateTicketService(payload);
      showSuccess("Ticket created successfully");
    } catch (error) {
      showError("Failed to create ticket");
      console.log("error: " + error);
    }
  };

  return (
    <div className="background">
      <div className="create-ticket-page">
        <h2>Create Ticket</h2>

        <div className="create-ticket-container">
          <form className="create-ticket-form" onSubmit={handleSubmit}>
            <div className="form-elements">
              <div className="form-group">
                <label htmlFor="title">Ticket Title</label>
                <input
                  id="title"
                  className="title-textbox"
                  name="title"
                  placeholder="Enter ticket title"
                  required
                />
              </div>

              <div className="form-group">
                <label htmlFor="description">Description</label>
                <textarea
                  id="description"
                  className="description-textbox"
                  name="description"
                  placeholder="Describe your issue..."
                  required
                />
              </div>
              <div className="form-group">
                <label htmlFor="priority">Priority</label>
                <select className="priority-select" name="priority">
                  <option value="" disabled>
                    Select Priority
                  </option>
                  {priorities.map((priority) => (
                    <option key={priority} value={priority}>
                      {priority}
                    </option>
                  ))}
                </select>
              </div>
              <div className="form-group">
                <label>Upload</label>
                <input type="file" multiple className="file-upload-btn" />
                <label>Uploaded files</label>
              </div>
              <div className="btn-group">
                <button
                  className="cancel-btn"
                  type="button"
                  onClick={() => navigate("/tickets")}
                >
                  Cancel
                </button>
                <button className="submit-btn">Submit</button>
              </div>
            </div>
          </form>
        </div>
      </div>
    </div>
  );
};
