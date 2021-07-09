import platform
from pynotifier import Notification

def system_notification(title:str,message:str='Message Body Empty'):
    Notification(title=title,description=message).send()

