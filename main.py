import pync
import platform

_systems_function = {
    'Darwin':pync.notify,
    'Linux':None,
    'Windows':None
}

def system_notification(message:str,title:str=None):
    os = platform.system()
    _systems_function[os](message,title=title)