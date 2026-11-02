import type { TicketPriority } from "../../types/ticket";
import "./css/createTicket.css";

export const CreateTicket = () => {
  const priorities: TicketPriority[] = ["Low", "High", "Urgent"];
  return (
    <div className="background">
      <div className="create-ticket-page">
        <h2>Create Ticket</h2>

        <div className="create-ticket-container">
          <form className="create-ticket-form">
            <div className="form-elements">
              <div className="form-group">
                <label htmlFor="title">Ticket Title</label>
                <input
                  id="title"
                  className="title-textbox"
                  placeholder="Enter ticket title"
                />
              </div>

              <div className="form-group">
                <label htmlFor="description">Description</label>
                <textarea
                  id="description"
                  className="description-textbox"
                  placeholder="Describe your issue..."
                />
              </div>
              <div className="form-group">
                <label htmlFor="priority">Priority</label>
                <select className="priority-select">
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
                  <input type="file" className="file-upload-btn"/>
              </div>
              <div className="btn-group">
                  <button className="cancel-btn" type="button">Cancel</button>
                  <button className="submit-btn">Submit</button>
              </div>
            </div>
          </form>
        </div>
      </div>
    </div>
  );
};
