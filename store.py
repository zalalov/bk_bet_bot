import pickle
import os
from collections import defaultdict
from config import get_config
from tg.decorators import singleton


@singleton
class Store:
    def __init__(self):
        self.data = {
            'users': {},
            'bets': []
        }

        self.config = get_config()

        if not os.path.exists(self.config.STORE_FILEPATH):
            self.data = {
                'users': {}
            }
        else:
            self.load()

    def dumps(self, ):
        return pickle.dump(self.data, self.config.STORE_FILEPATH)

    def load(self):
        self.data = pickle.load(self.config.STORE_FILEPATH)

    def add_user(self, user):
        self.data['users'][user] = {
            'bets': []
        }

        self.dumps()

    def add_bet(self, bet):
        self.data['bets'].append(bet)
