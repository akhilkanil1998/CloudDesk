import { useContext } from "react";
import { NotificationContext } from "../contexts/notification/NotificationContext";

// Custom hook to access the notification context
// from any component inside NotificationProvider.
export const useNotification = () => {
  // Retrieves the value provided by NotificationContext.Provider.
  const result = useContext(NotificationContext);

  // Checks whether the component is being used outside
  // NotificationProvider. If so, throw a meaningful error.
  if (result === undefined) {
    throw new Error("useNotification must be used within NotificationProvider");
  }

  // Returns the notification state and notification functions
  // so consuming components can use them.
  return result;
};
