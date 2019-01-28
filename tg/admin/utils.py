import re
import config

conf = config.get_config()

def parse_bets(text):
    _bets = text.strip()

    if not len(text):
        return []

    delimiters = [
        '\n \n',
        '\n\n'
    ]

    delimiter = None
    max = 0

    for d in delimiters:
        bets_count = len(_bets.split(d))

        if bets_count > max:
            max = bets_count
            delimiter = d

    _bets = _bets.split(delimiter)

    map(lambda x: x.strip(), _bets)

    if not len(_bets):
        return []

    parsed = []

    for bet in _bets:
        parsed.append(parse_bet(bet))

    return parsed



def parse_bet(bet):
    _bet = bet.strip()

    if not len(_bet):
        return None

    match = re.search(conf.REGEX_BET_COEF, bet)

    if match:
        return {
            'content': _bet,
            'coef': float(match.group(1))
        }

    return None

def parse_users(text):
    users = text.strip()

    if not len(text):
        return []

    users = users.split('\n')

    map(lambda x: x.strip(), users)

    if not len(users):
        return []

    parsed = []

    for user in users:
        u = re.search(conf.REGEX_USERNAME, user)

        if u:
            parsed.append(u.group(0))

    return parsed