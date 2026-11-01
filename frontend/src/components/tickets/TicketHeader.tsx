interface TicketHeaderProps{
    total:number;
}

export const TicketHeader= ({total}:TicketHeaderProps) => {
    return(
        <div className="ticket-header">
            <h1>Tickets ({total})</h1>
            <button className="create-ticket-button">
                &nbsp;Create&nbsp;
            </button>
        </div>
    )
}