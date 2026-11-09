import type { Notification } from "../../../contexts/notification/NotificationContext";
import { useNotification } from "../../../hooks/useNotification";
import "./notification.css";
interface NotificationProps {
  notification: Notification;
}
export const NotificationItem = ({ notification }: NotificationProps) => {
  const { dismissNotification } = useNotification();
  return (
    <div className={`notification-${notification.type}`}>
      <button className="close-btn" onClick={dismissNotification}>x</button>
      <p>{notification.type}</p>
      <p>{notification.message}</p>
    </div>
  );
};
