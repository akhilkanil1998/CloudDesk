import { createContext } from "react";

//	Describes the notification object
export interface Notification {
  id: number;
  message: string;
  type: "success" | "error" | "warning" | "info";
}

// Describes what other components can access
export interface NotificationContextType {
  notification: Notification | null;
  showSuccess: (message: string) => void;
  showError: (message: string) => void;
  showWarning: (message: string) => void;
  showInfo: (message: string) => void;
  dismissNotification: () => void;
}

export const NotificationContext = createContext<
  NotificationContextType | undefined
>(undefined);
