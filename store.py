import pickle
import os
from config import get_config
from tg.decorators import singleton


@singleton
class Store:
    def __init__(self):
        self.config = get_config()

        if not os.path.exists(self.config.STORE_FILEPATH):
            self.data = self.get_initial_value()
        else:
            self.load()

    def get_initial_value(self):
        return {
            'users': {},
            'bets': []
        }

    def dump(self):
        with open(self.config.STORE_FILEPATH, 'wb') as f:
            pickle.dump(self.data, f)

    def load(self):
        with open(self.config.STORE_FILEPATH, 'rb') as f:
            self.data = pickle.load(f)

    def add_user(self, user):
        self.data['users'][user] = {
            'bets': []
        }

        self.dump()

    def add_bet(self, bet):
        self.data['bets'].append(bet)

        self.dump()
