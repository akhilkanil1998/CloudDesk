import { useState, type ReactNode, useEffect } from "react";
import {
  NotificationContext,
  type Notification,
  type NotificationContextType,
} from "./NotificationContext";
import { NotificationContainer } from "../../components/common/notification/NotificationContainer";

// Defines the props accepted by NotificationProvider.
// ReactNode allows the provider to wrap any React components.
interface NotificationProviderProps {
  children: ReactNode;
}

export const NotificationProvider = ({
  children,
}: NotificationProviderProps) => {
  // Maintains the currently active notification.
  // Initially null means no notification is displayed.
  const [notification, setNotification] = useState<Notification | null>(null);

  // Handles the automatic dismissal of notifications.
  // This effect runs whenever the notification state changes.
  useEffect(() => {
    // If there is no active notification, there is no need to start a timer.
    if (notification === null) return;
    // Starts a timer that will execute after 4 seconds (4000 milliseconds).
    const timer = setTimeout(() => {
      // Clears the notification state after 4 seconds.
      // This causes React to re-render and remove the notification from the UI.

      setNotification(null);
    }, 4000);
    // Cleanup function:
    // React executes this before running the effect again
    // when the notification changes, or when the component unmounts.

    return () => {
      // Cancels the previously scheduled timer.
      // This prevents an older notification's timer from interfering
      // with a newer notification.
      clearTimeout(timer);
    };
  }, [notification]);

  // Common function responsible for creating and updating notifications.
  // Accepts a message and notification type.
  const showNotification = (
    message: string,
    type: Notification["type"],
  ): void => {
    console.log("Notification triggered:", message, type);

    setNotification({ id: Date.now(), message, type });
  };

  // Wrapper functions provide a simple API for other components.
  // Each function specifies the notification type internally.
  const showSuccess = (message: string) => {
    showNotification(message, "success");
  };
  const showError = (message: string) => {
    showNotification(message, "error");
  };
  const showWarning = (message: string) => {
    showNotification(message, "warning");
  };
  const showInfo = (message: string) => {
    showNotification(message, "info");
  };

  // Groups the current notification state and notification functions
  // into one object that follows the NotificationContextType interface.
  const notificationObject: NotificationContextType = {
    notification,
    showSuccess,
    showError,
    showWarning,
    showInfo,
  };

  // Makes the notification state and functions accessible
  // to all components rendered inside this provider.
  return (
    <NotificationContext.Provider value={notificationObject}>
      {children}
      <NotificationContainer />
    </NotificationContext.Provider>
  );
};
