import os


class Config:
    DB_CONNECTION_STRING = 'sqlite:///bet.db'


class Dev(Config):
    pass


class Admin(Config):
    MODE = 'admin'


class User(Config):
    MODE = 'user'


def get_config():
    if os.environ.get('DEBUG') is not None:
        return

    if os.environ.get('BOT_ENV') == 'ADMIN':
        return Admin

    return User

