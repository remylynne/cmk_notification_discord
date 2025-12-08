from enum import Enum



class HostState(Enum):
    UP = "UP"
    DOWN = "DOWN"
    UNREACHABLE = "UNREACH"

def hostStateByValue(value: str) -> HostState:
    for state in HostState:
        if state.value == value:
            return state
    raise ValueError(f"Unknown HostState value: {value}")

class ServiceState(Enum):
    OK = "OK"
    WARNING = "WARNING"
    CRITICAL = "CRIT"
    UNKNOWN = "UNKNOWN"

def serviceStateByValue(value: str) -> ServiceState:
    for state in ServiceState:
        if state.value == value:
            return state
    raise ValueError(f"Unknown ServiceState value: {value}")

class NotificationType(Enum):
    PROBLEM = "PROBLEM"
    RECOVERY = "RECOVERY"
    ACKNOWLEDGEMENT = "ACKNOWLEDGEMENT"
    FLAPPING_START = "FLAPPINGSTART"
    FLAPPING_STOP = "FLAPPINGSTOP"
    DOWNTIME_START = "DOWNTIMESTART"
    DOWNTIME_END = "DOWNTIMEEND"
    DOWNTIME_CANCELLED = "DOWNTIMECANCELLED"
    CUSTOM = "CUSTOM"
    ALERT_HANDLER = "ALERTHANDLER"

def notificationTypeByValue(value: str) -> NotificationType:
    for type in NotificationType:
        if type.value == value:
            return type
    raise ValueError(f"Unknown NotificationType value: {value}")