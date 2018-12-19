from config import get_config
from tg.bot import bot

def singleton(class_):
    instances = {}

    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return getinstance

def is_user_admin(fn):
    conf = get_config()

    def wrapper(message, *args, **kwargs):
        if conf.is_user_admin(message.from_user.username):
            fn(message, *args, **kwargs)

    return wrapper

def is_admin_mode(fn):
    conf = get_config()

    def decorator(message, *args, **kwargs):
        if conf.is_admin_mode():
            fn(message, *args, **kwargs)

    return decorator
