from .types import HostState, NotificationType, ServiceState
from dataclasses import dataclass
from typing import Literal, Union



@dataclass # common variables
class BaseNotification:
    host_name: str
    host_alias: str
    type: NotificationType
    output: str
    time: str
    site: str


@dataclass # variables specific to host notifications
class HostNotification(BaseNotification):
    state: HostState
    what: Literal["HOST"] = "HOST"


@dataclass # variables specific to service notifications
class ServiceNotification(BaseNotification):
    service_description: str
    state: ServiceState
    what: Literal["SERVICE"] = "SERVICE"

Notification = Union[HostNotification, ServiceNotification]