#!/usr/bin/env python3
# Discord Webhook

from .scripts.discord_client import buildDiscordMessage, sendDiscordMessage
from .scripts.notification_mapper import getNotification



if __name__ == "__main__":
    notification = getNotification()
    message = buildDiscordMessage(notification)
    sendDiscordMessage(message)