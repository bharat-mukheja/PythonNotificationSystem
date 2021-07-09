import platform
from pynotifier import Notification

# Notification destinations - Desktop, Slack, Discord, Email, Android/iOS, DBus, Multicast, IP unicast
# Notification sources - Files, Process, Filtered file/process

def system_notification(title:str,message:str='Message Body Empty'):
    Notification(title=title,description=message).send()

