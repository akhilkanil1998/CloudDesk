import type { Notification } from "../../../contexts/notification/NotificationContext";
import "./notification.css";
interface NotificationProps {
  notification: Notification;
}
export const NotificationItem = ({ notification }: NotificationProps) => {
  return (
    <div className={`notification-${notification.type}`}>
      <p>{notification.type}</p>
      <p>{notification.message}</p>
    </div>
  );
};
