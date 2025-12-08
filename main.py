from .scripts.discord_client import buildDiscordMessage, sendDiscordMessage
from .scripts.notification_mapper import getNotification



def main():
    notification = getNotification()
    message = buildDiscordMessage(notification)
    sendDiscordMessage(message)