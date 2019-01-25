import os
import utils



class Config:
    MODE = None
    DB_CONNECTION_STRING = 'sqlite:///bet.db'
    TG_BOT_TOKEN = os.environ['BOT_TOKEN']
    ADMINS = [
        # '<ADMIN_NAME>'
    ]
    STORE_FILEPATH = os.path.join(utils.script_path(), 'store.pickle')

    def is_admin_mode(self):
        return self.MODE == Admin.MODE

    def is_user_mode(self):
        return self.MODE == User.MODE

    def is_user_admin(self, username):
        return username in self.ADMINS


class Dev(Config):
    pass


class Admin(Config):
    MODE = 'admin'


class User(Config):
    MODE = 'user'


def get_config():
    """
    Config fabric method
    :return:
    """
    if os.environ.get('DEBUG') is not None:
        return Dev()

    if os.environ.get('BOT_ENV') == 'ADMIN':
        return Admin()

    return User()
