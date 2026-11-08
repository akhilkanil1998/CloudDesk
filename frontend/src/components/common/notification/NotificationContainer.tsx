import { NotificationItem } from "./Notification";
import { useNotification } from "../../../hooks/useNotification";

// Container component responsible for displaying the active notification.
export const NotificationContainer = () => {
  // Accesses the notification state from the Notification Context.
  // The notification will be either an object or null.
  const { notification } = useNotification();
  console.log("Current notification:", notification);

  // Conditional rendering:
  // If a notification exists, render NotificationItem and pass it as a prop.
  // If notification is null, render nothing.
  return notification && <NotificationItem notification={notification} />;
};
