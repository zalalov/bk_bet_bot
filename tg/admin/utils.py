import re

def parse_bets(bets):
    _bets = bets.strip()

    if not len(bets):
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

    match = re.search(r'\u041a\u0424 (\d+[.]\d+|\d+)', bet)

    if match:
        return {
            'content': _bet,
            'coef': float(match.group(1))
        }

    return None