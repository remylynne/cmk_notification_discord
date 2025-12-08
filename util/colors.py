from ..models.classes import Notification
from ..models.types import NotificationType, HostState, ServiceState



def getColorForNotification(notification: Notification) -> int:
    if notification.type == NotificationType.PROBLEM:
        if notification.what == "HOST":
            if notification.state == HostState.DOWN:
                return 0xFF0000
            elif notification.state == HostState.UNREACHABLE:
                return 0x8B0000
        else:  # SERVICE
            if notification.state == ServiceState.CRITICAL:
                return 0xFF0000
            elif notification.state == ServiceState.WARNING:
                return 0xFFA500
            elif notification.state == ServiceState.UNKNOWN:
                return 0x800080
    elif notification.type == NotificationType.RECOVERY:
        return 0x00FF00
    elif notification.type == NotificationType.ACKNOWLEDGEMENT:
        return 0x0000FF
    elif notification.type == NotificationType.FLAPPING_START:
        return 0xFF69B4
    elif notification.type == NotificationType.FLAPPING_STOP:
        return 0x00FFFF
    elif notification.type in {NotificationType.DOWNTIME_START, NotificationType.DOWNTIME_END, NotificationType.DOWNTIME_CANCELLED}:
        return 0xA9A9A9
    elif notification.type == NotificationType.CUSTOM:
        return 0x00FFFF
    elif notification.type == NotificationType.ALERT_HANDLER:
        return 0x008080
    
    return 0xFFFFFF  # fallback