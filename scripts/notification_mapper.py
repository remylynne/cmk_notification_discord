from ..models.classes import Notification, HostNotification, ServiceNotification
from ..models.types import notificationTypeByValue, hostStateByValue, serviceStateByValue
from ..util.config import context



def getNotification() -> Notification:
    host_name = context("NOTIFY_HOSTNAME")
    host_alias = context("NOTIFY_HOSTALIAS")
    type = notificationTypeByValue(context("NOTIFY_NOTIFICATIONTYPE"))
    time = context("NOTIFY_LONGDATETIME")
    site = context("OMD_SITE")

    if context("NOTIFY_WHAT") == "HOST":
        output = context("NOTIFY_HOSTOUTPUT")
        state = hostStateByValue(context("NOTIFY_HOSTSTATE"))
        return HostNotification(
            host_name=host_name,
            host_alias=host_alias,
            type=type,
            output=output,
            state=state,
            time=time,
            site=site,
        )
    elif context("NOTIFY_WHAT") == "SERVICE":
        service_description = context("NOTIFY_SERVICEDESC")
        output = context("NOTIFY_SERVICEOUTPUT")
        state = serviceStateByValue(context("NOTIFY_SERVICESTATE"))
        return ServiceNotification(
            host_name=host_name,
            host_alias=host_alias,
            type=type,
            output=output,
            service_description=service_description,
            state=state,
            time=time,
            site=site,
        )
    else:
        raise ValueError(f"Unknown NOTIFY_WHAT value: {context('NOTIFY_WHAT')}")