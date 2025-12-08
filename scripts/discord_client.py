from ..models.classes import Notification
from ..models.discord import Embed, Field, Footer, Message
from ..util.colors import getColorForNotification
from ..util import config
import requests
import sys



def _buildInfoEmbed(notification: Notification) -> Embed:
    if notification.what == "HOST":
        title = f"Host {notification.type} notification"
    else:
        title = f"Service {notification.type} notification"

    facts = [
        Field(
            name="Host",
            value=f"{notification.host_alias} ({notification.host_name})"
        )
    ]

    if (notification.what == "SERVICE"):
        facts.append(
            Field(
                name="Service",
                value=notification.service_description
            )
        )

    facts.append(
        Field(
            name="State",
            value=notification.state.name
        )
    )

    return Embed(
        title=title,
        color=getColorForNotification(notification),
        fields=facts
    )

def _buildOutputEmbed(notification: Notification) -> Embed:
    return Embed(
        title="Additional Info:",
        color=getColorForNotification(notification),
        description=notification.output,
        footer=Footer(
            text=f"CheckMK Notification from {notification.site}: {notification.time}",
            icon_url=config.icon
        )
    )

def buildDiscordMessage(notification: Notification) -> Message:
    return Message(embeds=[
        _buildInfoEmbed(notification),
        _buildOutputEmbed(notification)
    ])

def sendDiscordMessage(message: Message) -> int:
    webhook_url = config.parameter("discord_webhook_url")

    if not webhook_url:
        sys.stderr.write("No webhook url provided (webhook_url=<webhook_url>)")
        return 2

    response = requests.post(webhook_url, json=message)
    if 400 <= response.status_code <= 599:
        sys.stderr.write(f"HTTP {response.status_code} while sending notification to discord: {response.text}")
        if 400 <= response.status_code <= 499:
            return 2
        else: # 500 <= response.status_code <= 599
            return 1

    return 0